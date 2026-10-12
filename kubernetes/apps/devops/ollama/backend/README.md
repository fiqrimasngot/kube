# Ollama — Backend

GitOps deployment notes for `ollama` in the `devops` namespace.

## Context
- Deployment path: `kubernetes/apps/devops/ollama/backend`
- HelmRelease: `kubernetes/apps/devops/ollama/backend/helmrelease.yaml`
- Kustomization: `kubernetes/apps/devops/ollama/backend/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `30m`
- Timeout: `not specified`

## Runtime
- Images:
  - `docker.io/ollama/ollama` (`0.19.0`)
- Service declared: yes
- Route/ingress declared: yes

## Files
- `./helmrelease.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/devops/ollama/backend
kubectl -n devops get helmrelease ollama
kubectl -n devops get pods -l app.kubernetes.io/instance=ollama
```

## Reconcile
```sh
flux -n devops reconcile helmrelease ollama
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
