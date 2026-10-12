# Mealie

GitOps deployment notes for `mealie` in the `default` namespace.

## Context
- Deployment path: `kubernetes/apps/default/mealie/app`
- HelmRelease: `kubernetes/apps/default/mealie/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/default/mealie/app/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `30m`
- Timeout: `15m`
- Controllers: `mealie`, `app`, `tmp`, `nltk`

## Runtime
- Images:
  - `ghcr.io/onedr0p/postgres-init` (`16`)
  - `ghcr.io/mealie-recipes/mealie` (`v3.28.0`)
- Service declared: yes
- Route/ingress declared: yes
- Encrypted secret manifests: `secrets.sops.yaml`

## Files
- `./helmrelease.yaml`
- `./secrets.sops.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/default/mealie/app
kubectl -n default get helmrelease mealie
kubectl -n default get pods -l app.kubernetes.io/instance=mealie
```

## Reconcile
```sh
flux -n default reconcile helmrelease mealie
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
