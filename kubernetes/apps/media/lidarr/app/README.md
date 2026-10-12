# Lidarr

GitOps deployment notes for `lidarr` in the `media` namespace.

## Context
- Deployment path: `kubernetes/apps/media/lidarr/app`
- HelmRelease: `kubernetes/apps/media/lidarr/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/media/lidarr/app/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `15m`
- Timeout: `not specified`
- Controllers: `lidarr`, `downloads`, `tmp`, `music`

## Runtime
- Images:
  - `ghcr.io/home-operations/lidarr` (`3.1.3@sha256:b1e206e02bcacf1b540a813be74afb4f788114bbb540830478e5eb0e469c2162`)
- Service declared: yes
- Route/ingress declared: yes

## Files
- `./helmrelease.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/media/lidarr/app
kubectl -n media get helmrelease lidarr
kubectl -n media get pods -l app.kubernetes.io/instance=lidarr
```

## Reconcile
```sh
flux -n media reconcile helmrelease lidarr
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
