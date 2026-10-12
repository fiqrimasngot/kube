# Coredns

GitOps deployment notes for `coredns` in the `kube-system` namespace.

## Context
- Deployment path: `kubernetes/apps/kube-system/coredns/app`
- HelmRelease: `kubernetes/apps/kube-system/coredns/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/kube-system/coredns/app/kustomization.yaml`
- Chart/reference: `coredns`
- Reconcile interval: `1h`
- Timeout: `not specified`

## Runtime
- Images:
  - `mirror.gcr.io/coredns/coredns`
- Service declared: yes
- Route/ingress declared: not declared in helmrelease.yaml

## Files
- `./helmrelease.yaml`
- `./ocirepository.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/kube-system/coredns/app
kubectl -n kube-system get helmrelease coredns
kubectl -n kube-system get pods -l app.kubernetes.io/instance=coredns
```

## Reconcile
```sh
flux -n kube-system reconcile helmrelease coredns
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
