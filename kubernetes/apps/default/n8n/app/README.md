# N8n

GitOps deployment notes for `n8n` in the `default` namespace.

## Context
- Deployment path: `kubernetes/apps/default/n8n/app`
- HelmRelease: `kubernetes/apps/default/n8n/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/default/n8n/app/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `30m`
- Timeout: `not specified`
- Controllers: `n8n`, `main`

## Runtime
- Images:
  - `ghcr.io/n8n-io/n8n` (`2.42.2`)
- Service declared: yes
- Route/ingress declared: yes
- Encrypted secret manifests: `secrets.sops.yaml`

## Files
- `./helmrelease.yaml`
- `./secrets.sops.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/default/n8n/app
kubectl -n default get helmrelease n8n
kubectl -n default get pods -l app.kubernetes.io/instance=n8n
```

## Reconcile
```sh
flux -n default reconcile helmrelease n8n
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
