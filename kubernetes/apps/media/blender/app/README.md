# Blender

GitOps deployment notes for `blender` in the `media` namespace.

## Context
- Deployment path: `kubernetes/apps/media/blender/app`
- HelmRelease: `kubernetes/apps/media/blender/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/media/blender/app/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `30m`
- Timeout: `not specified`

## Runtime
- Images:
  - `lscr.io/linuxserver/blender` (`latest`)
- Service declared: yes
- Route/ingress declared: yes

## Files
- `./helmrelease.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/media/blender/app
kubectl -n media get helmrelease blender
kubectl -n media get pods -l app.kubernetes.io/instance=blender
```

## Reconcile
```sh
flux -n media reconcile helmrelease blender
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
