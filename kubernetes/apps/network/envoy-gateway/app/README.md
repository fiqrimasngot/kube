# Envoy Gateway

GitOps deployment notes for `envoy-gateway` in the `network` namespace.

## Context
- Deployment path: `kubernetes/apps/network/envoy-gateway/app`
- HelmRelease: `kubernetes/apps/network/envoy-gateway/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/network/envoy-gateway/app/kustomization.yaml`
- Chart/reference: `envoy-gateway`
- Reconcile interval: `1h`
- Timeout: `not specified`

## Runtime
- Images: managed by the referenced chart or not pinned in this file.
- Service declared: not declared in helmrelease.yaml
- Route/ingress declared: not declared in helmrelease.yaml

## Files
- `./certificate.yaml`
- `./envoy.yaml`
- `./helmrelease.yaml`
- `./ocirepository.yaml`
- `./podmonitor.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/network/envoy-gateway/app
kubectl -n network get helmrelease envoy-gateway
kubectl -n network get pods -l app.kubernetes.io/instance=envoy-gateway
```

## Reconcile
```sh
flux -n network reconcile helmrelease envoy-gateway
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
