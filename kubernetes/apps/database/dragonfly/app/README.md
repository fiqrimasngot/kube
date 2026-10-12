# Dragonfly

GitOps deployment notes for `dragonfly-operator` in the `database` namespace.

## Context
- Deployment path: `kubernetes/apps/database/dragonfly/app`
- HelmRelease: `kubernetes/apps/database/dragonfly/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/database/dragonfly/app/kustomization.yaml`
- Chart/reference: `dragonfly-operator`
- Reconcile interval: `5m`
- Timeout: `not specified`

## Runtime
- Images:
  - `ghcr.io/dragonflydb/operator` (`4.6.2`)
- Service declared: yes
- Route/ingress declared: not declared in helmrelease.yaml

## Files
- `https://raw.githubusercontent.com/dragonflydb/dragonfly-operator/v1.1.6/manifests/crd.yaml`
- `./helmrelease.yaml`
- `./rbac.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/database/dragonfly/app
kubectl -n database get helmrelease dragonfly-operator
kubectl -n database get pods -l app.kubernetes.io/instance=dragonfly-operator
```

## Reconcile
```sh
flux -n database reconcile helmrelease dragonfly-operator
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
