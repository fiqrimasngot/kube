# Check CLI discovery from a Hermes role

Run the preflight **in the assignee’s terminal, in the task repository**. A test in the parent pod does not tell you which client a worker will run. Use this checkout’s script even if the task is in the other repository:

```sh
python3 /opt/data/workspace/kube/scripts/hermes-cli-preflight.py
```

It locates `gh`, `kubectl`, `kustomize`, `helm` and `talosctl`, and runs client-only version commands. Each line gives the tool, result and selected executable. Exit 0 means all five ran. `missing` means PATH did not resolve the name; `failed(N)`, `timeout` or `not runnable` means it resolved but did not work. No login or cluster request is part of this check. Repeat it in **default**, **automationops**, **kubeimplementer**, **researcher** and **reviewer**; record the role and working directory with each result.

## Where the commands come from

1. Flux reads `fiqrimasngot/kube` main and builds `kubernetes/apps/devops/hermes/app`. `copy-config` copies the default and four named configs and profile metadata from the ConfigMap to the `hermes` PVC. Editing a live config is not a startup fix.
2. `install-tools` supplies shared clients and the kube/Talos working-directory wrappers under `/opt/data/.local/bin`. Existing installs on the PVC also include mise under `/opt/data/home`. A pre-existing `gh` launcher may use mise to run the repo’s version. These installs and profile-local wrappers are distinct from the pod image.
3. `stage-cli-path` recreates five links in a pod-local `emptyDir` on each start. It prefers the shared entry points, **not** `kubectl.real` or `talosctl.real`. When a shared `helm` or `kustomize` is absent, it links the existing `latest` install in the shared mise store. It does not install tools, activate repo config, run PVC code as root or write into anyone’s home. A missing target logs a warning rather than stopping the gateway. This is discovery on the same PVC, not provisioning mise on a blank volume.
4. The app mounts those links read-only. The pod PATH has them as a fallback. The image’s `/etc/profile` resets PATH for login shells; a mounted `/etc/profile.d` snippet appends the current worker’s local bin and then the fallback for uid 10000. Existing role wrappers and repo-activated tools can still win. No login, config store, service account or RBAC is added. Profiles share an OS user: PATH is not an authorization boundary.

## Verify access separately

- **GitHub:** use the role’s own session. Set `repo=fiqrimasngot/kube` (or the task’s actual `OWNER/REPO`). `gh api user --jq .login` identifies the login; `gh repo view "$repo" --json nameWithOwner,viewerPermission` tests this repository. For a PR use `gh pr view "$pr" -R "$repo" --json headRefOid,state,url` and `gh pr checks "$pr" -R "$repo"`. Match the expected full SHA and re-read the head after the checks. A login alone, or successful Git transport, does not prove checks are visible. No checks reported is not a pass.
- **Public evidence:** when anonymous reads are permitted, use `scripts/public_pr_receipt.py` from **that role’s existing `github` skill**: `python3 <skill-directory>/scripts/public_pr_receipt.py "$repo" "$pr" "$sha"`. Pass the expected 40-character head SHA. This GET-only receipt needs no login. A head change requires a new review. A rate limit, denial or incomplete response is not evidence that CI passed.
- **Protected or private evidence:** ask the designated authorized reader to retrieve the exact repo, PR, head SHA, check names, states/conclusions, URLs and observation time. Hand off those facts, not credentials. Label them _reader-provided_, not independently verified by the assignee. Never switch a global login, set a shared `GH_CONFIG_DIR`, or borrow another role’s token to make a check pass.
- **Cluster:** only the assigned reader should test live access. From `/opt/data/workspace/kube` or `/opt/data/workspace/kube-kl/k8s`, confirm the repo and expected cluster first. Use `kubectl --kubeconfig="$PWD/kubeconfig" get nodes -o name` and `talosctl --talosconfig="$PWD/talos/talosconfig" version --short` with the repository’s documented endpoint/node if needed. Compare the nodes/server with the intended target. From an isolated worktree, use the authorized canonical repo’s explicit config paths, not `$PWD` or a global override. Do not print configs. A denial, missing file, unreachable endpoint and wrong target are different results; do not widen access to fix discovery.

For a credential-free regression run, use Python with PyYAML from the repo root:

```sh
python3 -m unittest discover -s kubernetes/apps/devops/hermes/app/tests -p test_cli_discovery.py
```
