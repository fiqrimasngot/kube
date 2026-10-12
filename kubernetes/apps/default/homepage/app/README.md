# homepage deployment

GitOps deployment README for `kubernetes/apps/default/homepage/app/helmrelease.yaml`.

## Summary
- Namespace: `default`
- HelmRelease: `homepage`
- Path: `kubernetes/apps/default/homepage/app`
- Kustomization: `kubernetes/apps/default/homepage/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/default/homepage/ks.yaml`
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `30m`
- Timeout: `not declared`

## Controllers and images
- `homepage`: type `Deployment`, replicas `1`
  - container `app` image `ghcr.io/gethomepage/homepage:v1.8.0@sha256:7dc099d5c6ec7fc945d858218565925b01ff8a60bcbfda990fc680a8b5cd0b6e`

## Services
- `app`: http:3000

## Routes
- `app`: hosts `dash.${SECRET_DOMAIN}`, gateways `envoy-internal`

## Persistence
- `config`: type=`configMap`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/default/homepage/app >/tmp/homepage-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default annotate helmrelease homepage reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default get helmrelease homepage -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default get pods -l app.kubernetes.io/instance=homepage -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
