import os
from pathlib import Path
import subprocess
import tempfile
import unittest

SCRIPT = Path(__file__).with_name('upload-only.py')

class UploadOnlyTest(unittest.TestCase):
    def test_rejects_commands_without_executing(self):
        for command in ('', 'git-receive-pack \'/fixture.git\'',
                        "git-upload-pack '/other.git'", "git-upload-pack '/fixture.git'; id",
                        'git-upload-pack /fixture.git', 'sh'):
            with self.subTest(command=command):
                result = subprocess.run(['python3', str(SCRIPT)],
                    env={**os.environ, 'SSH_ORIGINAL_COMMAND': command}, capture_output=True)
                self.assertEqual(result.returncode, 1)
                self.assertIn(b'rejected', result.stderr)

    def test_real_clone_of_synthetic_fixture(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source, bare, clone = (root / n for n in ('source', 'fixture.git', 'clone'))
            subprocess.run(['git', 'init', '-q', str(source)], check=True)
            (source / 'README').write_text('synthetic fixture only\n')
            subprocess.run(['git', '-C', str(source), 'add', 'README'], check=True)
            subprocess.run(['git', '-C', str(source), '-c', 'user.name=Fixture',
                            '-c', 'user.email=fixture@example.invalid', 'commit', '-qm', 'fixture'], check=True)
            subprocess.run(['git', 'clone', '-q', '--bare', str(source), str(bare)], check=True)
            # Replace only the fixed repository path in a disposable copy, not the command check.
            test_script = root / 'forced.py'
            test_script.write_text(SCRIPT.read_text().replace('/srv/private-git/fixture.git', str(bare)))
            ssh = root / 'ssh'
            ssh.write_text('#!/bin/sh\nexport SSH_ORIGINAL_COMMAND="$2"\nexec python3 "' + str(test_script) + '"\n')
            ssh.chmod(0o700)
            subprocess.run(['git', 'clone', '-q', 'ssh://fixture@localhost/fixture.git', str(clone)],
                           env={**os.environ, 'GIT_SSH_COMMAND': str(ssh), 'GIT_SSH_VARIANT': 'simple'}, check=True)
            self.assertEqual((clone / 'README').read_text(), 'synthetic fixture only\n')
            result = subprocess.run(['git', '-C', str(clone), 'push', 'origin', 'HEAD'],
                           env={**os.environ, 'GIT_SSH_COMMAND': str(ssh), 'GIT_SSH_VARIANT': 'simple'}, capture_output=True)
            self.assertNotEqual(result.returncode, 0)

if __name__ == '__main__':
    unittest.main()
