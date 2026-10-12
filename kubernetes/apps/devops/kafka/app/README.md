# Kafka

GitOps deployment notes for `strimzi` in the `devops` namespace.

## Context
- Deployment path: `kubernetes/apps/devops/kafka/app`
- HelmRelease: `kubernetes/apps/devops/kafka/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/devops/kafka/app/kustomization.yaml`
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
kubectl kustomize kubernetes/apps/devops/kafka/app
kubectl -n devops get helmrelease strimzi
kubectl -n devops get pods -l app.kubernetes.io/instance=strimzi
```

## Reconcile
```sh
flux -n devops reconcile helmrelease strimzi
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
