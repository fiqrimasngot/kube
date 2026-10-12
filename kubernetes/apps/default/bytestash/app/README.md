# Bytestash

GitOps deployment notes for `bytestash` in the `default` namespace.

## Context
- Deployment path: `kubernetes/apps/default/bytestash/app`
- HelmRelease: `kubernetes/apps/default/bytestash/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/default/bytestash/app/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `30m`
- Timeout: `not specified`
- Controllers: `bytestash`, `app`

## Runtime
- Images:
  - `ghcr.io/jordan-dalby/bytestash` (`1.5.9@sha256:9c17b5510ca45c976fe23b0d4705ad416aa58d4bf756a70e03ef1f08cf7801fd`)
- Service declared: yes
- Route/ingress declared: yes
- Encrypted secret manifests: `secrets.sops.yaml`

## Files
- `./helmrelease.yaml`
- `./secrets.sops.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/default/bytestash/app
kubectl -n default get helmrelease bytestash
kubectl -n default get pods -l app.kubernetes.io/instance=bytestash
```

## Reconcile
```sh
flux -n default reconcile helmrelease bytestash
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
