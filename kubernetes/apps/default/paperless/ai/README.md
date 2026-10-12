# Paperless — AI

GitOps deployment notes for `paperless-ai` in the `default` namespace.

## Context
- Deployment path: `kubernetes/apps/default/paperless/ai`
- HelmRelease: `kubernetes/apps/default/paperless/ai/helmrelease.yaml`
- Kustomization: `kubernetes/apps/default/paperless/ai/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `15m`
- Timeout: `15m`
- Controllers: `paperless-ai`

## Runtime
- Images:
  - `docker.io/clusterzx/paperless-ai` (`3.0.9@sha256:2b65888163fd59716f1c8285b31c5bd0b30c9c3c192c42b516688e3887d4ba60`)
- Service declared: yes
- Route/ingress declared: yes
- Encrypted secret manifests: `secrets.sops.yaml`

## Files
- `./helmrelease.yaml`
- `./secrets.sops.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/default/paperless/ai
kubectl -n default get helmrelease paperless-ai
kubectl -n default get pods -l app.kubernetes.io/instance=paperless-ai
```

## Reconcile
```sh
flux -n default reconcile helmrelease paperless-ai
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
