# Speedtest Exporter

GitOps deployment notes for `speedtest-exporter` in the `observability` namespace.

## Context
- Deployment path: `kubernetes/apps/observability/speedtest-exporter/app`
- HelmRelease: `kubernetes/apps/observability/speedtest-exporter/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/observability/speedtest-exporter/app/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `30m`
- Timeout: `not specified`
- Controllers: `main`

## Runtime
- Images:
  - `ghcr.io/miguelndecarvalho/speedtest-exporter` (`v3.5.4`)
- Service declared: yes
- Route/ingress declared: not declared in helmrelease.yaml

## Files
- `./helmrelease.yaml`
- `./prometheusrule.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/observability/speedtest-exporter/app
kubectl -n observability get helmrelease speedtest-exporter
kubectl -n observability get pods -l app.kubernetes.io/instance=speedtest-exporter
```

## Reconcile
```sh
flux -n observability reconcile helmrelease speedtest-exporter
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
