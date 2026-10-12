# jellyseerr deployment

GitOps deployment README for `kubernetes/apps/media/jellyseerr/app/helmrelease.yaml`.

## Summary
- Namespace: `media`
- HelmRelease: `jellyseerr`
- Path: `kubernetes/apps/media/jellyseerr/app`
- Kustomization: `kubernetes/apps/media/jellyseerr/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/media/jellyseerr/ks.yaml`
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `30m`
- Timeout: `not declared`

## Controllers and images
- `jellyseerr`: type `Deployment`
  - container `app` image `fallenbagel/jellyseerr:2.7.3`

## Services
- `app`: http:5055

## Routes
- `app`: hosts `request.${SECRET_DOMAIN}`, gateways `envoy-external`

## Persistence
- `config`: existingClaim=`jellyseerr`
- `tmpfs`: type=`emptyDir`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/media/jellyseerr/app >/tmp/jellyseerr-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media annotate helmrelease jellyseerr reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media get helmrelease jellyseerr -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media get pods -l app.kubernetes.io/instance=jellyseerr -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
