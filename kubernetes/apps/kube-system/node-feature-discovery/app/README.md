# node-feature-discovery deployment

GitOps deployment README for `kubernetes/apps/kube-system/node-feature-discovery/app/helmrelease.yaml`.

## Summary
- Namespace: `kube-system`
- HelmRelease: `node-feature-discovery`
- Path: `kubernetes/apps/kube-system/node-feature-discovery/app`
- Kustomization: `kubernetes/apps/kube-system/node-feature-discovery/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/kube-system/node-feature-discovery/ks.yaml`
- Chart: chart `node-feature-discovery` from `HelmRepository/node-feature-discovery` version `0.18.3`
- Reconcile interval: `15m`
- Timeout: `not declared`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/kube-system/node-feature-discovery/app >/tmp/node-feature-discovery-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n kube-system annotate helmrelease node-feature-discovery reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n kube-system get helmrelease node-feature-discovery -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n kube-system get pods -l app.kubernetes.io/instance=node-feature-discovery -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
