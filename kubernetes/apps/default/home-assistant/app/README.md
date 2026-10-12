# Home Assistant

GitOps deployment notes for `home-assistant` in the `default` namespace.

## Context
- Deployment path: `kubernetes/apps/default/home-assistant/app`
- HelmRelease: `kubernetes/apps/default/home-assistant/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/default/home-assistant/app/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `15m`
- Timeout: `not specified`
- Controllers: `main`

## Runtime
- Images:
  - `ghcr.io/home-operations/home-assistant` (`2026.6.3@sha256:82db7a297c96a0288559c5f2849878168c14a06557edc114084d874268c92a9a`)
  - `ghcr.io/coder/code-server` (`4.139.1`)
- Service declared: yes
- Route/ingress declared: yes
- Encrypted secret manifests: `secrets.sops.yaml`

## Files
- `./helmrelease.yaml`
- `./secrets.sops.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/default/home-assistant/app
kubectl -n default get helmrelease home-assistant
kubectl -n default get pods -l app.kubernetes.io/instance=home-assistant
```

## Reconcile
```sh
flux -n default reconcile helmrelease home-assistant
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
