# Actual

GitOps deployment notes for `actual` in the `default` namespace.

## Context
- Deployment path: `kubernetes/apps/default/actual/app`
- HelmRelease: `kubernetes/apps/default/actual/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/default/actual/app/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `30m`
- Timeout: `not specified`
- Controllers: `main`

## Runtime
- Images:
  - `ghcr.io/actualbudget/actual-server` (`26.9.0`)
- Service declared: yes
- Route/ingress declared: yes

## Files
- `./helmrelease.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/default/actual/app
kubectl -n default get helmrelease actual
kubectl -n default get pods -l app.kubernetes.io/instance=actual
```

## Reconcile
```sh
flux -n default reconcile helmrelease actual
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
