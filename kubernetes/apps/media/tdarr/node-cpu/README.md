# Tdarr — Node Cpu

GitOps deployment notes for `tdarr-node-cpu` in the `media` namespace.

## Context
- Deployment path: `kubernetes/apps/media/tdarr/node-cpu`
- HelmRelease: `kubernetes/apps/media/tdarr/node-cpu/helmrelease.yaml`
- Kustomization: `kubernetes/apps/media/tdarr/node-cpu/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `30m`
- Timeout: `not specified`
- Controllers: `tdarr-node-cpu`, `movies`, `tv`, `music`, `transcode`

## Runtime
- Images:
  - `ghcr.io/haveagitgat/tdarr_node` (`2.58.02@sha256:62e14509bc19dea9b6f5dc85d0942163b6fa240d780a53eb590d894d46c9e1f2`)
- Service declared: yes
- Route/ingress declared: not declared in helmrelease.yaml

## Files
- `helmrelease.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/media/tdarr/node-cpu
kubectl -n media get helmrelease tdarr-node-cpu
kubectl -n media get pods -l app.kubernetes.io/instance=tdarr-node-cpu
```

## Reconcile
```sh
flux -n media reconcile helmrelease tdarr-node-cpu
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
