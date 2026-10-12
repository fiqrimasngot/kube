# Kube Prometheus Stack

GitOps deployment notes for `kube-prometheus-stack` in the `observability` namespace.

## Context
- Deployment path: `kubernetes/apps/observability/kube-prometheus-stack/app`
- HelmRelease: `kubernetes/apps/observability/kube-prometheus-stack/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/observability/kube-prometheus-stack/app/kustomization.yaml`
- Chart/reference: `spec:`
- Reconcile interval: `30m`
- Timeout: `60`
- Controllers: `deploymentStrategy`

## Runtime
- Images: managed by the referenced chart or not pinned in this file.
- Service declared: yes
- Route/ingress declared: yes
- Encrypted secret manifests: `secrets.sops.yaml`

## Files
- `./helmrelease.yaml`
- `./secrets.sops.yaml`
- `./grafana-dashboard`

## Validate
```sh
kubectl kustomize kubernetes/apps/observability/kube-prometheus-stack/app
kubectl -n observability get helmrelease kube-prometheus-stack
kubectl -n observability get pods -l app.kubernetes.io/instance=kube-prometheus-stack
```

## Reconcile
```sh
flux -n observability reconcile helmrelease kube-prometheus-stack
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
