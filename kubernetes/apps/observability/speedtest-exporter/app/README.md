# speedtest-exporter deployment

GitOps deployment README for `kubernetes/apps/observability/speedtest-exporter/app/helmrelease.yaml`.

## Summary
- Namespace: `observability`
- HelmRelease: `speedtest-exporter`
- Path: `kubernetes/apps/observability/speedtest-exporter/app`
- Kustomization: `kubernetes/apps/observability/speedtest-exporter/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/observability/speedtest-exporter/ks.yaml`
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `30m`
- Timeout: `not declared`

## Supporting manifests
- `prometheusrule.yaml`

## Controllers and images
- `main`: type `Deployment`
  - container `main` image `ghcr.io/miguelndecarvalho/speedtest-exporter:v3.5.4`

## Services
- `main`: http:9798

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/observability/speedtest-exporter/app >/tmp/speedtest-exporter-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n observability annotate helmrelease speedtest-exporter reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n observability get helmrelease speedtest-exporter -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n observability get pods -l app.kubernetes.io/instance=speedtest-exporter -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
