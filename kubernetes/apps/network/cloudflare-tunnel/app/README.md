# Cloudflare Tunnel

GitOps deployment notes for `cloudflare-tunnel` in the `network` namespace.

## Context
- Deployment path: `kubernetes/apps/network/cloudflare-tunnel/app`
- HelmRelease: `kubernetes/apps/network/cloudflare-tunnel/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/network/cloudflare-tunnel/app/kustomization.yaml`
- Chart/reference: `cloudflare-tunnel`
- Reconcile interval: `1h`
- Timeout: `not specified`
- Controllers: `config-file`

## Runtime
- Images:
  - `docker.io/cloudflare/cloudflared` (`2026.9.1`)
- Service declared: yes
- Route/ingress declared: yes
- Encrypted secret manifests: `secret.sops.yaml`

## Files
- `./dnsendpoint.yaml`
- `./secret.sops.yaml`
- `./helmrelease.yaml`
- `./ocirepository.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/network/cloudflare-tunnel/app
kubectl -n network get helmrelease cloudflare-tunnel
kubectl -n network get pods -l app.kubernetes.io/instance=cloudflare-tunnel
```

## Reconcile
```sh
flux -n network reconcile helmrelease cloudflare-tunnel
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
