# immich-server deployment

GitOps deployment README for `kubernetes/apps/media/immich/app/server/helmrelease.yaml`.

## Summary
- Namespace: `media`
- HelmRelease: `immich-server`
- Path: `kubernetes/apps/media/immich/app/server`
- Kustomization: `kubernetes/apps/media/immich/app/server/kustomization.yaml`
- Flux app Kustomization: not found at app root
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `15m`
- Timeout: `not declared`

## Controllers and images
- `main`: type `Deployment`, replicas `1`
  - container `immich-server` image `ghcr.io/immich-app/immich-server:v2.7.5`

## Services
- `immich-server`: http:2283

## Routes
- `immich-server`: hosts `photos.${SECRET_DOMAIN}`, gateways `envoy-external`

## Persistence
- `library`: type=`nfs`, path=`/immich`
- `external`: type=`nfs`, path=`/immich`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/media/immich/app/server >/tmp/immich-server-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media annotate helmrelease immich-server reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media get helmrelease immich-server -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media get pods -l app.kubernetes.io/instance=immich-server -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
