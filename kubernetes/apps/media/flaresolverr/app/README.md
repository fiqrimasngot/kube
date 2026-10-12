# flaresolverr deployment

GitOps deployment README for `kubernetes/apps/media/flaresolverr/app/helmrelease.yaml`.

## Summary
- Namespace: `media`
- HelmRelease: `flaresolverr`
- Path: `kubernetes/apps/media/flaresolverr/app`
- Kustomization: `kubernetes/apps/media/flaresolverr/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/media/flaresolverr/ks.yaml`
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `30m`
- Timeout: `not declared`

## Controllers and images
- `flaresolverr`: type `Deployment`
  - container `app` image `ghcr.io/flaresolverr/flaresolverr:v3.4.6@sha256:7962759d99d7e125e108e0f5e7f3cdbcd36161776d058d1d9b7153b92ef1af9e`

## Services
- `app`: http:8191

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/media/flaresolverr/app >/tmp/flaresolverr-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media annotate helmrelease flaresolverr reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media get helmrelease flaresolverr -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media get pods -l app.kubernetes.io/instance=flaresolverr -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
