# Paperless

GitOps deployment notes for `paperless` in the `default` namespace.

## Context
- Deployment path: `kubernetes/apps/default/paperless/app`
- HelmRelease: `kubernetes/apps/default/paperless/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/default/paperless/app/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `15m`
- Timeout: `15m`
- Controllers: `paperless`, `app`

## Runtime
- Images:
  - `ghcr.io/onedr0p/postgres-init` (`17.4`)
  - `ghcr.io/paperless-ngx/paperless-ngx` (`2.20.15`)
  - `docker.io/apache/tika` (`3.2.3.0-full`)
  - `gotenberg/gotenberg` (`8.25.1`)
- Service declared: yes
- Route/ingress declared: yes
- Encrypted secret manifests: `secrets.sops.yaml`

## Files
- `./helmrelease.yaml`
- `./secrets.sops.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/default/paperless/app
kubectl -n default get helmrelease paperless
kubectl -n default get pods -l app.kubernetes.io/instance=paperless
```

## Reconcile
```sh
flux -n default reconcile helmrelease paperless
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
