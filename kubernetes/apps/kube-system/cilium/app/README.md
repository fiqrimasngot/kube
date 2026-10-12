# Cilium

GitOps deployment notes for `cilium` in the `kube-system` namespace.

## Context
- Deployment path: `kubernetes/apps/kube-system/cilium/app`
- HelmRelease: `kubernetes/apps/kube-system/cilium/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/kube-system/cilium/app/kustomization.yaml`
- Chart/reference: `cilium`
- Reconcile interval: `1h`
- Timeout: `not specified`

## Runtime
- Images: managed by the referenced chart or not pinned in this file.
- Service declared: not declared in helmrelease.yaml
- Route/ingress declared: not declared in helmrelease.yaml

## Files
- `./helmrelease.yaml`
- `./ocirepository.yaml`
- `./networks.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/kube-system/cilium/app
kubectl -n kube-system get helmrelease cilium
kubectl -n kube-system get pods -l app.kubernetes.io/instance=cilium
```

## Reconcile
```sh
flux -n kube-system reconcile helmrelease cilium
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
