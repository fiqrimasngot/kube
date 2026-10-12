# immich-machine-learning deployment

GitOps deployment README for `kubernetes/apps/media/immich/app/machine-learning/helmrelease.yaml`.

## Summary
- Namespace: `media`
- HelmRelease: `immich-machine-learning`
- Path: `kubernetes/apps/media/immich/app/machine-learning`
- Kustomization: `kubernetes/apps/media/immich/app/machine-learning/kustomization.yaml`
- Flux app Kustomization: not found at app root
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `30m`
- Timeout: `not declared`

## Controllers and images
- `immich-machine-learning`: type `Deployment`
  - container `main` image `ghcr.io/immich-app/immich-machine-learning:v2.7.5`

## Services
- `main`: http:3003

## Persistence
- `library`: type=`nfs`, path=`/immich`
- `cache`: enabled=`True`, type=`emptyDir`
- `geocoding-dump`: enabled=`True`, type=`emptyDir`
- `transformers-cache`: enabled=`True`, type=`emptyDir`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/media/immich/app/machine-learning >/tmp/immich-machine-learning-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media annotate helmrelease immich-machine-learning reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media get helmrelease immich-machine-learning -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media get pods -l app.kubernetes.io/instance=immich-machine-learning -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
