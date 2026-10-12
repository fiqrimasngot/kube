# Sonarr

GitOps deployment notes for `sonarr` in the `media` namespace.

## Context
- Deployment path: `kubernetes/apps/media/sonarr/app`
- HelmRelease: `kubernetes/apps/media/sonarr/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/media/sonarr/app/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `30m`
- Timeout: `15m`
- Controllers: `sonarr`, `tmp`, `tv`, `downloads`

## Runtime
- Images:
  - `ghcr.io/home-operations/sonarr` (`4.0.17.2969@sha256:6806001ccc2ec95d941c9c0de012dbcb59c6a33932cfc17f71e300bdd48cabfe`)
- Service declared: yes
- Route/ingress declared: yes

## Files
- `./helmrelease.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/media/sonarr/app
kubectl -n media get helmrelease sonarr
kubectl -n media get pods -l app.kubernetes.io/instance=sonarr
```

## Reconcile
```sh
flux -n media reconcile helmrelease sonarr
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
