"""Apply the skill-root precedence fix to the pinned Hermes source copy."""
from pathlib import Path
import hashlib
import sys

SOURCE_SHA256 = "0d47bda41ed9d1ec84856df3d336a42bb94161e89bd9a8b857e76ec76be9f7b7"
PATCHED_SHA256 = "bad25202ace2f99b086bfa664744a59b1c6bbae8cb8892ea67fdfae33947887c"

OLD = '''    if len(candidates) > 1:
        # The refusal below guards against one skill silently shadowing another. Copies of ONE
'''
NEW = '''    if len(candidates) > 1:
        # Project roots form one tier: preserve collisions across the entire tier.
        # Otherwise choose the first local/external root, retaining its collisions.
        if not any(_under_any(c[1], project_dirs) for c in candidates):
            for root in all_dirs:
                in_root = [c for c in candidates if _owning_search_dir(c[1], all_dirs) == root]
                if in_root:
                    candidates = in_root
                    break
    if len(candidates) > 1:
        # The refusal below guards against one skill silently shadowing another. Copies of ONE
'''


def patch_file(path):
    path = Path(path)
    data = path.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    if digest == PATCHED_SHA256:
        compile(data, str(path), "exec")
        return
    if digest != SOURCE_SHA256:
        raise SystemExit("Hermes skill resolver checksum mismatch; refusing to patch")
    text = data.decode("utf-8")
    if text.count(OLD) != 1:
        raise SystemExit("Hermes skill resolver source changed; refusing to patch")
    updated = text.replace(OLD, NEW, 1)
    if hashlib.sha256(updated.encode("utf-8")).hexdigest() != PATCHED_SHA256:
        raise SystemExit("Patched resolver checksum mismatch; refusing to write")
    compile(updated, str(path), "exec")
    path.write_bytes(updated.encode("utf-8"))


if __name__ == "__main__":
    patch_file(sys.argv[1])
