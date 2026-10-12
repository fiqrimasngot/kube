# Shlink — Web

GitOps deployment notes for `shlink-web` in the `default` namespace.

## Context
- Deployment path: `kubernetes/apps/default/shlink/web`
- HelmRelease: `kubernetes/apps/default/shlink/web/helmrelease.yaml`
- Kustomization: `kubernetes/apps/default/shlink/web/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `30m`
- Timeout: `not specified`
- Controllers: `shlink-web`, `main`

## Runtime
- Images:
  - `ghcr.io/shlinkio/shlink-web-client` (`4.6.2`)
- Service declared: yes
- Route/ingress declared: yes
- Encrypted secret manifests: `secrets.sops.yaml`

## Files
- `./helmrelease.yaml`
- `./secrets.sops.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/default/shlink/web
kubectl -n default get helmrelease shlink-web
kubectl -n default get pods -l app.kubernetes.io/instance=shlink-web
```

## Reconcile
```sh
flux -n default reconcile helmrelease shlink-web
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
