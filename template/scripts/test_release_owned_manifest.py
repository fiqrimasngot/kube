"""Exercise makejinja without touching the real generated cluster tree."""
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib
import unittest

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = Path("kubernetes/apps/default/study-planner/app/helmrelease.yaml")


class ReleaseOwnedManifestTests(unittest.TestCase):
    def test_reset_and_regeneration_preserve_release_owned_manifests(self):
        config = tomllib.loads((ROOT / "makejinja.toml").read_text())["makejinja"]
        manifests = [MANIFEST, Path("kubernetes/apps/default/amdglobal/app/helmrelease.yaml")]
        for present in (True, False):
            with self.subTest(present=present), tempfile.TemporaryDirectory() as directory:
                fixture = Path(directory)
                (fixture / "template").mkdir()
                shutil.copyfile(ROOT / "justfile", fixture / "justfile")
                shutil.copyfile(ROOT / "template/mod.just", fixture / "template/mod.just")
                expected = {}
                for manifest in manifests:
                    for source in config["inputs"]:
                        template = fixture / source / (str(manifest) + ".j2")
                        template.parent.mkdir(parents=True, exist_ok=True)
                        template.write_text("must not overwrite the release-owned manifest\n")
                    if present:
                        live = fixture / manifest
                        live.parent.mkdir(parents=True, exist_ok=True)
                        # Include arbitrary release-owned bytes, not just today's image tag.
                        expected[manifest] = (ROOT / manifest).read_bytes() + b"\n# release-owned sentinel\r\n"
                        live.write_bytes(expected[manifest])
                disposable = fixture / "kubernetes/reset-probe.txt"
                disposable.parent.mkdir(parents=True, exist_ok=True)
                disposable.write_text("reset must remove this")
                subprocess.run(["just", "--yes", "template", "reset"], cwd=fixture,
                               check=True, capture_output=True, text=True)
                self.assertFalse(disposable.exists())
                for manifest in manifests:
                    if present:
                        self.assertEqual((fixture / manifest).read_bytes(), expected[manifest])
                    else:
                        self.assertFalse((fixture / manifest).exists())
                (fixture / "template/config/probe.txt.j2").write_text("generation ran\n")
                settings = fixture / "makejinja.toml"
                settings.write_text("[makejinja]\n" + "\n".join(
                    key + " = " + json.dumps(config[key])
                    for key in ("inputs", "output", "exclude_patterns", "jinja_suffix", "force")
                ) + "\n")
                executable = Path(sys.executable).parent / "makejinja"
                subprocess.run([str(executable)], cwd=fixture, check=True,
                               env={**os.environ, "MAKEJINJA_SETTINGS": str(settings)},
                               capture_output=True, text=True)
                self.assertEqual((fixture / "probe.txt").read_text().strip(), "generation ran")
                for manifest in manifests:
                    if present:
                        self.assertEqual((fixture / manifest).read_bytes(), expected[manifest])
                    else:
                        self.assertFalse((fixture / manifest).exists())

    def test_regeneration_preserves_advanced_release_images(self):
        config = tomllib.loads((ROOT / "makejinja.toml").read_text())["makejinja"]
        with tempfile.TemporaryDirectory() as directory:
            fixture = Path(directory)
            # Use both configured input layers, including a conflicting override.
            for source in config["inputs"]:
                template = fixture / source / (str(MANIFEST) + ".j2")
                template.parent.mkdir(parents=True)
                shutil.copyfile(ROOT / "template/config" / (str(MANIFEST) + ".j2"), template)
            live = fixture / MANIFEST
            live.parent.mkdir(parents=True)
            current = (ROOT / MANIFEST).read_text()
            digests = iter(["a" * 64, "b" * 64])
            advanced = re.sub(
                r"tag: build-[^\n]+",
                lambda match: "tag: build-" + "f" * 40 + "@sha256:" + next(digests),
                current,
            )
            self.assertNotEqual(current, advanced)
            self.assertEqual(advanced.count("tag: build-" + "f" * 40), 2)
            live.write_text(advanced)
            probe = fixture / "template/config/probe.txt.j2"
            probe.write_text("generation ran\n")
            # Keep the real ownership/exclusion settings, but omit the cluster
            # inventory loader: this isolated fixture needs no cluster credentials.
            settings = fixture / "makejinja.toml"
            settings.write_text("[makejinja]\n" + "\n".join(
                key + " = " + json.dumps(config[key])
                for key in ("inputs", "output", "exclude_patterns", "jinja_suffix", "force")
            ) + "\n")
            executable = Path(sys.executable).parent / "makejinja"
            subprocess.run([str(executable)], cwd=fixture, check=True,
                           env={**os.environ, "MAKEJINJA_SETTINGS": str(settings)},
                           capture_output=True, text=True)
            self.assertEqual(live.read_text(), advanced)
            self.assertEqual((fixture / "probe.txt").read_text().strip(), "generation ran")


if __name__ == "__main__":
    unittest.main()
