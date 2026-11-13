"""Exercise the CI retry wrapper with real child processes."""
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).with_name("retry-network.sh")


class RetryNetworkTests(unittest.TestCase):
    def run_command(self, failures, message):
        with tempfile.TemporaryDirectory() as directory:
            counter = Path(directory) / "attempts"
            child = (
                "import pathlib, sys; "
                "p = pathlib.Path(sys.argv[1]); "
                "n = int(p.read_text()) + 1 if p.exists() else 1; "
                "p.write_text(str(n)); "
                "print(sys.argv[3] if n <= int(sys.argv[2]) else 'passed'); "
                "sys.exit(7 if n <= int(sys.argv[2]) else 0)"
            )
            result = subprocess.run(
                ["bash", str(SCRIPT), sys.executable, "-c", child,
                 str(counter), str(failures), message],
                capture_output=True, text=True,
                env={**os.environ, "NETWORK_RETRY_DELAY": "0"},
            )
            attempts = int(counter.read_text()) if counter.exists() else 0
            return result, attempts

    def test_recovers_from_transient_tls_error(self):
        result, attempts = self.run_command(
            1, "fetch https://example.test: tls: first record does not look like a TLS handshake"
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(attempts, 2)
        self.assertIn("passed", result.stdout)


    def test_persistent_tls_error_fails_after_three_attempts(self):
        result, attempts = self.run_command(
            10, "tls: first record does not look like a TLS handshake"
        )
        self.assertEqual(result.returncode, 7)
        self.assertEqual(attempts, 3)

    def test_validation_error_is_not_retried(self):
        result, attempts = self.run_command(10, "schema validation failed")
        self.assertEqual(result.returncode, 7)
        self.assertEqual(attempts, 1)

    def test_success_is_not_retried(self):
        result, attempts = self.run_command(0, "unused")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(attempts, 1)

    def test_requires_a_command(self):
        result = subprocess.run(["bash", str(SCRIPT)], capture_output=True)
        self.assertNotEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
