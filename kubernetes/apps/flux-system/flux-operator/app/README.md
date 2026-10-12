# Flux Operator

GitOps deployment notes for `flux-operator` in the `flux-system` namespace.

## Context
- Deployment path: `kubernetes/apps/flux-system/flux-operator/app`
- HelmRelease: `kubernetes/apps/flux-system/flux-operator/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/flux-system/flux-operator/app/kustomization.yaml`
- Chart/reference: `flux-operator`
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
kubectl kustomize kubernetes/apps/flux-system/flux-operator/app
kubectl -n flux-system get helmrelease flux-operator
kubectl -n flux-system get pods -l app.kubernetes.io/instance=flux-operator
```

## Reconcile
```sh
flux -n flux-system reconcile helmrelease flux-operator
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
