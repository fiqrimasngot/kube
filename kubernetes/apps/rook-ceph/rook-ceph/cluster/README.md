# Rook Ceph — Cluster

GitOps deployment notes for `rook-ceph-cluster` in the `rook-ceph` namespace.

## Context
- Deployment path: `kubernetes/apps/rook-ceph/rook-ceph/cluster`
- HelmRelease: `kubernetes/apps/rook-ceph/rook-ceph/cluster/helmrelease.yaml`
- Kustomization: `kubernetes/apps/rook-ceph/rook-ceph/cluster/kustomization.yaml`
- Chart/reference: `rook-ceph-cluster`
- Reconcile interval: `15m`
- Timeout: `not specified`

## Runtime
- Images: managed by the referenced chart or not pinned in this file.
- Service declared: not declared in helmrelease.yaml
- Route/ingress declared: yes

## Files
- `./helmrelease.yaml`
- `./prometheusrule.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/rook-ceph/rook-ceph/cluster
kubectl -n rook-ceph get helmrelease rook-ceph-cluster
kubectl -n rook-ceph get pods -l app.kubernetes.io/instance=rook-ceph-cluster
```

## Reconcile
```sh
flux -n rook-ceph reconcile helmrelease rook-ceph-cluster
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
