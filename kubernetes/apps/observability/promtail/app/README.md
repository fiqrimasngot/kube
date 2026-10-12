# Promtail

GitOps deployment notes for `promtail` in the `observability` namespace.

## Context
- Deployment path: `kubernetes/apps/observability/promtail/app`
- HelmRelease: `kubernetes/apps/observability/promtail/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/observability/promtail/app/kustomization.yaml`
- Chart/reference: `spec:`
- Reconcile interval: `5m`
- Timeout: `60s`

## Runtime
- Images:
  - `grafana/promtail` (`3.6.3@sha256:130b6dd63277d99ce87560c0266c0c30d07bc15ba0a8a590d42215465d4f5363`)
- Service declared: yes
- Route/ingress declared: not declared in helmrelease.yaml

## Files
- `./helmrelease.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/observability/promtail/app
kubectl -n observability get helmrelease promtail
kubectl -n observability get pods -l app.kubernetes.io/instance=promtail
```

## Reconcile
```sh
flux -n observability reconcile helmrelease promtail
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
