# Shlink

GitOps deployment notes for `shlink` in the `default` namespace.

## Context
- Deployment path: `kubernetes/apps/default/shlink/app`
- HelmRelease: `kubernetes/apps/default/shlink/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/default/shlink/app/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `30m`
- Timeout: `not specified`
- Controllers: `shlink`, `main`, `tmp`, `tmp-data`

## Runtime
- Images:
  - `ghcr.io/onedr0p/postgres-init` (`16`)
  - `ghcr.io/shlinkio/shlink` (`4.6.0@sha256:e607cd6f8c7f6bfd4cc734c812538d4123602c455a439c43dd02b35af885948f`)
- Service declared: yes
- Route/ingress declared: yes
- Encrypted secret manifests: `secrets.sops.yaml`

## Files
- `./helmrelease.yaml`
- `./secrets.sops.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/default/shlink/app
kubectl -n default get helmrelease shlink
kubectl -n default get pods -l app.kubernetes.io/instance=shlink
```

## Reconcile
```sh
flux -n default reconcile helmrelease shlink
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
