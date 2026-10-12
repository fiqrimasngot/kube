# Obsidian Couchdb

GitOps deployment notes for `obsidian-couchdb` in the `database` namespace.

## Context
- Deployment path: `kubernetes/apps/database/obsidian-couchdb/app`
- HelmRelease: `kubernetes/apps/database/obsidian-couchdb/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/database/obsidian-couchdb/app/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `30m`
- Timeout: `not specified`
- Controllers: `main`, `config`, `config-storage`

## Runtime
- Images:
  - `public.ecr.aws/docker/library/busybox` (`latest`)
  - `public.ecr.aws/docker/library/couchdb` (`3.5.1`)
- Service declared: yes
- Route/ingress declared: yes
- Encrypted secret manifests: `secrets.sops.yaml`

## Files
- `./helmrelease.yaml`
- `./secrets.sops.yaml`
- `name: obsidian-couchdb-configmap`
- `config/config.ini`

## Validate
```sh
kubectl kustomize kubernetes/apps/database/obsidian-couchdb/app
kubectl -n database get helmrelease obsidian-couchdb
kubectl -n database get pods -l app.kubernetes.io/instance=obsidian-couchdb
```

## Reconcile
```sh
flux -n database reconcile helmrelease obsidian-couchdb
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
