#!/usr/bin/env python3
"""Check local client discovery in the calling role, not access to any service."""
import shutil
import subprocess


PROBES = {
    "gh": ["--version"],
    "kubectl": ["version", "--client"],
    "kustomize": ["version"],
    "helm": ["version", "--short"],
    "talosctl": ["version", "--client", "--short"],
}


def main():
    failed = False
    for name, args in PROBES.items():
        path = shutil.which(name)
        if not path:
            print(f"{name}: missing")
            failed = True
            continue
        try:
            code = subprocess.run([path, *args], timeout=15, stdin=subprocess.DEVNULL,
                                  stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode
            status = "ok" if code == 0 else f"failed({code})"
        except subprocess.TimeoutExpired:
            status = "timeout"
        except OSError:
            status = "not runnable"
        print(f"{name}: {status} {path}")
        failed |= status != "ok"
    return int(failed)


if __name__ == "__main__":
    raise SystemExit(main())
