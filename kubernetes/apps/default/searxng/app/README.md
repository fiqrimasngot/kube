# Searxng

GitOps deployment notes for `searxng` in the `default` namespace.

## Context
- Deployment path: `kubernetes/apps/default/searxng/app`
- HelmRelease: `kubernetes/apps/default/searxng/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/default/searxng/app/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `30m`
- Timeout: `not specified`
- Controllers: `searxng`, `config`, `tmp`

## Runtime
- Images:
  - `docker.io/searxng/searxng` (`2024.7.7-ef103ba80`)
- Service declared: yes
- Route/ingress declared: yes
- Encrypted secret manifests: `secrets.sops.yaml`

## Files
- `./secrets.sops.yaml`
- `./helmrelease.yaml`
- `name: searxng-configmap`
- `settings.yml=./resources/settings.yml`
- `limiter.toml=./resources/limiter.toml`

## Validate
```sh
kubectl kustomize kubernetes/apps/default/searxng/app
kubectl -n default get helmrelease searxng
kubectl -n default get pods -l app.kubernetes.io/instance=searxng
```

## Reconcile
```sh
flux -n default reconcile helmrelease searxng
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
