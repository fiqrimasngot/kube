# Samba

GitOps deployment notes for `samba` in the `storage` namespace.

## Context
- Deployment path: `kubernetes/apps/storage/samba/app`
- HelmRelease: `kubernetes/apps/storage/samba/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/storage/samba/app/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `1h`
- Timeout: `15m`
- Controllers: `config`, `time-machine`, `camera`

## Runtime
- Images:
  - `ghcr.io/crazy-max/samba` (`4.21.4@sha256:75f5037770eab774b82f298268305af8a18a01a1daad679f8d2d17c54059c847`)
- Service declared: yes
- Route/ingress declared: not declared in helmrelease.yaml

## Files
- `./helmrelease.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/storage/samba/app
kubectl -n storage get helmrelease samba
kubectl -n storage get pods -l app.kubernetes.io/instance=samba
```

## Reconcile
```sh
flux -n storage reconcile helmrelease samba
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
