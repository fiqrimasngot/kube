# tdarr-node deployment

GitOps deployment README for `kubernetes/apps/media/tdarr/node/helmrelease.yaml`.

## Summary
- Namespace: `media`
- HelmRelease: `tdarr-node`
- Path: `kubernetes/apps/media/tdarr/node`
- Kustomization: `kubernetes/apps/media/tdarr/node/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/media/tdarr/ks.yaml`
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `30m`
- Timeout: `not declared`

## Supporting manifests
- `hpa.yaml`

## Controllers and images
- `tdarr-node`: type `Deployment`
  - container `app` image `ghcr.io/haveagitgat/tdarr_node:2.58.02@sha256:62e14509bc19dea9b6f5dc85d0942163b6fa240d780a53eb590d894d46c9e1f2`

## Services
- `app`: server:8266

## Persistence
- `movies`: type=`nfs`, path=`/media/movies`
- `tv`: type=`nfs`, path=`/media/tv`
- `music`: type=`nfs`, path=`/media/music`
- `transcode`: type=`nfs`, path=`/media/temp`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/media/tdarr/node >/tmp/tdarr-node-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media annotate helmrelease tdarr-node reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media get helmrelease tdarr-node -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media get pods -l app.kubernetes.io/instance=tdarr-node -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
