# K8s Gateway

GitOps deployment notes for `k8s-gateway` in the `network` namespace.

## Context
- Deployment path: `kubernetes/apps/network/k8s-gateway/app`
- HelmRelease: `kubernetes/apps/network/k8s-gateway/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/network/k8s-gateway/app/kustomization.yaml`
- Chart/reference: `k8s-gateway`
- Reconcile interval: `1h`
- Timeout: `not specified`

## Runtime
- Images: managed by the referenced chart or not pinned in this file.
- Service declared: yes
- Route/ingress declared: yes

## Files
- `./helmrelease.yaml`
- `./ocirepository.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/network/k8s-gateway/app
kubectl -n network get helmrelease k8s-gateway
kubectl -n network get pods -l app.kubernetes.io/instance=k8s-gateway
```

## Reconcile
```sh
flux -n network reconcile helmrelease k8s-gateway
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
