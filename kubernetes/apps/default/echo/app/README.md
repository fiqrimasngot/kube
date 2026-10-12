# Echo

GitOps deployment notes for `echo` in the `default` namespace.

## Context
- Deployment path: `kubernetes/apps/default/echo/app`
- HelmRelease: `kubernetes/apps/default/echo/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/default/echo/app/kustomization.yaml`
- Chart/reference: `echo`
- Reconcile interval: `1h`
- Timeout: `not specified`

## Runtime
- Images: managed by the referenced chart or not pinned in this file.
- Service declared: not declared in helmrelease.yaml
- Route/ingress declared: yes

## Files
- `./helmrelease.yaml`
- `./ocirepository.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/default/echo/app
kubectl -n default get helmrelease echo
kubectl -n default get pods -l app.kubernetes.io/instance=echo
```

## Reconcile
```sh
flux -n default reconcile helmrelease echo
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
