# tdarr deployment

GitOps deployment README for `kubernetes/apps/media/tdarr/app/helmrelease.yaml`.

## Summary
- Namespace: `media`
- HelmRelease: `tdarr`
- Path: `kubernetes/apps/media/tdarr/app`
- Kustomization: `kubernetes/apps/media/tdarr/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/media/tdarr/ks.yaml`
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `30m`
- Timeout: `not declared`

## Supporting manifests
- `configmap.yaml`
- `priorityclass.yaml`

## Controllers and images
- `tdarr`: type `Deployment`
  - container `tdarr` image `ghcr.io/haveagitgat/tdarr:2.58.02@sha256:20a5656c4af4854e1877046294f77113f949d27e35940a9a65f231423d063207`

## Services
- `app`: http:8265, server:8266

## Routes
- `app`: hosts `{{ .Release.Name }}.${SECRET_DOMAIN}`, gateways `envoy-internal`

## Persistence
- `config`: existingClaim=`tdarr`
- `transcode`: type=`nfs`, path=`/media/temp`
- `movies`: type=`nfs`, path=`/media/movies`
- `tv`: type=`nfs`, path=`/media/tv`
- `music`: type=`nfs`, path=`/media/music`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/media/tdarr/app >/tmp/tdarr-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media annotate helmrelease tdarr reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media get helmrelease tdarr -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media get pods -l app.kubernetes.io/instance=tdarr -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
