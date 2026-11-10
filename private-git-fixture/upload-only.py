#!/usr/bin/env python3
"""Forced SSH command for the synthetic fixture only."""
import os
import sys

REPOSITORY = "/srv/private-git/fixture.git"
COMMAND = "git-upload-pack '/fixture.git'"

def main():
    if os.environ.get("SSH_ORIGINAL_COMMAND") != COMMAND:
        print("rejected: only fixture upload-pack is allowed", file=sys.stderr)
        return 1
    os.execv("/usr/bin/git-upload-pack", ["git-upload-pack", REPOSITORY])

if __name__ == "__main__":
    sys.exit(main())
