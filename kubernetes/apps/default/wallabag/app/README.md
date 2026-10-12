# Wallabag

GitOps deployment notes for `wallabag` in the `default` namespace.

## Context
- Deployment path: `kubernetes/apps/default/wallabag/app`
- HelmRelease: `kubernetes/apps/default/wallabag/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/default/wallabag/app/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `30m`
- Timeout: `15m`
- Controllers: `wallabag`, `main`

## Runtime
- Images:
  - `ghcr.io/home-operations/postgres-init` (`18`)
  - `wallabag/wallabag` (`2.6.14`)
- Service declared: yes
- Route/ingress declared: yes
- Encrypted secret manifests: `secrets.sops.yaml`

## Files
- `./helmrelease.yaml`
- `./secrets.sops.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/default/wallabag/app
kubectl -n default get helmrelease wallabag
kubectl -n default get pods -l app.kubernetes.io/instance=wallabag
```

## Reconcile
```sh
flux -n default reconcile helmrelease wallabag
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
