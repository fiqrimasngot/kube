# NFS Server

GitOps deployment notes for `nfs-server` in the `storage` namespace.

## Context
- Deployment path: `kubernetes/apps/storage/nfs-server/app`
- HelmRelease: `kubernetes/apps/storage/nfs-server/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/storage/nfs-server/app/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `1h`
- Timeout: `2m`
- Controllers: `nfs-server`, `exports`, `fake-export`

## Runtime
- Images:
  - `quay.io/aminvakil/alpine-nfs-server` (`latest`)
- Service declared: not declared in helmrelease.yaml
- Route/ingress declared: not declared in helmrelease.yaml
- Local PVC manifests: `pvc.yaml`

## Files
- `./helmrelease.yaml`
- `./pv.yaml`
- `./pvc.yaml`
- `./exports.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/storage/nfs-server/app
kubectl -n storage get helmrelease nfs-server
kubectl -n storage get pods -l app.kubernetes.io/instance=nfs-server
```

## Reconcile
```sh
flux -n storage reconcile helmrelease nfs-server
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
