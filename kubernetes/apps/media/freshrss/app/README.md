# Freshrss

GitOps deployment notes for `freshrss` in the `media` namespace.

## Context
- Deployment path: `kubernetes/apps/media/freshrss/app`
- HelmRelease: `kubernetes/apps/media/freshrss/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/media/freshrss/app/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `30m`
- Timeout: `not specified`
- Controllers: `freshrss`

## Runtime
- Images:
  - `freshrss/freshrss` (`1.30.0@sha256:258b8edfc8a76a61f60d2d6a14d8f8d12495d78abf38646a2137612dfa264a21`)
- Service declared: yes
- Route/ingress declared: yes

## Files
- `./helmrelease.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/media/freshrss/app
kubectl -n media get helmrelease freshrss
kubectl -n media get pods -l app.kubernetes.io/instance=freshrss
```

## Reconcile
```sh
flux -n media reconcile helmrelease freshrss
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
