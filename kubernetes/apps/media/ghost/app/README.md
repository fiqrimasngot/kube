# Ghost

GitOps deployment notes for `ghost` in the `media` namespace.

## Context
- Deployment path: `kubernetes/apps/media/ghost/app`
- HelmRelease: `kubernetes/apps/media/ghost/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/media/ghost/app/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `5m`
- Timeout: `15m`
- Controllers: `ghost`

## Runtime
- Images:
  - `docker.io/library/ghost` (`6.10.3`)
- Service declared: yes
- Route/ingress declared: yes

## Files
- `./helmrelease.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/media/ghost/app
kubectl -n media get helmrelease ghost
kubectl -n media get pods -l app.kubernetes.io/instance=ghost
```

## Reconcile
```sh
flux -n media reconcile helmrelease ghost
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
