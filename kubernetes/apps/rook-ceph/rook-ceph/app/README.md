# Rook Ceph

GitOps deployment notes for `rook-ceph` in the `rook-ceph` namespace.

## Context
- Deployment path: `kubernetes/apps/rook-ceph/rook-ceph/app`
- HelmRelease: `kubernetes/apps/rook-ceph/rook-ceph/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/rook-ceph/rook-ceph/app/kustomization.yaml`
- Chart/reference: `rook-ceph`
- Reconcile interval: `15m`
- Timeout: `not specified`

## Runtime
- Images:
  - `ghcr.io/rook/ceph` (`v1.18.8`)
- Service declared: not declared in helmrelease.yaml
- Route/ingress declared: not declared in helmrelease.yaml
- Encrypted secret manifests: `secret.sops.yaml`

## Files
- `./helmrelease.yaml`
- `./secret.sops.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/rook-ceph/rook-ceph/app
kubectl -n rook-ceph get helmrelease rook-ceph
kubectl -n rook-ceph get pods -l app.kubernetes.io/instance=rook-ceph
```

## Reconcile
```sh
flux -n rook-ceph reconcile helmrelease rook-ceph
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
