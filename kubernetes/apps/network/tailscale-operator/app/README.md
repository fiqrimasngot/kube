# Tailscale Operator

GitOps deployment notes for `tailscale` in the `network` namespace.

## Context
- Deployment path: `kubernetes/apps/network/tailscale-operator/app`
- HelmRelease: `kubernetes/apps/network/tailscale-operator/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/network/tailscale-operator/app/kustomization.yaml`
- Chart/reference: `spec:`
- Reconcile interval: `2h`
- Timeout: `not specified`

## Runtime
- Images: managed by the referenced chart or not pinned in this file.
- Service declared: not declared in helmrelease.yaml
- Route/ingress declared: not declared in helmrelease.yaml
- Encrypted secret manifests: `secret.sops.yaml`

## Files
- `secret.sops.yaml`
- `helmrelease.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/network/tailscale-operator/app
kubectl -n network get helmrelease tailscale
kubectl -n network get pods -l app.kubernetes.io/instance=tailscale
```

## Reconcile
```sh
flux -n network reconcile helmrelease tailscale
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
