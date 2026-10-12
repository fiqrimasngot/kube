# Sabnzbd

GitOps deployment notes for `sabnzbd` in the `media` namespace.

## Context
- Deployment path: `kubernetes/apps/media/sabnzbd/app`
- HelmRelease: `kubernetes/apps/media/sabnzbd/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/media/sabnzbd/app/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `30m`
- Timeout: `15m`
- Controllers: `sabnzbd`, `downloads`, `logs`, `tmp`

## Runtime
- Images:
  - `ghcr.io/home-operations/sabnzbd` (`5.0.4@sha256:0c78c4752607d6d3fca43817af3540dad515c48dbab2c980ef7ef5bc27849b2b`)
- Service declared: yes
- Route/ingress declared: yes

## Files
- `./helmrelease.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/media/sabnzbd/app
kubectl -n media get helmrelease sabnzbd
kubectl -n media get pods -l app.kubernetes.io/instance=sabnzbd
```

## Reconcile
```sh
flux -n media reconcile helmrelease sabnzbd
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
