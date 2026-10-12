# radarr deployment

GitOps deployment README for `kubernetes/apps/media/radarr/app/helmrelease.yaml`.

## Summary
- Namespace: `media`
- HelmRelease: `radarr`
- Path: `kubernetes/apps/media/radarr/app`
- Kustomization: `kubernetes/apps/media/radarr/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/media/radarr/ks.yaml`
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `30m`
- Timeout: `not declared`

## Controllers and images
- `radarr`: type `Deployment`
  - container `app` image `ghcr.io/home-operations/radarr:6.2.1.10461@sha256:0756fffa75b30219e3dbac8d027a5389f53cbb34ae83fa4b0976c1b0524c8eb1`

## Services
- `app`: http:80

## Routes
- `app`: hosts `{{ .Release.Name }}.${SECRET_DOMAIN}`, gateways `envoy-internal`

## Persistence
- `config`: existingClaim=`radarr`
- `tmp`: type=`emptyDir`
- `movies`: type=`nfs`, path=`/media/movies`
- `downloads`: type=`nfs`, path=`/media/downloads`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/media/radarr/app >/tmp/radarr-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media annotate helmrelease radarr reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media get helmrelease radarr -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media get pods -l app.kubernetes.io/instance=radarr -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
