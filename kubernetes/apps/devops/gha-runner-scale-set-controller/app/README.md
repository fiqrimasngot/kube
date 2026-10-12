# Gha Runner Scale Set Controller

GitOps deployment notes for `actions-runner-controller` in the `devops` namespace.

## Context
- Deployment path: `kubernetes/apps/devops/gha-runner-scale-set-controller/app`
- HelmRelease: `kubernetes/apps/devops/gha-runner-scale-set-controller/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/devops/gha-runner-scale-set-controller/app/kustomization.yaml`
- Chart/reference: `spec:`
- Reconcile interval: `5m`
- Timeout: `not specified`

## Runtime
- Images: managed by the referenced chart or not pinned in this file.
- Service declared: not declared in helmrelease.yaml
- Route/ingress declared: not declared in helmrelease.yaml
- Encrypted secret manifests: `secrets.sops.yaml`

## Files
- `./secrets.sops.yaml`
- `./helmrelease.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/devops/gha-runner-scale-set-controller/app
kubectl -n devops get helmrelease actions-runner-controller
kubectl -n devops get pods -l app.kubernetes.io/instance=actions-runner-controller
```

## Reconcile
```sh
flux -n devops reconcile helmrelease actions-runner-controller
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
