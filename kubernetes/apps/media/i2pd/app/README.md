# I2pd

GitOps deployment notes for `i2pd` in the `media` namespace.

## Context
- Deployment path: `kubernetes/apps/media/i2pd/app`
- HelmRelease: `kubernetes/apps/media/i2pd/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/media/i2pd/app/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `30m`
- Timeout: `not specified`
- Controllers: `i2pd`

## Runtime
- Images:
  - `registry.skysolutions.fi/docker.io/purplei2p/i2pd` (`release-2.50.0`)
- Service declared: yes
- Route/ingress declared: yes

## Files
- `./helmrelease.yaml`
- `name: i2pd`
- `config/i2pd-docker.conf`

## Validate
```sh
kubectl kustomize kubernetes/apps/media/i2pd/app
kubectl -n media get helmrelease i2pd
kubectl -n media get pods -l app.kubernetes.io/instance=i2pd
```

## Reconcile
```sh
flux -n media reconcile helmrelease i2pd
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
