# Volsync

GitOps deployment notes for `volsync` in the `volsync-system` namespace.

## Context
- Deployment path: `kubernetes/apps/volsync-system/volsync/app`
- HelmRelease: `kubernetes/apps/volsync-system/volsync/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/volsync-system/volsync/app/kustomization.yaml`
- Chart/reference: `volsync`
- Reconcile interval: `15m`
- Timeout: `not specified`

## Runtime
- Images: managed by the referenced chart or not pinned in this file.
- Service declared: not declared in helmrelease.yaml
- Route/ingress declared: not declared in helmrelease.yaml

## Files
- `./helmrelease.yaml`
- `./prometheusrule.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/volsync-system/volsync/app
kubectl -n volsync-system get helmrelease volsync
kubectl -n volsync-system get pods -l app.kubernetes.io/instance=volsync
```

## Reconcile
```sh
flux -n volsync-system reconcile helmrelease volsync
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
