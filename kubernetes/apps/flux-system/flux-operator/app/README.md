# flux-operator deployment

GitOps deployment README for `kubernetes/apps/flux-system/flux-operator/app/helmrelease.yaml`.

## Summary
- Namespace: `flux-system`
- HelmRelease: `flux-operator`
- Path: `kubernetes/apps/flux-system/flux-operator/app`
- Kustomization: `kubernetes/apps/flux-system/flux-operator/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/flux-system/flux-operator/ks.yaml`
- Chart: chartRef `OCIRepository/flux-operator`
- Reconcile interval: `1h`
- Timeout: `not declared`

## Supporting manifests
- `ocirepository.yaml`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/flux-system/flux-operator/app >/tmp/flux-operator-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n flux-system annotate helmrelease flux-operator reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n flux-system get helmrelease flux-operator -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n flux-system get pods -l app.kubernetes.io/instance=flux-operator -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
