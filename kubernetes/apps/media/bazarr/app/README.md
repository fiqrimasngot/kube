# Bazarr

GitOps deployment notes for `bazarr` in the `media` namespace.

## Context
- Deployment path: `kubernetes/apps/media/bazarr/app`
- HelmRelease: `kubernetes/apps/media/bazarr/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/media/bazarr/app/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `30m`
- Timeout: `not specified`
- Controllers: `bazarr`, `app`, `tmp`, `movies`, `tv`, `music`, `downloads`

## Runtime
- Images:
  - `ghcr.io/home-operations/bazarr` (`1.6.0@sha256:cd63bbd0986c93e238eb8b9442604d249f0d4080099b389f822abe2062044417`)
- Service declared: yes
- Route/ingress declared: yes

## Files
- `./helmrelease.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/media/bazarr/app
kubectl -n media get helmrelease bazarr
kubectl -n media get pods -l app.kubernetes.io/instance=bazarr
```

## Reconcile
```sh
flux -n media reconcile helmrelease bazarr
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
