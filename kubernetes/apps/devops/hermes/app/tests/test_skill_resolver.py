"""Behavioral tests against a copy of the pinned image's Hermes resolver.

Run: /opt/hermes/.venv/bin/python -m unittest discover -s kubernetes/apps/devops/hermes/app/tests
Set HERMES_SOURCE to the extracted source tree when not running in the image.
"""
import importlib.util
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

SOURCE = Path(os.environ.get("HERMES_SOURCE", "/opt/hermes"))
sys.path.insert(0, str(SOURCE))


class ResolverTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        copied = self.base / "skills_tool.py"
        shutil.copyfile(SOURCE / "tools/skills_tool.py", copied)
        # The test can run unpatched to demonstrate the original collision.
        if os.environ.get("TEST_UNPATCHED") != "1":
            patcher = Path(__file__).resolve().parents[1] / "resources/patch-skill-resolver.py"
            import runpy
            runpy.run_path(str(patcher))["patch_file"](copied)
        spec = importlib.util.spec_from_file_location("resolver_under_test", copied)
        self.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.module)
        self.local = self.base / "local"
        self.shared = self.base / "shared"
        self.project = self.base / "project"
        for root in (self.local, self.shared, self.project):
            root.mkdir()
        self.dirs = patch.object(self.module, "_skill_search_dirs", side_effect=lambda: ([], [self.local, self.shared], self.local))
        self.dirs.start()
        self.addCleanup(self.dirs.stop)
        self.disabled = patch.object(self.module, "_is_skill_disabled", return_value=False)
        self.disabled.start()
        self.addCleanup(self.disabled.stop)

    def skill(self, root, category, body):
        directory = root / category / "example"
        (directory / "references").mkdir(parents=True)
        (directory / "SKILL.md").write_text(f"---\nname: example\ndescription: {body}\n---\n{body}\n")
        (directory / "references/api.md").write_text(body + " reference")
        return directory

    def view(self, name="example", file_path=None):
        return json.loads(self.module.skill_view(name, file_path=file_path, preprocess=False))

    def test_local_override_matches_listing_and_preserves_shared(self):
        local = self.skill(self.local, "custom", "local content")
        shared = self.skill(self.shared, "upstream", "shared content")
        before = (shared / "SKILL.md").read_bytes()
        listed = json.loads(self.module.skills_list())["skills"]
        self.assertEqual([item["description"] for item in listed if item["name"] == "example"], ["local content"])
        viewed = self.view()
        self.assertTrue(viewed["success"], viewed)
        self.assertEqual(viewed["skill_dir"], str(local))
        self.assertIn("local content", viewed["content"])
        self.assertEqual(self.view(file_path="references/api.md")["content"], "local content reference")
        self.assertEqual((shared / "SKILL.md").read_bytes(), before)
        self.assertEqual((shared / "references/api.md").read_text(), "shared content reference")

    def test_project_override_and_reference(self):
        project = self.skill(self.project, "team", "project content")
        self.skill(self.local, "custom", "local content")
        self.skill(self.shared, "upstream", "shared content")
        with patch.object(self.module, "_skill_search_dirs", return_value=([self.project], [self.project, self.local, self.shared], self.local)), patch("agent.skill_utils.is_quarantined_project_skill", return_value=False):
            self.assertEqual(self.view()["skill_dir"], str(project))
            self.assertEqual(self.view(file_path="references/api.md")["content"], "project content reference")

    def test_same_root_different_skills_remain_ambiguous(self):
        self.skill(self.local, "first", "first content")
        self.skill(self.local, "second", "second content")
        self.skill(self.shared, "upstream", "shared content")
        result = self.view()
        self.assertFalse(result["success"])
        self.assertIn("Ambiguous skill name", result["error"])
        self.assertEqual(len(result["matches"]), 2)

    def test_different_project_roots_remain_ambiguous(self):
        other = self.base / "other-project"
        other.mkdir()
        self.skill(self.project, "team", "project one")
        self.skill(other, "team", "project two")
        self.skill(self.local, "custom", "local content")
        with patch.object(self.module, "_skill_search_dirs", return_value=([self.project, other], [self.project, other, self.local, self.shared], self.local)):
            result = self.view()
        self.assertFalse(result["success"])
        self.assertIn("Ambiguous skill name", result["error"])
        self.assertEqual(len(result["matches"]), 2)

    def test_quarantined_project_blocks_local_fallback_and_reference(self):
        self.skill(self.project, "team", "quarantined")
        self.skill(self.local, "custom", "local content")
        with patch.object(self.module, "_skill_search_dirs", return_value=([self.project], [self.project, self.local, self.shared], self.local)), patch("agent.skill_utils.is_quarantined_project_skill", return_value=True):
            for name, file_path in (("example", None), ("team/example", "references/api.md")):
                result = self.view(name, file_path)
                self.assertFalse(result["success"], result)
                self.assertIn("quarantined", result["error"])

    def test_plugin_qualified_dispatch_ignores_local_collision(self):
        from unittest.mock import MagicMock
        plugin = self.skill(self.base / "plugin", "skills", "plugin content")
        self.skill(self.local, "custom", "local content")
        manager = MagicMock()
        manager.find_plugin_skill.return_value = plugin / "SKILL.md"
        with patch("hermes_cli.plugins.discover_plugins"), patch("hermes_cli.plugins.get_plugin_manager", return_value=manager):
            result = self.view("sample:example")
        self.assertTrue(result["success"], result)
        self.assertIn("plugin content", result["content"])
        manager.find_plugin_skill.assert_called_with("sample:example")

    def test_shared_updates_visible_without_local_override(self):
        shared = self.skill(self.shared, "upstream", "version one")
        self.assertIn("version one", self.view()["content"])
        (shared / "SKILL.md").write_text("---\nname: example\ndescription: version two\n---\nversion two\n")
        self.assertIn("version two", self.view()["content"])

    def test_identical_local_copy_still_shadows_later_shared_update(self):
        self.skill(self.local, "same", "version one")
        shared = self.skill(self.shared, "same", "version one")
        (shared / "SKILL.md").write_text("---\nname: example\ndescription: version two\n---\nversion two\n")
        self.assertIn("version one", self.view()["content"])
        self.assertIn("version one", self.view("same/example")["content"])

    def test_explicit_shared_category_and_reference(self):
        self.skill(self.local, "custom", "local content")
        shared = self.skill(self.shared, "upstream", "shared content")
        self.assertEqual(self.view("upstream/example")["skill_dir"], str(shared))
        self.assertEqual(self.view("upstream/example", "references/api.md")["content"], "shared content reference")


if __name__ == "__main__":
    unittest.main()
