# Uptime Kuma

GitOps deployment notes for `uptime-kuma` in the `observability` namespace.

## Context
- Deployment path: `kubernetes/apps/observability/uptime-kuma/app`
- HelmRelease: `kubernetes/apps/observability/uptime-kuma/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/observability/uptime-kuma/app/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `15m`
- Timeout: `"3600"`
- Controllers: `main`

## Runtime
- Images:
  - `louislam/uptime-kuma` (`2.0.2`)
- Service declared: yes
- Route/ingress declared: yes

## Files
- `./helmrelease.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/observability/uptime-kuma/app
kubectl -n observability get helmrelease uptime-kuma
kubectl -n observability get pods -l app.kubernetes.io/instance=uptime-kuma
```

## Reconcile
```sh
flux -n observability reconcile helmrelease uptime-kuma
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
