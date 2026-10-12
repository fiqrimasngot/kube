# Immich — Server

GitOps deployment notes for `immich-server` in the `media` namespace.

## Context
- Deployment path: `kubernetes/apps/media/immich/app/server`
- HelmRelease: `kubernetes/apps/media/immich/app/server/helmrelease.yaml`
- Kustomization: `kubernetes/apps/media/immich/app/server/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `15m`
- Timeout: `not specified`
- Controllers: `immich-server`, `library`, `external`

## Runtime
- Images:
  - `ghcr.io/onedr0p/postgres-init` (`17.4`)
  - `ghcr.io/immich-app/immich-server` (`v2.7.5`)
- Service declared: yes
- Route/ingress declared: yes

## Files
- `./helmrelease.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/media/immich/app/server
kubectl -n media get helmrelease immich-server
kubectl -n media get pods -l app.kubernetes.io/instance=immich-server
```

## Reconcile
```sh
flux -n media reconcile helmrelease immich-server
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
