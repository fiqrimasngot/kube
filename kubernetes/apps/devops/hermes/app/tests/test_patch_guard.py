import runpy
import os
import shutil
import tempfile
import unittest
from pathlib import Path

PATCH = Path(__file__).resolve().parents[1] / 'resources/patch-skill-resolver.py'
SOURCE = Path(os.environ.get('HERMES_SOURCE', '/opt/hermes')) / 'tools/skills_tool.py'

class PatchGuardTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.file = Path(self.tmp.name) / 'skills_tool.py'
        shutil.copyfile(SOURCE, self.file)
        self.patch = runpy.run_path(str(PATCH))['patch_file']

    def test_unexpected_source_fails_without_writing(self):
        self.file.write_bytes(self.file.read_bytes() + b'\n# unexpected change\n')
        before = self.file.read_bytes()
        with self.assertRaises(SystemExit):
            self.patch(self.file)
        self.assertEqual(self.file.read_bytes(), before)

    def test_malformed_source_rejected_without_writing(self):
        malformed = self.file.read_bytes() + b'\ndef broken(:\n'
        self.file.write_bytes(malformed)
        with self.assertRaises(SystemExit):
            self.patch(self.file)
        self.assertEqual(self.file.read_bytes(), malformed)

    def test_idempotent_but_tampered_patched_source_rejected(self):
        self.patch(self.file)
        expected = self.file.read_bytes()
        self.patch(self.file)
        self.assertEqual(self.file.read_bytes(), expected)
        self.file.write_bytes(expected + b'\n# tampered\n')
        with self.assertRaises(SystemExit):
            self.patch(self.file)
