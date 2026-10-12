# Metrics Server

GitOps deployment notes for `metrics-server` in the `kube-system` namespace.

## Context
- Deployment path: `kubernetes/apps/kube-system/metrics-server/app`
- HelmRelease: `kubernetes/apps/kube-system/metrics-server/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/kube-system/metrics-server/app/kustomization.yaml`
- Chart/reference: `metrics-server`
- Reconcile interval: `1h`
- Timeout: `not specified`

## Runtime
- Images: managed by the referenced chart or not pinned in this file.
- Service declared: not declared in helmrelease.yaml
- Route/ingress declared: not declared in helmrelease.yaml

## Files
- `./helmrelease.yaml`
- `./ocirepository.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/kube-system/metrics-server/app
kubectl -n kube-system get helmrelease metrics-server
kubectl -n kube-system get pods -l app.kubernetes.io/instance=metrics-server
```

## Reconcile
```sh
flux -n kube-system reconcile helmrelease metrics-server
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
