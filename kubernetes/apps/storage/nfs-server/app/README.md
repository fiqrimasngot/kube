# nfs-server deployment

GitOps deployment README for `kubernetes/apps/storage/nfs-server/app/helmrelease.yaml`.

## Summary
- Namespace: `storage`
- HelmRelease: `nfs-server`
- Path: `kubernetes/apps/storage/nfs-server/app`
- Kustomization: `kubernetes/apps/storage/nfs-server/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/storage/nfs-server/ks.yaml`
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `1h`
- Timeout: `not declared`

## Supporting manifests
- `exports.yaml`
- `pv.yaml`
- `pvc.yaml`

## Controllers and images
- `nfs-server`: type `Deployment`
  - container `nfs-server` image `quay.io/aminvakil/alpine-nfs-server:latest`

## Persistence
- `exports`: type=`configMap`
- `fake-export`: type=`emptyDir`
- `doc`: existingClaim=`doc`
- `immich`: existingClaim=`photos`
- `media`: existingClaim=`media`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/storage/nfs-server/app >/tmp/nfs-server-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n storage annotate helmrelease nfs-server reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n storage get helmrelease nfs-server -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n storage get pods -l app.kubernetes.io/instance=nfs-server -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
