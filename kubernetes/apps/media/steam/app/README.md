# Steam

GitOps deployment notes for `steam` in the `media` namespace.

## Context
- Deployment path: `kubernetes/apps/media/steam/app`
- HelmRelease: `kubernetes/apps/media/steam/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/media/steam/app/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `30m`
- Timeout: `not specified`
- Controllers: `app`, `games`, `dev-shm`

## Runtime
- Images:
  - `josh5/steam-headless` (`latest@sha256:59b509525951fc941979094493af63c1c8a73b23c069b30038108a833800d83b`)
- Service declared: yes
- Route/ingress declared: yes
- Encrypted secret manifests: `secret.sops.yaml`

## Files
- `secret.sops.yaml`
- `helmrelease.yaml`
- `name: steam-init-scripts`
- `udevd.sh=resources/udevd.sh`
- `kustomizeconfig.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/media/steam/app
kubectl -n media get helmrelease steam
kubectl -n media get pods -l app.kubernetes.io/instance=steam
```

## Reconcile
```sh
flux -n media reconcile helmrelease steam
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
