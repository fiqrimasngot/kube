# Pihole

GitOps deployment notes for `pihole` in the `network` namespace.

## Context
- Deployment path: `kubernetes/apps/network/pihole/app`
- HelmRelease: `kubernetes/apps/network/pihole/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/network/pihole/app/kustomization.yaml`
- Chart/reference: `spec:`
- Reconcile interval: `2h`
- Timeout: `3m`

## Runtime
- Images:
  - `crazymax/cloudflared` (`latest@sha256:7e94afadbc1fca729d4187e566697319a8752e471085f4d86396300e21039508`)
  - `pihole/pihole` (`2025.11.1`)
  - `ekofr/pihole-exporter` (`v1.2.0`)
- Service declared: not declared in helmrelease.yaml
- Route/ingress declared: yes
- Encrypted secret manifests: `secret.sops.yaml`

## Files
- `./secret.sops.yaml`
- `./helmrelease.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/network/pihole/app
kubectl -n network get helmrelease pihole
kubectl -n network get pods -l app.kubernetes.io/instance=pihole
```

## Reconcile
```sh
flux -n network reconcile helmrelease pihole
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
