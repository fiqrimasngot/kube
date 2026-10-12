# Go2rtc

GitOps deployment notes for `go2rtc` in the `security` namespace.

## Context
- Deployment path: `kubernetes/apps/security/go2rtc/app`
- HelmRelease: `kubernetes/apps/security/go2rtc/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/security/go2rtc/app/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `1h`
- Timeout: `not specified`
- Controllers: `go2rtc`, `app`

## Runtime
- Images:
  - `ghcr.io/alexxit/go2rtc` (`1.9.14@sha256:675c318b23c06fd862a61d262240c9a63436b4050d177ffc68a32710d9e05bae`)
- Service declared: yes
- Route/ingress declared: yes

## Files
- `./helmrelease.yaml`
- `name: go2rtc-config`
- `./resources/go2rtc.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/security/go2rtc/app
kubectl -n security get helmrelease go2rtc
kubectl -n security get pods -l app.kubernetes.io/instance=go2rtc
```

## Reconcile
```sh
flux -n security reconcile helmrelease go2rtc
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
