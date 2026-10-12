# smartctl-exporter deployment

GitOps deployment README for `kubernetes/apps/observability/smartctl-exporter/app/helmrelease.yaml`.

## Summary
- Namespace: `observability`
- HelmRelease: `smartctl-exporter`
- Path: `kubernetes/apps/observability/smartctl-exporter/app`
- Kustomization: `kubernetes/apps/observability/smartctl-exporter/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/observability/smartctl-exporter/ks.yaml`
- Chart: chartRef `OCIRepository/smartctl-exporter`
- Reconcile interval: `1h`
- Timeout: `not declared`

## Supporting manifests
- `prometheusrule.yaml`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/observability/smartctl-exporter/app >/tmp/smartctl-exporter-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n observability annotate helmrelease smartctl-exporter reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n observability get helmrelease smartctl-exporter -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n observability get pods -l app.kubernetes.io/instance=smartctl-exporter -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
