# metrics-server deployment

GitOps deployment README for `kubernetes/apps/kube-system/metrics-server/app/helmrelease.yaml`.

## Summary
- Namespace: `kube-system`
- HelmRelease: `metrics-server`
- Path: `kubernetes/apps/kube-system/metrics-server/app`
- Kustomization: `kubernetes/apps/kube-system/metrics-server/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/kube-system/metrics-server/ks.yaml`
- Chart: chartRef `OCIRepository/metrics-server`
- Reconcile interval: `1h`
- Timeout: `not declared`

## Supporting manifests
- `ocirepository.yaml`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/kube-system/metrics-server/app >/tmp/metrics-server-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n kube-system annotate helmrelease metrics-server reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n kube-system get helmrelease metrics-server -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n kube-system get pods -l app.kubernetes.io/instance=metrics-server -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
