# Dcgm Exporter

GitOps deployment notes for `dcgm-exporter` in the `observability` namespace.

## Context
- Deployment path: `kubernetes/apps/observability/dcgm-exporter/app`
- HelmRelease: `kubernetes/apps/observability/dcgm-exporter/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/observability/dcgm-exporter/app/kustomization.yaml`
- Chart/reference: `spec:`
- Reconcile interval: `1h`
- Timeout: `not specified`

## Runtime
- Images:
  - `nvcr.io/nvidia/k8s/dcgm-exporter` (`3.3.8-3.6.0-ubuntu22.04`)
- Service declared: not declared in helmrelease.yaml
- Route/ingress declared: not declared in helmrelease.yaml

## Files
- `./helmrelease.yaml`
- `./alerts.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/observability/dcgm-exporter/app
kubectl -n observability get helmrelease dcgm-exporter
kubectl -n observability get pods -l app.kubernetes.io/instance=dcgm-exporter
```

## Reconcile
```sh
flux -n observability reconcile helmrelease dcgm-exporter
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
