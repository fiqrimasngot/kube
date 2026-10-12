# Prowlarr

GitOps deployment notes for `prowlarr` in the `media` namespace.

## Context
- Deployment path: `kubernetes/apps/media/prowlarr/app`
- HelmRelease: `kubernetes/apps/media/prowlarr/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/media/prowlarr/app/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `30m`
- Timeout: `not specified`
- Controllers: `prowlarr`, `tmp`

## Runtime
- Images:
  - `ghcr.io/home-operations/prowlarr` (`2.4.0.5397@sha256:8a140c9104c754a272f5e0d1dfcb32a06f07946a431a45c1083a16344f531748`)
- Service declared: yes
- Route/ingress declared: yes

## Files
- `./helmrelease.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/media/prowlarr/app
kubectl -n media get helmrelease prowlarr
kubectl -n media get pods -l app.kubernetes.io/instance=prowlarr
```

## Reconcile
```sh
flux -n media reconcile helmrelease prowlarr
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
