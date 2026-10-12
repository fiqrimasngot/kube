# steam deployment

GitOps deployment README for `kubernetes/apps/media/steam/app/helmrelease.yaml`.

## Summary
- Namespace: `media`
- HelmRelease: `steam`
- Path: `kubernetes/apps/media/steam/app`
- Kustomization: `kubernetes/apps/media/steam/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/media/steam/ks.yaml`
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `30m`
- Timeout: `not declared`

## Secret manifests
Secret manifest filenames only; do not put decrypted values in this README.
- `secret.sops.yaml`

## Supporting manifests
- `kustomizeconfig.yaml`

## Controllers and images
- `app`: type `Deployment`
  - container `steam` image `josh5/steam-headless:latest@sha256:59b509525951fc941979094493af63c1c8a73b23c069b30038108a833800d83b`

## Services
- `app`: http:8083, s-t1:47984, s-t2:47989, sunshine-ui:47990, s-t3:48010, s-u1:47998, s-u2:47999, s-u3:48000

## Routes
- `app`: hosts `steam.${SECRET_DOMAIN}`, gateways `envoy-internal`

## Persistence
- `home`: existingClaim=`steam`
- `games`: type=`nfs`, path=`/media/games`
- `dev-shm`: type=`emptyDir`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/media/steam/app >/tmp/steam-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media annotate helmrelease steam reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media get helmrelease steam -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media get pods -l app.kubernetes.io/instance=steam -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
