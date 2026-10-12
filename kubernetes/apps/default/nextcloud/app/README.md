# Nextcloud

GitOps deployment notes for `nextcloud` in the `default` namespace.

## Context
- Deployment path: `kubernetes/apps/default/nextcloud/app`
- HelmRelease: `kubernetes/apps/default/nextcloud/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/default/nextcloud/app/kustomization.yaml`
- Chart/reference: `spec:`
- Reconcile interval: `1h`
- Timeout: `60m`

## Runtime
- Images:
  - `public.ecr.aws/docker/library/nextcloud`
- Service declared: not declared in helmrelease.yaml
- Route/ingress declared: yes
- Encrypted secret manifests: `secrets.sops.yaml`

## Files
- `./helmrelease.yaml`
- `./secrets.sops.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/default/nextcloud/app
kubectl -n default get helmrelease nextcloud
kubectl -n default get pods -l app.kubernetes.io/instance=nextcloud
```

## Reconcile
```sh
flux -n default reconcile helmrelease nextcloud
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
