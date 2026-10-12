# i2pd deployment

GitOps deployment README for `kubernetes/apps/media/i2pd/app/helmrelease.yaml`.

## Summary
- Namespace: `media`
- HelmRelease: `i2pd`
- Path: `kubernetes/apps/media/i2pd/app`
- Kustomization: `kubernetes/apps/media/i2pd/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/media/i2pd/ks.yaml`
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `30m`
- Timeout: `not declared`

## Controllers and images
- `i2pd`: type `Deployment`
  - container `app` image `registry.skysolutions.fi/docker.io/purplei2p/i2pd:release-2.50.0`

## Services
- `app`: http:7070, httpproxy:4444, socksproxy:4447

## Routes
- `app`: hosts `{{ .Release.Name }}.${SECRET_DOMAIN}`, gateways `envoy-internal`

## Persistence
- `home`: enabled=`True`, type=`emptyDir`
- `configfile`: enabled=`True`, type=`configMap`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/media/i2pd/app >/tmp/i2pd-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media annotate helmrelease i2pd reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media get helmrelease i2pd -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media get pods -l app.kubernetes.io/instance=i2pd -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
