# Goldilocks

GitOps deployment notes for `fairwinds-charts` in the `observability` namespace.

## Context
- Deployment path: `kubernetes/apps/observability/goldilocks/app`
- HelmRelease: `kubernetes/apps/observability/goldilocks/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/observability/goldilocks/app/kustomization.yaml`
- Chart/reference: `spec:`
- Reconcile interval: `15m`
- Timeout: `3m`

## Runtime
- Images: managed by the referenced chart or not pinned in this file.
- Service declared: not declared in helmrelease.yaml
- Route/ingress declared: yes

## Files
- `./helmrelease.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/observability/goldilocks/app
kubectl -n observability get helmrelease fairwinds-charts
kubectl -n observability get pods -l app.kubernetes.io/instance=fairwinds-charts
```

## Reconcile
```sh
flux -n observability reconcile helmrelease fairwinds-charts
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
