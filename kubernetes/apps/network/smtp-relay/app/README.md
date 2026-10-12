# SMTP Relay

GitOps deployment notes for `smtp-relay` in the `network` namespace.

## Context
- Deployment path: `kubernetes/apps/network/smtp-relay/app`
- HelmRelease: `kubernetes/apps/network/smtp-relay/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/network/smtp-relay/app/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `1h`
- Timeout: `not specified`
- Controllers: `config`, `cache`, `tls`, `state`, `runtime`

## Runtime
- Images:
  - `ghcr.io/foxcpp/maddy` (`0.8.2@sha256:eeb5813fc4d101ec5d8f7b08b7255fd76ced2a06884ea94450c8a9a22fd6a08d`)
- Service declared: yes
- Route/ingress declared: not declared in helmrelease.yaml
- Encrypted secret manifests: `secret.sops.yaml`

## Files
- `./helmrelease.yaml`
- `./certificate.yaml`
- `./secret.sops.yaml`
- `name: smtp-relay-configmap`
- `maddy.conf=./resources/maddy.conf`

## Validate
```sh
kubectl kustomize kubernetes/apps/network/smtp-relay/app
kubectl -n network get helmrelease smtp-relay
kubectl -n network get pods -l app.kubernetes.io/instance=smtp-relay
```

## Reconcile
```sh
flux -n network reconcile helmrelease smtp-relay
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
