# Honcho

GitOps deployment notes for `honcho` in the `devops` namespace.

## Context
- Deployment path: `kubernetes/apps/devops/honcho/app`
- HelmRelease: `kubernetes/apps/devops/honcho/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/devops/honcho/app/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `30m`
- Timeout: `15m`
- Controllers: `api`, `deriver`

## Runtime
- Images:
  - `ghcr.io/plastic-labs/honcho` (`latest@sha256:c8f99f1d78d5698c53c559cfff9c00aa1dd4ad8bd57b5ced1e1795eb6a17f16c`)
- Service declared: yes
- Route/ingress declared: yes
- Encrypted secret manifests: `secrets.sops.yaml`, `auth-secret.sops.yaml`

## Files
- `./helmrelease.yaml`
- `./secrets.sops.yaml`
- `./auth-secret.sops.yaml`
- `./postgres.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/devops/honcho/app
kubectl -n devops get helmrelease honcho
kubectl -n devops get pods -l app.kubernetes.io/instance=honcho
```

## Reconcile
```sh
flux -n devops reconcile helmrelease honcho
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
