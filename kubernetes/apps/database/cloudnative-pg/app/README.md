# Cloudnative Pg

GitOps deployment notes for `cloudnative-pg` in the `database` namespace.

## Context
- Deployment path: `kubernetes/apps/database/cloudnative-pg/app`
- HelmRelease: `kubernetes/apps/database/cloudnative-pg/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/database/cloudnative-pg/app/kustomization.yaml`
- Chart/reference: `spec:`
- Reconcile interval: `2h`
- Timeout: `not specified`

## Runtime
- Images: managed by the referenced chart or not pinned in this file.
- Service declared: not declared in helmrelease.yaml
- Route/ingress declared: not declared in helmrelease.yaml
- Encrypted secret manifests: `secrets.sops.yaml`

## Files
- `./helmrelease.yaml`
- `./secrets.sops.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/database/cloudnative-pg/app
kubectl -n database get helmrelease cloudnative-pg
kubectl -n database get pods -l app.kubernetes.io/instance=cloudnative-pg
```

## Reconcile
```sh
flux -n database reconcile helmrelease cloudnative-pg
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
