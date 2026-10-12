# Kiwix

GitOps deployment notes for `kiwix` in the `default` namespace.

## Context
- Deployment path: `kubernetes/apps/default/kiwix/app`
- HelmRelease: `kubernetes/apps/default/kiwix/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/default/kiwix/app/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `30m`
- Timeout: `not specified`
- Controllers: `main`

## Runtime
- Images:
  - `ghcr.io/kiwix/kiwix-serve` (`latest`)
- Service declared: yes
- Route/ingress declared: yes

## Files
- `./helmrelease.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/default/kiwix/app
kubectl -n default get helmrelease kiwix
kubectl -n default get pods -l app.kubernetes.io/instance=kiwix
```

## Reconcile
```sh
flux -n default reconcile helmrelease kiwix
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
