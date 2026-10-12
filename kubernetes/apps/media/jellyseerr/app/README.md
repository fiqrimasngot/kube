# Jellyseerr

GitOps deployment notes for `jellyseerr` in the `media` namespace.

## Context
- Deployment path: `kubernetes/apps/media/jellyseerr/app`
- HelmRelease: `kubernetes/apps/media/jellyseerr/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/media/jellyseerr/app/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `30m`
- Timeout: `not specified`
- Controllers: `jellyseerr`, `tmpfs`

## Runtime
- Images:
  - `fallenbagel/jellyseerr` (`2.7.3`)
- Service declared: yes
- Route/ingress declared: yes

## Files
- `./helmrelease.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/media/jellyseerr/app
kubectl -n media get helmrelease jellyseerr
kubectl -n media get pods -l app.kubernetes.io/instance=jellyseerr
```

## Reconcile
```sh
flux -n media reconcile helmrelease jellyseerr
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
