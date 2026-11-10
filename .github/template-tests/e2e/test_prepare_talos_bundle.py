"""Check that E2E preparation never reuses the production Talos bundle."""

import os
from pathlib import Path
import subprocess
from string import Template
import tempfile
import tomllib
import unittest


SCRIPT = Path(__file__).with_name("cluster.sh")


class PrepareTalosBundleTest(unittest.TestCase):
    def run_prepare_steps(self, provisioned, should_remove):
        source = SCRIPT.read_text()
        start = source.index('echo "==> configure"', source.index("prepare() {"))
        end = source.index("\n# Flux's FluxInstance", start)
        configure_steps = source[start:end]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "talos").mkdir()
            (root / "talos/secrets.sops.yaml").write_text("production-encrypted-bundle")
            bin_dir = root / "bin"
            bin_dir.mkdir()
            just = bin_dir / "just"
            just.write_text("#!/bin/sh\nif [ \"$1\" = configure ]; then\n  test ! -e talos/secrets.sops.yaml || exit 42\nfi\n")
            just.chmod(0o755)
            env = {**os.environ, "PATH": f"{bin_dir}:{os.environ['PATH']}", "PROVISIONED": str(provisioned).lower()}
            if not should_remove:
                just.write_text("#!/bin/sh\nif [ \"$1\" = configure ]; then\n  test -e talos/secrets.sops.yaml || exit 42\nfi\n")
            result = subprocess.run(["bash", "-euo", "pipefail", "-c", configure_steps], cwd=root, env=env, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual((root / "talos/secrets.sops.yaml").exists(), not should_remove)

    def test_ci_uses_a_fresh_talos_bundle(self):
        self.run_prepare_steps(provisioned=True, should_remove=True)

    def test_local_preserves_existing_bundle(self):
        self.run_prepare_steps(provisioned=False, should_remove=False)

    def test_qemu_node_uses_runner_mtu(self):
        template = SCRIPT.with_name("node.toml.tmpl").read_text()
        env = {**os.environ, "E2E_NODE_NAME": "e2e-0", "E2E_NODE_ADDRESS": "10.9.0.2",
               "E2E_NODE_CONTROLLER": "true", "E2E_NODE_DISK": "/dev/vda",
               "E2E_NODE_MAC": "02:00:00:00:00:01", "E2E_NODE_MTU": "1280"}
        rendered = Template(template).substitute(env)
        self.assertEqual(tomllib.loads(rendered)["nodes"][0]["mtu"], 1280)


if __name__ == "__main__":
    unittest.main()
