# Nvidia Plugin

GitOps deployment notes for `nvidia-dvp` in the `kube-system` namespace.

## Context
- Deployment path: `kubernetes/apps/kube-system/nvidia-plugin/app`
- HelmRelease: `kubernetes/apps/kube-system/nvidia-plugin/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/kube-system/nvidia-plugin/app/kustomization.yaml`
- Chart/reference: `spec:`
- Reconcile interval: `30m`
- Timeout: `3m`

## Runtime
- Images: managed by the referenced chart or not pinned in this file.
- Service declared: not declared in helmrelease.yaml
- Route/ingress declared: not declared in helmrelease.yaml

## Files
- `./helmrelease.yaml`
- `./class.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/kube-system/nvidia-plugin/app
kubectl -n kube-system get helmrelease nvidia-dvp
kubectl -n kube-system get pods -l app.kubernetes.io/instance=nvidia-dvp
```

## Reconcile
```sh
flux -n kube-system reconcile helmrelease nvidia-dvp
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
