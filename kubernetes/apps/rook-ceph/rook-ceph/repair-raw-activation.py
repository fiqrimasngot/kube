#!/usr/bin/env python3
"""Work around ceph-volume's raw-activation scan of unavailable RBD devices.

Run with --apply to patch the OSD deployments; otherwise use server dry-run.
This is a runtime workaround: Rook can regenerate these deployment commands.
Remove it when the Ceph image excludes RBD devices from raw activation scans.
"""

import argparse
import json
import subprocess


PREFIX = """python3 - <<'CEPH_RAW_SCAN_FIX'
from pathlib import Path
import ceph_volume.objectstore.raw as raw
path = Path(raw.__file__)
source = path.read_text()
needle = "            device: str = d.get('NAME', '')\\n"
replacement = needle + "            if device.startswith(('/dev/rbd', '/dev/mapper/luks-rbd-')):\\n                continue\\n"
if replacement not in source:
    assert source.count(needle) == 1, 'Unexpected ceph-volume source; refusing to modify'
    path.write_text(source.replace(needle, replacement))
CEPH_RAW_SCAN_FIX
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    deployments = json.loads(
        subprocess.check_output(
            ["kubectl", "get", "deployments", "-n", "rook-ceph", "-l", "app=rook-ceph-osd", "-o", "json"]
        )
    )
    for deployment in deployments["items"]:
        name = deployment["metadata"]["name"]
        activate = next(
            container
            for container in deployment["spec"]["template"]["spec"]["initContainers"]
            if container["name"] == "activate"
        )
        command = activate["command"]
        if "CEPH_RAW_SCAN_FIX" in command[-1]:
            print(f"{name}: already patched")
            continue
        if activate["image"] != "quay.io/ceph/ceph:v20.2.4":
            raise RuntimeError(f"{name}: image differs from the verified v20.2.4")
        if len(command) != 3 or command[:2] != ["/bin/bash", "-c"]:
            raise RuntimeError(f"{name}: unexpected activation command")
        patch = {
            "spec": {"template": {"spec": {"initContainers": [{
                "name": "activate", "command": command[:2] + [PREFIX + command[2]]
            }]}}}
        }
        invocation = ["kubectl", "patch", "deployment", name, "-n", "rook-ceph", "--type=strategic", "-p", json.dumps(patch)]
        if not args.apply:
            invocation.append("--dry-run=server")
        subprocess.run(invocation, check=True)


if __name__ == "__main__":
    main()
