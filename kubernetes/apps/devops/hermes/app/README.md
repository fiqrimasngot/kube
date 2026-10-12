# Hermes

GitOps deployment notes for `hermes` in the `devops` namespace.

## Context
- Deployment path: `kubernetes/apps/devops/hermes/app`
- HelmRelease: `kubernetes/apps/devops/hermes/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/devops/hermes/app/kustomization.yaml`
- Chart/reference: `hermes`
- Reconcile interval: `1h`
- Timeout: `not specified`
- Controllers: `tmp`, `config`

## Runtime
- Images:
  - `docker.io/library/alpine` (`3.24`)
  - `nousresearch/hermes-agent` (`v2026.9.24@sha256:fca358f12efd65bfaaca05884166f15c0e2788375ca30d77061ac1ebc96452b7`)
  - `ghcr.io/coder/code-server` (`4.139.1@sha256:0c067c3cf09ed1830ce282387826be8feefef8a5828f462791c2df3f1007ee17`)
- Service declared: yes
- Route/ingress declared: yes
- Encrypted secret manifests: `secret.sops.yaml`

## Files
- `./secret.sops.yaml`
- `./helmrelease.yaml`
- `./ocirepository.yaml`
- `name: hermes-configmap`
- `config.yaml=./resources/config.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/devops/hermes/app
kubectl -n devops get helmrelease hermes
kubectl -n devops get pods -l app.kubernetes.io/instance=hermes
```

## Reconcile
```sh
flux -n devops reconcile helmrelease hermes
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
