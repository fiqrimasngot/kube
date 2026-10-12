# Garage

GitOps deployment notes for `garage` in the `storage` namespace.

## Context
- Deployment path: `kubernetes/apps/storage/garage/app`
- HelmRelease: `kubernetes/apps/storage/garage/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/storage/garage/app/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `30m`
- Timeout: `15m`
- Controllers: `garage`, `config`, `secrets`

## Runtime
- Images:
  - `mirror.gcr.io/dxflrs/garage` (`v2.4.1@sha256:9c96caa2612d3411acc5b0e6701fb238dbfba33e533a6d7d3d811a4b12d0d020`)
- Service declared: yes
- Route/ingress declared: not declared in helmrelease.yaml
- Encrypted secret manifests: `secret.sops.yaml`

## Files
- `./helmrelease.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/storage/garage/app
kubectl -n storage get helmrelease garage
kubectl -n storage get pods -l app.kubernetes.io/instance=garage
```

## Reconcile
```sh
flux -n storage reconcile helmrelease garage
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
