# Smartctl Exporter

GitOps deployment notes for `smartctl-exporter` in the `observability` namespace.

## Context
- Deployment path: `kubernetes/apps/observability/smartctl-exporter/app`
- HelmRelease: `kubernetes/apps/observability/smartctl-exporter/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/observability/smartctl-exporter/app/kustomization.yaml`
- Chart/reference: `smartctl-exporter`
- Reconcile interval: `5m`
- Timeout: `not specified`

## Runtime
- Images: managed by the referenced chart or not pinned in this file.
- Service declared: not declared in helmrelease.yaml
- Route/ingress declared: not declared in helmrelease.yaml

## Files
- `./helmrelease.yaml`
- `./prometheusrule.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/observability/smartctl-exporter/app
kubectl -n observability get helmrelease smartctl-exporter
kubectl -n observability get pods -l app.kubernetes.io/instance=smartctl-exporter
```

## Reconcile
```sh
flux -n observability reconcile helmrelease smartctl-exporter
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
