# Cyberchef

GitOps deployment notes for `cyberchef` in the `default` namespace.

## Context
- Deployment path: `kubernetes/apps/default/cyberchef/app`
- HelmRelease: `kubernetes/apps/default/cyberchef/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/default/cyberchef/app/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `15m`
- Timeout: `not specified`
- Controllers: `main`

## Runtime
- Images:
  - `docker.io/mpepping/cyberchef` (`v10.19.4`)
- Service declared: yes
- Route/ingress declared: yes

## Files
- `./helmrelease.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/default/cyberchef/app
kubectl -n default get helmrelease cyberchef
kubectl -n default get pods -l app.kubernetes.io/instance=cyberchef
```

## Reconcile
```sh
flux -n default reconcile helmrelease cyberchef
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
