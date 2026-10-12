# Cert Manager

GitOps deployment notes for `cert-manager` in the `cert-manager` namespace.

## Context
- Deployment path: `kubernetes/apps/cert-manager/cert-manager/app`
- HelmRelease: `kubernetes/apps/cert-manager/cert-manager/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/cert-manager/cert-manager/app/kustomization.yaml`
- Chart/reference: `cert-manager`
- Reconcile interval: `1h`
- Timeout: `not specified`

## Runtime
- Images: managed by the referenced chart or not pinned in this file.
- Service declared: not declared in helmrelease.yaml
- Route/ingress declared: not declared in helmrelease.yaml
- Encrypted secret manifests: `secret.sops.yaml`

## Files
- `./clusterissuer.yaml`
- `./helmrelease.yaml`
- `./ocirepository.yaml`
- `./secret.sops.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/cert-manager/cert-manager/app
kubectl -n cert-manager get helmrelease cert-manager
kubectl -n cert-manager get pods -l app.kubernetes.io/instance=cert-manager
```

## Reconcile
```sh
flux -n cert-manager reconcile helmrelease cert-manager
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
