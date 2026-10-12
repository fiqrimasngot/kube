# ghost deployment

GitOps deployment README for `kubernetes/apps/media/ghost/app/helmrelease.yaml`.

## Summary
- Namespace: `media`
- HelmRelease: `ghost`
- Path: `kubernetes/apps/media/ghost/app`
- Kustomization: `kubernetes/apps/media/ghost/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/media/ghost/ks.yaml`
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `5m`
- Timeout: `15m`

## Controllers and images
- `ghost`: type `deployment`, replicas `1`
  - container `app` image `docker.io/library/ghost:6.10.3`

## Services
- `app`: http:2368

## Routes
- `app`: hosts `${SECRET_DOMAIN}`, gateways `envoy-external`

## Persistence
- `content`: existingClaim=`ghost`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/media/ghost/app >/tmp/ghost-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media annotate helmrelease ghost reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media get helmrelease ghost -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media get pods -l app.kubernetes.io/instance=ghost -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
