# Node Feature Discovery

GitOps deployment notes for `node-feature-discovery` in the `kube-system` namespace.

## Context
- Deployment path: `kubernetes/apps/kube-system/node-feature-discovery/app`
- HelmRelease: `kubernetes/apps/kube-system/node-feature-discovery/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/kube-system/node-feature-discovery/app/kustomization.yaml`
- Chart/reference: `spec:`
- Reconcile interval: `1h`
- Timeout: `not specified`

## Runtime
- Images: managed by the referenced chart or not pinned in this file.
- Service declared: not declared in helmrelease.yaml
- Route/ingress declared: not declared in helmrelease.yaml

## Files
- `./helmrelease.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/kube-system/node-feature-discovery/app
kubectl -n kube-system get helmrelease node-feature-discovery
kubectl -n kube-system get pods -l app.kubernetes.io/instance=node-feature-discovery
```

## Reconcile
```sh
flux -n kube-system reconcile helmrelease node-feature-discovery
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
