# bazarr deployment

GitOps deployment README for `kubernetes/apps/media/bazarr/app/helmrelease.yaml`.

## Summary
- Namespace: `media`
- HelmRelease: `bazarr`
- Path: `kubernetes/apps/media/bazarr/app`
- Kustomization: `kubernetes/apps/media/bazarr/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/media/bazarr/ks.yaml`
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `30m`
- Timeout: `not declared`

## Controllers and images
- `bazarr`: type `Deployment`
  - container `app` image `ghcr.io/home-operations/bazarr:1.6.0@sha256:cd63bbd0986c93e238eb8b9442604d249f0d4080099b389f822abe2062044417`

## Services
- `app`: http:6767

## Routes
- `app`: hosts `{{ .Release.Name }}.${SECRET_DOMAIN}`, gateways `envoy-internal`

## Persistence
- `config`: existingClaim=`bazarr`
- `tmp`: type=`emptyDir`
- `movies`: type=`nfs`, path=`/media/movies`
- `tv`: type=`nfs`, path=`/media/tv`
- `music`: type=`nfs`, path=`/media/music`
- `downloads`: type=`nfs`, path=`/media/downloads`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/media/bazarr/app >/tmp/bazarr-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media annotate helmrelease bazarr reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media get helmrelease bazarr -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media get pods -l app.kubernetes.io/instance=bazarr -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
