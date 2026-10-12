# Homepage

GitOps deployment notes for `homepage` in the `default` namespace.

## Context
- Deployment path: `kubernetes/apps/default/homepage/app`
- HelmRelease: `kubernetes/apps/default/homepage/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/default/homepage/app/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `30m`
- Timeout: `not specified`
- Controllers: `config`

## Runtime
- Images:
  - `ghcr.io/gethomepage/homepage` (`v1.8.0@sha256:7dc099d5c6ec7fc945d858218565925b01ff8a60bcbfda990fc680a8b5cd0b6e`)
- Service declared: yes
- Route/ingress declared: yes

## Files
- `./helmrelease.yaml`
- `name: homepage-config`
- `config/bookmarks.yaml`
- `config/services.yaml`
- `config/kubernetes.yaml`
- `config/settings.yaml`
- `config/widgets.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/default/homepage/app
kubectl -n default get helmrelease homepage
kubectl -n default get pods -l app.kubernetes.io/instance=homepage
```

## Reconcile
```sh
flux -n default reconcile helmrelease homepage
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
