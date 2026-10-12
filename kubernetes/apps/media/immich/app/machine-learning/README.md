# Immich — Machine Learning

GitOps deployment notes for `immich-machine-learning` in the `media` namespace.

## Context
- Deployment path: `kubernetes/apps/media/immich/app/machine-learning`
- HelmRelease: `kubernetes/apps/media/immich/app/machine-learning/helmrelease.yaml`
- Kustomization: `kubernetes/apps/media/immich/app/machine-learning/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `30m`
- Timeout: `not specified`
- Controllers: `library`

## Runtime
- Images:
  - `ghcr.io/immich-app/immich-machine-learning` (`v2.7.5`)
- Service declared: yes
- Route/ingress declared: not declared in helmrelease.yaml

## Files
- `./helmrelease.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/media/immich/app/machine-learning
kubectl -n media get helmrelease immich-machine-learning
kubectl -n media get pods -l app.kubernetes.io/instance=immich-machine-learning
```

## Reconcile
```sh
flux -n media reconcile helmrelease immich-machine-learning
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
