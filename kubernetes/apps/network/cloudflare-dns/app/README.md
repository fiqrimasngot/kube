# Cloudflare DNS

GitOps deployment notes for `cloudflare-dns` in the `network` namespace.

## Context
- Deployment path: `kubernetes/apps/network/cloudflare-dns/app`
- HelmRelease: `kubernetes/apps/network/cloudflare-dns/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/network/cloudflare-dns/app/kustomization.yaml`
- Chart/reference: `cloudflare-dns`
- Reconcile interval: `1h`
- Timeout: `not specified`

## Runtime
- Images: managed by the referenced chart or not pinned in this file.
- Service declared: not declared in helmrelease.yaml
- Route/ingress declared: yes
- Encrypted secret manifests: `secret.sops.yaml`

## Files
- `./secret.sops.yaml`
- `./helmrelease.yaml`
- `./ocirepository.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/network/cloudflare-dns/app
kubectl -n network get helmrelease cloudflare-dns
kubectl -n network get pods -l app.kubernetes.io/instance=cloudflare-dns
```

## Reconcile
```sh
flux -n network reconcile helmrelease cloudflare-dns
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
