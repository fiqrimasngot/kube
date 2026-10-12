# Garage — UI

GitOps deployment notes for `garage-webui` in the `storage` namespace.

## Context
- Deployment path: `kubernetes/apps/storage/garage/ui`
- HelmRelease: `kubernetes/apps/storage/garage/ui/helmrelease.yaml`
- Kustomization: `kubernetes/apps/storage/garage/ui/kustomization.yaml`
- Chart/reference: `app-template`
- Reconcile interval: `1h`
- Timeout: `not specified`
- Controllers: `garage-webui`, `app`, `config`

## Runtime
- Images:
  - `docker.io/khairul169/garage-webui` (`1.1.0@sha256:17c793551873155065bf9a022dabcde874de808a1f26e648d4b82e168806439c`)
- Service declared: yes
- Route/ingress declared: yes

## Files
- `./helmrelease.yaml`

## Validate
```sh
kubectl kustomize kubernetes/apps/storage/garage/ui
kubectl -n storage get helmrelease garage-webui
kubectl -n storage get pods -l app.kubernetes.io/instance=garage-webui
```

## Reconcile
```sh
flux -n storage reconcile helmrelease garage-webui
```

## Notes
- Do not print decrypted Secret values while troubleshooting.
- Persist runtime fixes in Git; live patches alone will drift on the next reconcile.
