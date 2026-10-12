# Flux Instance

GitOps deployment notes for `flux-instance` in the `flux-system` namespace.

## Context
- Deployment path: `kubernetes/apps/flux-system/flux-instance/app`
- HelmRelease: `kubernetes/apps/flux-system/flux-instance/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/flux-system/flux-instance/app/kustomization.yaml`
- Chart/reference: `flux-instance`
- Reconcile interval: `1h`
- Timeout: `not specified`

## Runtime
- Images: managed by the referenced chart or not pinned in this file.
- Service declared: not declared in helmrelease.yaml
- Route/ingress declared: not declared in helmrelease.yaml
- Encrypted secret manifests: `secret.sops.yaml`

## Files
- `./helmrelease.yaml`
- `./ocirepository.yaml`
- `./secret.sops.yaml`
- `./httproute.yaml`
- `./receiver.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/flux-system/flux-instance/app
kubectl -n flux-system get helmrelease flux-instance
kubectl -n flux-system get pods -l app.kubernetes.io/instance=flux-instance
```

## Reconcile
```sh
flux -n flux-system reconcile helmrelease flux-instance
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
