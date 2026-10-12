# Loki

GitOps deployment notes for `grafana` in the `observability` namespace.

## Context
- Deployment path: `kubernetes/apps/observability/loki/app`
- HelmRelease: `kubernetes/apps/observability/loki/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/observability/loki/app/kustomization.yaml`
- Chart/reference: `spec:`
- Reconcile interval: `2h`
- Timeout: `15m`
- Controllers: `storage`, `deploymentStrategy`, `dashboards`

## Runtime
- Images:
  - `nginxinc/nginx-unprivileged` (`1.27.4-alpine`)
  - `ghcr.io/kiwigrid/k8s-sidecar`
- Service declared: not declared in helmrelease.yaml
- Route/ingress declared: yes
- Encrypted secret manifests: `secrets.sops.yaml`

## Files
- `./helmrelease.yaml`
- `./secrets.sops.yaml`
- `name: loki-rules`
- `SyslogErrorRate.yaml=./alerts/syslog-errors.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/observability/loki/app
kubectl -n observability get helmrelease grafana
kubectl -n observability get pods -l app.kubernetes.io/instance=grafana
```

## Reconcile
```sh
flux -n observability reconcile helmrelease grafana
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
