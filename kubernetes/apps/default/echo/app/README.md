# echo deployment

GitOps deployment README for `kubernetes/apps/default/echo/app/helmrelease.yaml`.

## Summary
- Namespace: `default`
- HelmRelease: `echo`
- Path: `kubernetes/apps/default/echo/app`
- Kustomization: `kubernetes/apps/default/echo/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/default/echo/ks.yaml`
- Chart: chartRef `OCIRepository/echo`
- Reconcile interval: `1h`
- Timeout: `not declared`

## Supporting manifests
- `ocirepository.yaml`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/default/echo/app >/tmp/echo-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default annotate helmrelease echo reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default get helmrelease echo -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default get pods -l app.kubernetes.io/instance=echo -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
