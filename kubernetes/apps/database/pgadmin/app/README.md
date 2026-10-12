# Pgadmin

GitOps deployment notes for `pgadmin` in the `database` namespace.

## Context
- Deployment path: `kubernetes/apps/database/pgadmin/app`
- HelmRelease: `kubernetes/apps/database/pgadmin/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/database/pgadmin/app/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `30m`
- Timeout: `not specified`
- Controllers: `pgadmin`, `app`

## Runtime
- Images:
  - `dpage/pgadmin4` (`'9.11'`)
- Service declared: yes
- Route/ingress declared: yes
- Encrypted secret manifests: `secrets.sops.yaml`

## Files
- `./secrets.sops.yaml`
- `./helmrelease.yaml`
- `name: servers-json`
- `config/servers.json`

## Validate
```sh
kubectl kustomize kubernetes/apps/database/pgadmin/app
kubectl -n database get helmrelease pgadmin
kubectl -n database get pods -l app.kubernetes.io/instance=pgadmin
```

## Reconcile
```sh
flux -n database reconcile helmrelease pgadmin
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
