"""The QEMU cluster reconciles only its representative foundation."""

import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[3]
SCRIPT = Path(__file__).with_name("minimal_apps.py")


class MinimalAppsTest(unittest.TestCase):
    def test_published_apps_exclude_production_workloads(self):
        with tempfile.TemporaryDirectory() as directory:
            kubernetes = Path(directory) / "kubernetes"
            shutil.copytree(ROOT / "kubernetes", kubernetes)
            subprocess.run(["python3", str(SCRIPT), str(kubernetes)], check=True)
            rendered = subprocess.run(
                ["kubectl", "kustomize", str(kubernetes / "apps")],
                check=True, capture_output=True, text=True,
            ).stdout
            resources = subprocess.run(
                ["yq", "-o=json", "-I=0", "--no-doc", ".", "-"],
                input=rendered, capture_output=True, text=True, check=True,
            ).stdout
            # yq returns one JSON document per YAML resource.
            documents = [json.loads(line) for line in resources.splitlines() if line.strip()]
            kustomizations = {item["metadata"]["name"] for item in documents
                              if item["kind"] == "Kustomization"}
            self.assertEqual(kustomizations, {"cilium", "coredns", "flux-operator", "flux-instance"})
            self.assertNotIn("HelmRelease", {item["kind"] for item in documents})
            self.assertIn("default", {item["metadata"]["name"] for item in documents
                                      if item["kind"] == "Namespace"})
            self.assertTrue((kubernetes / "apps/default/kustomization.yaml").exists())
            self.assertTrue((kubernetes / "apps/default/namespace.yaml").exists())
            self.assertTrue((kubernetes / "apps/kube-system/cilium/app/helmrelease.yaml").exists())


if __name__ == "__main__":
    unittest.main()
