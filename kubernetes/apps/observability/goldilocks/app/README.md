# goldilocks deployment

GitOps deployment README for `kubernetes/apps/observability/goldilocks/app/helmrelease.yaml`.

## Summary
- Namespace: `observability`
- HelmRelease: `goldilocks`
- Path: `kubernetes/apps/observability/goldilocks/app`
- Kustomization: `kubernetes/apps/observability/goldilocks/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/observability/goldilocks/ks.yaml`
- Chart: chart `goldilocks` from `HelmRepository/fairwinds-charts` version `10.2.0`
- Reconcile interval: `30m`
- Timeout: `not declared`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/observability/goldilocks/app >/tmp/goldilocks-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n observability annotate helmrelease goldilocks reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n observability get helmrelease goldilocks -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n observability get pods -l app.kubernetes.io/instance=goldilocks -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
