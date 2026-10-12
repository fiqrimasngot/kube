# Blackbox Exporter

GitOps deployment notes for `prometheus-community` in the `observability` namespace.

## Context
- Deployment path: `kubernetes/apps/observability/blackbox-exporter/app`
- HelmRelease: `kubernetes/apps/observability/blackbox-exporter/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/observability/blackbox-exporter/app/kustomization.yaml`
- Chart/reference: `spec:`
- Reconcile interval: `5m`
- Timeout: `5s`

## Runtime
- Images: managed by the referenced chart or not pinned in this file.
- Service declared: not declared in helmrelease.yaml
- Route/ingress declared: yes

## Files
- `./helmrelease.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/observability/blackbox-exporter/app
kubectl -n observability get helmrelease prometheus-community
kubectl -n observability get pods -l app.kubernetes.io/instance=prometheus-community
```

## Reconcile
```sh
flux -n observability reconcile helmrelease prometheus-community
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
