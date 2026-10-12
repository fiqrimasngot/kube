# Jellyfin

GitOps deployment notes for `jellyfin` in the `media` namespace.

## Context
- Deployment path: `kubernetes/apps/media/jellyfin/app`
- HelmRelease: `kubernetes/apps/media/jellyfin/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/media/jellyfin/app/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `30m`
- Timeout: `not specified`
- Controllers: `jellyfin`, `movies`, `tv`, `music`, `tmp`, `dri`

## Runtime
- Images:
  - `registry.skysolutions.fi/docker.io/jellyfin/jellyfin` (`10.11.5`)
- Service declared: yes
- Route/ingress declared: yes

## Files
- `./helmrelease.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/media/jellyfin/app
kubectl -n media get helmrelease jellyfin
kubectl -n media get pods -l app.kubernetes.io/instance=jellyfin
```

## Reconcile
```sh
flux -n media reconcile helmrelease jellyfin
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
