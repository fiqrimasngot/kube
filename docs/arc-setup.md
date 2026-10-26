# GitHub Actions Runner Controller setup

Status: prerequisites prepared and verified; GitHub App credentials are stored only in the Kubernetes Secret below.

- Runner scope: organization-level (preferred default).
- GitHub organization: `fiqrim-dug` (inferred from the repository remote `fiqrim-dug/k8s`).
- Repository: `fiqrim-dug/k8s`.
- Kubernetes context: `topf@kubernetes`.
- Cluster API: `https://10.32.1.10:6443`.
- Controller namespace: `arc-systems` (created and verified).
- Runner namespace: `arc-runners` (created and verified).
- Secret name: `arc-runners/github-app-secret`.
- Required secret keys: `github_app_id`, `github_app_installation_id`, `github_app_private_key`.

- GitHub App ID: `5474031`.
- GitHub App installation ID: `175309995`.
- GitHub App permissions: organization self-hosted runners read/write (org-level ARC scope).
- Kubernetes Secret status: present as `Opaque`; values are not recorded here.

Do not commit private keys, generated Kubernetes Secret manifests containing values, or other secret material. Verify the secret without printing values with:

```sh
kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig get secret -n arc-runners github-app-secret
kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig get secret -n arc-runners github-app-secret -o go-template='{{range $k, $v := .data}}{{$k}}{{"\\n"}}{{end}}'
```

## Autoscaling runner scale set

The organization-level scale set is managed by Flux from:
`kubernetes/apps/arc-systems/gha-runner-scale-set/`.

- Release: `k8s-runners` in `arc-runners`.
- GitHub configuration: `https://github.com/fiqrim-dug`.
- Workflows select it with `runs-on: k8s-runners`.
- Capacity: zero idle runners, up to ten ephemeral runners.
- Runner requests/limits: 500m/1Gi and 2 CPU/4Gi.
- Container mode: `dind`, enabling Docker builds, service containers, and container actions.

DinD requires privileged runner pods. This is intentionally selected for arbitrary workflow compatibility; it increases the impact of a compromised workflow, so the runners must not receive cluster-admin permissions. The accompanying NetworkPolicy denies ingress to runner pods while leaving egress available for GitHub, registries, and workflow dependencies.
