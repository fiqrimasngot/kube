# Tdarr — Node

GitOps deployment notes for `tdarr-node` in the `media` namespace.

## Context
- Deployment path: `kubernetes/apps/media/tdarr/node`
- HelmRelease: `kubernetes/apps/media/tdarr/node/helmrelease.yaml`
- Kustomization: `kubernetes/apps/media/tdarr/node/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `30m`
- Timeout: `not specified`
- Controllers: `tdarr-node`, `movies`, `tv`, `music`, `transcode`

## Runtime
- Images:
  - `ghcr.io/haveagitgat/tdarr_node` (`2.58.02@sha256:62e14509bc19dea9b6f5dc85d0942163b6fa240d780a53eb590d894d46c9e1f2`)
- Service declared: yes
- Route/ingress declared: not declared in helmrelease.yaml

## Files
- `helmrelease.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/media/tdarr/node
kubectl -n media get helmrelease tdarr-node
kubectl -n media get pods -l app.kubernetes.io/instance=tdarr-node
```

## Reconcile
```sh
flux -n media reconcile helmrelease tdarr-node
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
