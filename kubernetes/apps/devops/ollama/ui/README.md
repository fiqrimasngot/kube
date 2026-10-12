# Ollama — UI

GitOps deployment notes for `open-webui` in the `devops` namespace.

## Context
- Deployment path: `kubernetes/apps/devops/ollama/ui`
- HelmRelease: `kubernetes/apps/devops/ollama/ui/helmrelease.yaml`
- Kustomization: `kubernetes/apps/devops/ollama/ui/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `1h`
- Timeout: `not specified`
- Controllers: `open-webui`, `app`

## Runtime
- Images:
  - `ghcr.io/open-webui/open-webui` (`0.7.2@sha256:16d9a3615b45f14a0c89f7ad7a3bf151f923ed32c2e68f9204eb17d1ce40774b`)
  - `ghcr.io/home-operations/postgres-init` (`18.1.0@sha256:3c54d39f19fdb82ed5b3f286450e4071133cc6025bd0e25856bc2c522f8fc030`)
- Service declared: yes
- Route/ingress declared: yes
- Encrypted secret manifests: `secrets.sops.yaml`

## Files
- `./helmrelease.yaml`
- `./secrets.sops.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/devops/ollama/ui
kubectl -n devops get helmrelease open-webui
kubectl -n devops get pods -l app.kubernetes.io/instance=open-webui
```

## Reconcile
```sh
flux -n devops reconcile helmrelease open-webui
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
