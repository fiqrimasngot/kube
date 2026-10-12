# dcgm-exporter deployment

GitOps deployment README for `kubernetes/apps/observability/dcgm-exporter/app/helmrelease.yaml`.

## Summary
- Namespace: `observability`
- HelmRelease: `dcgm-exporter`
- Path: `kubernetes/apps/observability/dcgm-exporter/app`
- Kustomization: `kubernetes/apps/observability/dcgm-exporter/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/observability/dcgm-exporter/ks.yaml`
- Chart: chart `dcgm-exporter` from `HelmRepository/dcgm-exporter` version `4.7.1`
- Reconcile interval: `15m`
- Timeout: `not declared`

## Supporting manifests
- `alerts.yaml`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/observability/dcgm-exporter/app >/tmp/dcgm-exporter-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n observability annotate helmrelease dcgm-exporter reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n observability get helmrelease dcgm-exporter -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n observability get pods -l app.kubernetes.io/instance=dcgm-exporter -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
