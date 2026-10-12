# Snapshot Controller

GitOps deployment notes for `snapshot-controller` in the `volsync-system` namespace.

## Context
- Deployment path: `kubernetes/apps/volsync-system/snapshot-controller/app`
- HelmRelease: `kubernetes/apps/volsync-system/snapshot-controller/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/volsync-system/snapshot-controller/app/kustomization.yaml`
- Chart/reference: `snapshot-controller`
- Reconcile interval: `15m`
- Timeout: `not specified`

## Runtime
- Images: managed by the referenced chart or not pinned in this file.
- Service declared: not declared in helmrelease.yaml
- Route/ingress declared: not declared in helmrelease.yaml

## Files
- `./helmrelease.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/volsync-system/snapshot-controller/app
kubectl -n volsync-system get helmrelease snapshot-controller
kubectl -n volsync-system get pods -l app.kubernetes.io/instance=snapshot-controller
```

## Reconcile
```sh
flux -n volsync-system reconcile helmrelease snapshot-controller
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
