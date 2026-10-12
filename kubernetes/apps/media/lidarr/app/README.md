# lidarr deployment

GitOps deployment README for `kubernetes/apps/media/lidarr/app/helmrelease.yaml`.

## Summary
- Namespace: `media`
- HelmRelease: `lidarr`
- Path: `kubernetes/apps/media/lidarr/app`
- Kustomization: `kubernetes/apps/media/lidarr/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/media/lidarr/ks.yaml`
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `15m`
- Timeout: `not declared`

## Controllers and images
- `lidarr`: type `Deployment`
  - container `app` image `ghcr.io/home-operations/lidarr:3.1.3@sha256:b1e206e02bcacf1b540a813be74afb4f788114bbb540830478e5eb0e469c2162`

## Services
- `app`: http:8686

## Routes
- `app`: hosts `{{ .Release.Name }}.${SECRET_DOMAIN}`, gateways `envoy-internal`

## Persistence
- `downloads`: type=`nfs`, path=`/media/downloads`
- `config`: enabled=`True`, existingClaim=`lidarr`
- `tmp`: type=`emptyDir`
- `music`: type=`nfs`, path=`/media/music`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/media/lidarr/app >/tmp/lidarr-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media annotate helmrelease lidarr reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media get helmrelease lidarr -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media get pods -l app.kubernetes.io/instance=lidarr -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
