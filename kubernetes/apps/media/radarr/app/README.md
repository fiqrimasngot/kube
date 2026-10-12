# Radarr

GitOps deployment notes for `radarr` in the `media` namespace.

## Context
- Deployment path: `kubernetes/apps/media/radarr/app`
- HelmRelease: `kubernetes/apps/media/radarr/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/media/radarr/app/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `30m`
- Timeout: `not specified`
- Controllers: `radarr`, `tmp`, `movies`, `downloads`

## Runtime
- Images:
  - `ghcr.io/home-operations/radarr` (`6.2.1.10461@sha256:0756fffa75b30219e3dbac8d027a5389f53cbb34ae83fa4b0976c1b0524c8eb1`)
- Service declared: yes
- Route/ingress declared: yes

## Files
- `./helmrelease.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/media/radarr/app
kubectl -n media get helmrelease radarr
kubectl -n media get pods -l app.kubernetes.io/instance=radarr
```

## Reconcile
```sh
flux -n media reconcile helmrelease radarr
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
