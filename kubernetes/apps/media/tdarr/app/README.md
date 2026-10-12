# Tdarr

GitOps deployment notes for `tdarr` in the `media` namespace.

## Context
- Deployment path: `kubernetes/apps/media/tdarr/app`
- HelmRelease: `kubernetes/apps/media/tdarr/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/media/tdarr/app/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `30m`
- Timeout: `not specified`
- Controllers: `tdarr`, `transcode`, `movies`, `tv`, `music`

## Runtime
- Images:
  - `ghcr.io/haveagitgat/tdarr` (`2.58.02@sha256:20a5656c4af4854e1877046294f77113f949d27e35940a9a65f231423d063207`)
- Service declared: yes
- Route/ingress declared: yes

## Files
- `helmrelease.yaml`
- `priorityclass.yaml`
- `configmap.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/media/tdarr/app
kubectl -n media get helmrelease tdarr
kubectl -n media get pods -l app.kubernetes.io/instance=tdarr
```

## Reconcile
```sh
flux -n media reconcile helmrelease tdarr
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
