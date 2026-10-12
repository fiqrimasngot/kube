# Minio

GitOps deployment notes for `minio` in the `storage` namespace.

## Context
- Deployment path: `kubernetes/apps/storage/minio/app`
- HelmRelease: `kubernetes/apps/storage/minio/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/storage/minio/app/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `30m`
- Timeout: `15m`
- Controllers: `app`

## Runtime
- Images:
  - `docker.io/pgsty/silo` (`RELEASE.2026-09-16T00-00-00Z@sha256:635197cb9f36d01bee221d34d1c7d7960f6a95c48b0b6c01d99cd13bdae51a46`)
- Service declared: yes
- Route/ingress declared: yes
- Encrypted secret manifests: `secret.sops.yaml`

## Files
- `./helmrelease.yaml`
- `./secret.sops.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/storage/minio/app
kubectl -n storage get helmrelease minio
kubectl -n storage get pods -l app.kubernetes.io/instance=minio
```

## Reconcile
```sh
flux -n storage reconcile helmrelease minio
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
