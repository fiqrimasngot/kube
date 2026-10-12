# Homebox

GitOps deployment notes for `homebox` in the `default` namespace.

## Context
- Deployment path: `kubernetes/apps/default/homebox/app`
- HelmRelease: `kubernetes/apps/default/homebox/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/default/homebox/app/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `30m`
- Timeout: `not specified`
- Controllers: `homebox`, `main`, `tmp`

## Runtime
- Images:
  - `ghcr.io/sysadminsmedia/homebox` (`0.26.2`)
- Service declared: yes
- Route/ingress declared: yes

## Files
- `./helmrelease.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/default/homebox/app
kubectl -n default get helmrelease homebox
kubectl -n default get pods -l app.kubernetes.io/instance=homebox
```

## Reconcile
```sh
flux -n default reconcile helmrelease homebox
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
