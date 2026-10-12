# blackbox-exporter deployment

GitOps deployment README for `kubernetes/apps/observability/blackbox-exporter/app/helmrelease.yaml`.

## Summary
- Namespace: `observability`
- HelmRelease: `blackbox-exporter`
- Path: `kubernetes/apps/observability/blackbox-exporter/app`
- Kustomization: `kubernetes/apps/observability/blackbox-exporter/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/observability/blackbox-exporter/ks.yaml`
- Chart: chart `prometheus-blackbox-exporter` from `HelmRepository/prometheus-community` version `11.6.1`
- Reconcile interval: `30m`
- Timeout: `not declared`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/observability/blackbox-exporter/app >/tmp/blackbox-exporter-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n observability annotate helmrelease blackbox-exporter reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n observability get helmrelease blackbox-exporter -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n observability get pods -l app.kubernetes.io/instance=blackbox-exporter -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
