"""Regression test for Flux resources appearing after the root sync."""

import os
from pathlib import Path
import re
import subprocess
import tempfile
import unittest


SCRIPT = Path(__file__).with_name("cluster.sh")
EXPECTED = (
    "kustomization/cluster-apps --namespace flux-system",
    "kustomization/flux-system --namespace flux-system",
    "kustomization/flux-instance --namespace flux-system",
    "kustomization/flux-operator --namespace flux-system",
    "kustomization/cilium --namespace kube-system",
    "kustomization/coredns --namespace kube-system",
    "helmrelease/flux-instance --namespace flux-system",
    "helmrelease/flux-operator --namespace flux-system",
    "helmrelease/cilium --namespace kube-system",
    "helmrelease/coredns --namespace kube-system",
)


class ClusterHealthTest(unittest.TestCase):
    def test_waits_for_each_expected_flux_resource_to_appear_and_be_ready(self):
        source = SCRIPT.read_text()
        match = re.search(r"^assert_cluster_health\(\) \{.*?^\}", source, re.M | re.S)
        self.assertIsNotNone(match)
        assert match is not None
        with tempfile.TemporaryDirectory() as directory:
            work = Path(directory)
            kubectl = work / "kubectl"
            kubectl.write_text(
                "#!/bin/sh\n"
                'printf "%s\\n" "$*" >> "$KUBE_MOCK_LOG"\n'
                'case "$1" in\n'
                '  helmreleases) echo "error: no matching resources found" >&2; exit 1;;\n'
                'esac\n'
            )
            kubectl.chmod(0o755)
            log = work / "calls"
            env = dict(os.environ, PATH=f"{work}:{os.environ['PATH']}", KUBE_MOCK_LOG=str(log))
            result = subprocess.run(
                ["bash", "-euo", "pipefail", "-c", match.group() + "\nassert_cluster_health"],
                env=env,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            calls = log.read_text().splitlines()
            for resource in EXPECTED:
                create = [i for i, call in enumerate(calls) if resource in call and "--for=create" in call]
                ready = [i for i, call in enumerate(calls) if resource in call and "--for=condition=Ready" in call]
                self.assertTrue(create, resource)
                self.assertTrue(ready, resource)
                self.assertLess(create[0], ready[0], resource)


if __name__ == "__main__":
    unittest.main()
