"""Exercise the release's discovery init in scratch, without a PVC or credentials."""
import platform
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import yaml

APP = Path(__file__).resolve().parents[1]
ROOT = APP.parents[4]
PREFLIGHT = ROOT / "scripts/hermes-cli-preflight.py"
TOOLS = ("gh", "kubectl", "kustomize", "helm", "talosctl")
PROFILES = ("default", "automationops", "kubeimplementer", "researcher", "reviewer")


def values(path):
    return yaml.safe_load(path.read_text())["spec"]["values"]


class DiscoveryTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.data = self.root / "data"
        self.stage = self.root / "cli"
        self.stage.mkdir()
        self.init = values(APP / "helmrelease.yaml")["controllers"]["hermes"]["initContainers"]

    def executable(self, path, body):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("#!/bin/sh\n" + body + "\n")
        path.chmod(0o755)

    def stage_links(self):
        # Execute the actual init command. Redirect only the two mount points.
        shell, flag, script = self.init["stage-cli-path"]["command"]
        script = script.replace("/opt/data", str(self.data)).replace("/run/hermes-cli", str(self.stage))
        return subprocess.run([shell, flag, script], env={"PATH": "/usr/bin:/bin"},
                              check=True, capture_output=True, text=True)

    def fixture(self):
        arch = {"x86_64": "amd64", "aarch64": "arm64"}[platform.machine()]
        for tool in ("gh", "kubectl", "talosctl"):
            self.executable(self.data / ".local/bin" / tool, "exit 0")
        installs = self.data / "home/.local/share/mise/installs"
        self.executable(installs / f"helm/latest/linux-{arch}/helm", "exit 0")
        self.executable(installs / "kustomize/latest/kustomize", "exit 0")

    def probe(self, home, uid="10000"):
        # Simulate the image uid even in root-run CI. No operator env or tools.
        system = self.root / "sysbin"
        self.executable(system / "id", f"printf '%s\\n' {uid}")
        return subprocess.run(["/bin/sh", "-ec", '. "$1"; . "$1"; exec "$2" "$3"',
                               "probe", self.stage / "path.sh", sys.executable, PREFLIGHT],
                              env={"HOME": str(home), "PATH": str(system)}, cwd=home,
                              capture_output=True, text=True)

    def test_fresh_homes(self):
        self.fixture()
        self.stage_links()
        self.assertEqual(set(p.name for p in (self.stage / "bin").iterdir()), set(TOOLS))
        for profile in PROFILES:
            with self.subTest(profile=profile):
                home = self.root / profile / "home"
                home.mkdir(parents=True)
                result = self.probe(home)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                for tool in TOOLS:
                    self.assertIn(f"{tool}: ok {self.stage}/bin/{tool}", result.stdout)
                self.assertEqual(list(home.iterdir()), [])

    def test_keep_wrapper_across_repeated_init(self):
        self.fixture()
        home = self.root / "reviewer/home"
        local = home / ".local/bin/gh"
        self.executable(local, 'test "$1" = --version')
        before = local.read_bytes()
        self.stage_links()
        self.stage_links()
        result = self.probe(home)
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn(f"gh: ok {local}", result.stdout)
        self.assertEqual(local.read_bytes(), before)

    def test_missing_and_broken_clients_report_separate_failures(self):
        self.fixture()
        (self.data / ".local/bin/kubectl").unlink()
        self.executable(self.data / ".local/bin/gh", 'echo do-not-log >&2; exit 23')
        staged = self.stage_links()
        self.assertIn("CLI fallback unavailable: kubectl", staged.stderr)
        result = self.probe(self.root)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("kubectl: missing", result.stdout)
        self.assertIn("gh: failed(23)", result.stdout)
        self.assertNotIn("do-not-log", result.stdout + result.stderr)
        self.assertIn("talosctl: ok", result.stdout)

    def test_cluster_wrappers_keep_cwd_selection_and_explicit_overrides(self):
        self.fixture()
        self.stage_links()
        script = self.init["install-tools"]["command"][-1].replace("$$", "$")
        for tool, selector, relative in (("kubectl", "KUBECONFIG", "kubeconfig"),
                                         ("talosctl", "TALOSCONFIG", "talos/talosconfig")):
            marker = f"cat > /opt/data/.local/bin/{tool} <<'EOF'\n"
            wrapper = script.split(marker, 1)[1].split("\nEOF", 1)[0]
            shared = self.data / ".local/bin"
            (shared / tool).write_text(wrapper.replace("/opt/data", str(self.data)) + "\n")
            self.executable(shared / (tool + ".real"), f'test "${selector}" = "$EXPECTED"')
            for repo in ("kube", "kube-kl/k8s"):
                work = self.data / "workspace" / repo
                sub = work / "sub"
                sub.mkdir(parents=True, exist_ok=True)
                for override in (None, "explicit"):
                    with self.subTest(tool=tool, repo=repo, override=override):
                        env = {"EXPECTED": override or str(work / relative)}
                        if override:
                            env[selector] = override
                        subprocess.run([self.stage / "bin" / tool], cwd=sub, env=env, check=True)

    def test_root_login_does_not_add_worker_tools(self):
        self.fixture()
        self.stage_links()
        result = self.probe(self.root, uid="0")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout.count(": missing"), len(TOOLS))

    def test_template_preserves_canonical_tool_bootstrap_and_mounts(self):
        release = values(APP / "helmrelease.yaml")
        template = values(ROOT / "template/config" / APP.relative_to(ROOT) / "helmrelease.yaml.j2")
        for v in (release, template):
            controller = v["controllers"]["hermes"]
            self.assertNotIn("kubectl-tools", controller["initContainers"])
            self.assertTrue(controller["containers"]["app"]["env"]["PATH"].endswith(":/run/hermes-cli/bin"))
        for name in ("install-tools", "stage-cli-path"):
            self.assertEqual(self.init[name], template["controllers"]["hermes"]["initContainers"][name])
        self.assertEqual(release["persistence"]["cli-path"], template["persistence"]["cli-path"])
