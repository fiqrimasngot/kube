# uptime-kuma deployment

GitOps deployment README for `kubernetes/apps/observability/uptime-kuma/app/helmrelease.yaml`.

## Summary
- Namespace: `observability`
- HelmRelease: `uptime-kuma`
- Path: `kubernetes/apps/observability/uptime-kuma/app`
- Kustomization: `kubernetes/apps/observability/uptime-kuma/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/observability/uptime-kuma/ks.yaml`
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `15m`
- Timeout: `not declared`

## Controllers and images
- `main`: type `Deployment`
  - container `main` image `louislam/uptime-kuma:2.0.2`

## Services
- `main`: http:3001

## Routes
- `main`: hosts `uptime.${SECRET_DOMAIN}`, gateways `envoy-external`

## Persistence
- `data`: enabled=`True`, existingClaim=`uptime-kuma`, storageClass=`ceph-block`, size=`10Gi`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/observability/uptime-kuma/app >/tmp/uptime-kuma-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n observability annotate helmrelease uptime-kuma reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n observability get helmrelease uptime-kuma -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n observability get pods -l app.kubernetes.io/instance=uptime-kuma -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
