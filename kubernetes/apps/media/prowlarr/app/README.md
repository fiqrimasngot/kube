# prowlarr deployment

GitOps deployment README for `kubernetes/apps/media/prowlarr/app/helmrelease.yaml`.

## Summary
- Namespace: `media`
- HelmRelease: `prowlarr`
- Path: `kubernetes/apps/media/prowlarr/app`
- Kustomization: `kubernetes/apps/media/prowlarr/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/media/prowlarr/ks.yaml`
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `30m`
- Timeout: `not declared`

## Controllers and images
- `prowlarr`: type `Deployment`
  - container `app` image `ghcr.io/home-operations/prowlarr:2.4.0.5397@sha256:8a140c9104c754a272f5e0d1dfcb32a06f07946a431a45c1083a16344f531748`

## Services
- `app`: http:80

## Routes
- `app`: hosts `{{ .Release.Name }}.${SECRET_DOMAIN}`, gateways `envoy-internal`

## Persistence
- `config`: existingClaim=`prowlarr`
- `tmp`: type=`emptyDir`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/media/prowlarr/app >/tmp/prowlarr-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media annotate helmrelease prowlarr reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media get helmrelease prowlarr -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media get pods -l app.kubernetes.io/instance=prowlarr -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
