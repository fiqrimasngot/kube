# gha-runner-scale-set deployment

GitOps deployment README for `kubernetes/apps/devops/gha-runner-scale-set/app/helmrelease.yaml`.

## Summary
- Namespace: `devops`
- HelmRelease: `gha-runner-scale-set`
- Path: `kubernetes/apps/devops/gha-runner-scale-set/app`
- Kustomization: `kubernetes/apps/devops/gha-runner-scale-set/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/devops/gha-runner-scale-set/ks.yaml`
- Chart: chart `gha-runner-scale-set` from `HelmRepository/actions-runner-controller` version `0.13.0`
- Reconcile interval: `30m`
- Timeout: `not declared`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/devops/gha-runner-scale-set/app >/tmp/gha-runner-scale-set-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n devops annotate helmrelease gha-runner-scale-set reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n devops get helmrelease gha-runner-scale-set -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n devops get pods -l app.kubernetes.io/instance=gha-runner-scale-set -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
