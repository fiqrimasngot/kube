# CSI Driver NFS

GitOps deployment notes for `csi-driver-nfs` in the `storage` namespace.

## Context
- Deployment path: `kubernetes/apps/storage/csi-driver-nfs/app`
- HelmRelease: `kubernetes/apps/storage/csi-driver-nfs/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/storage/csi-driver-nfs/app/kustomization.yaml`
- Chart/reference: `spec:`
- Reconcile interval: `2h`
- Timeout: `not specified`

## Runtime
- Images: managed by the referenced chart or not pinned in this file.
- Service declared: not declared in helmrelease.yaml
- Route/ingress declared: not declared in helmrelease.yaml

## Files
- `./helmrelease.yaml`
- `./storageclass.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/storage/csi-driver-nfs/app
kubectl -n storage get helmrelease csi-driver-nfs
kubectl -n storage get pods -l app.kubernetes.io/instance=csi-driver-nfs
```

## Reconcile
```sh
flux -n storage reconcile helmrelease csi-driver-nfs
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
