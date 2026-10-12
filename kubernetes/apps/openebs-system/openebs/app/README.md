# Openebs

GitOps deployment notes for `openebs` in the `openebs-system` namespace.

## Context
- Deployment path: `kubernetes/apps/openebs-system/openebs/app`
- HelmRelease: `kubernetes/apps/openebs-system/openebs/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/openebs-system/openebs/app/kustomization.yaml`
- Chart/reference: `openebs`
- Reconcile interval: `1h`
- Timeout: `2m`

## Runtime
- Images:
  - `ghcr.io/kiwigrid/k8s-sidecar` (`4.4.0`)
- Service declared: not declared in helmrelease.yaml
- Route/ingress declared: not declared in helmrelease.yaml

## Files
- `./helmrelease.yaml`
- `./storageclass.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/openebs-system/openebs/app
kubectl -n openebs-system get helmrelease openebs
kubectl -n openebs-system get pods -l app.kubernetes.io/instance=openebs
```

## Reconcile
```sh
flux -n openebs-system reconcile helmrelease openebs
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
