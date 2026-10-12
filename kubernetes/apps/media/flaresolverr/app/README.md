# Flaresolverr

GitOps deployment notes for `flaresolverr` in the `media` namespace.

## Context
- Deployment path: `kubernetes/apps/media/flaresolverr/app`
- HelmRelease: `kubernetes/apps/media/flaresolverr/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/media/flaresolverr/app/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `30m`
- Timeout: `not specified`
- Controllers: `flaresolverr`

## Runtime
- Images:
  - `ghcr.io/flaresolverr/flaresolverr` (`v3.4.6@sha256:7962759d99d7e125e108e0f5e7f3cdbcd36161776d058d1d9b7153b92ef1af9e`)
- Service declared: yes
- Route/ingress declared: not declared in helmrelease.yaml

## Files
- `./helmrelease.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/media/flaresolverr/app
kubectl -n media get helmrelease flaresolverr
kubectl -n media get pods -l app.kubernetes.io/instance=flaresolverr
```

## Reconcile
```sh
flux -n media reconcile helmrelease flaresolverr
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
