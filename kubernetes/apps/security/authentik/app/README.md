# Authentik

GitOps deployment notes for `authentik` in the `security` namespace.

## Context
- Deployment path: `kubernetes/apps/security/authentik/app`
- HelmRelease: `kubernetes/apps/security/authentik/app/helmrelease.yaml`
- Kustomization: `kubernetes/apps/security/authentik/app/kustomization.yaml`
- Chart/reference: `spec:`
- Reconcile interval: `2h`
- Timeout: `not specified`
- Controllers: `deploymentStrategy`

## Runtime
- Images: managed by the referenced chart or not pinned in this file.
- Service declared: not declared in helmrelease.yaml
- Route/ingress declared: yes

## Files
- `./helmrelease.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/security/authentik/app
kubectl -n security get helmrelease authentik
kubectl -n security get pods -l app.kubernetes.io/instance=authentik
```

## Reconcile
```sh
flux -n security reconcile helmrelease authentik
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
