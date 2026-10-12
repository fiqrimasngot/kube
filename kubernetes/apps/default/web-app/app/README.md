# Web App

GitOps deployment notes for `web-app` in the `default` namespace.

## Context
- Deployment path: `kubernetes/apps/default/web-app/app`
- HelmRelease: `kubernetes/apps/default/web-app/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/default/web-app/app/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `30m`
- Timeout: `not specified`

## Runtime
- Images:
  - `fiqrimasngot/bakeryapp` (`latest`)
- Service declared: yes
- Route/ingress declared: yes

## Files
- `./helmrelease.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/default/web-app/app
kubectl -n default get helmrelease web-app
kubectl -n default get pods -l app.kubernetes.io/instance=web-app
```

## Reconcile
```sh
flux -n default reconcile helmrelease web-app
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
