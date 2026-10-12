# jellyfin deployment

GitOps deployment README for `kubernetes/apps/media/jellyfin/app/helmrelease.yaml`.

## Summary
- Namespace: `media`
- HelmRelease: `jellyfin`
- Path: `kubernetes/apps/media/jellyfin/app`
- Kustomization: `kubernetes/apps/media/jellyfin/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/media/jellyfin/ks.yaml`
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `30m`
- Timeout: `not declared`

## Controllers and images
- `jellyfin`: type `statefulset`
  - container `app` image `registry.skysolutions.fi/docker.io/jellyfin/jellyfin:10.11.5`

## Services
- `jellyfin`: http:8096

## Routes
- `jellyfin`: hosts `jelly.${SECRET_DOMAIN}`, gateways `envoy-external`

## Persistence
- `config`: existingClaim=`${APP}`
- `movies`: type=`nfs`, path=`/media/movies`
- `tv`: type=`nfs`, path=`/media/tv`
- `music`: type=`nfs`, path=`/media/music`
- `tmp`: type=`emptyDir`
- `dri`: type=`hostPath`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/media/jellyfin/app >/tmp/jellyfin-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media annotate helmrelease jellyfin reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media get helmrelease jellyfin -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media get pods -l app.kubernetes.io/instance=jellyfin -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
