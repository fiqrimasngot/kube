# csi-driver-nfs deployment

GitOps deployment README for `kubernetes/apps/storage/csi-driver-nfs/app/helmrelease.yaml`.

## Summary
- Namespace: `storage`
- HelmRelease: `csi-driver-nfs`
- Path: `kubernetes/apps/storage/csi-driver-nfs/app`
- Kustomization: `kubernetes/apps/storage/csi-driver-nfs/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/storage/csi-driver-nfs/ks.yaml`
- Chart: chart `csi-driver-nfs` from `HelmRepository/csi-driver-nfs` version `4.12.1`
- Reconcile interval: `30m`
- Timeout: `not declared`

## Supporting manifests
- `storageclass.yaml`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/storage/csi-driver-nfs/app >/tmp/csi-driver-nfs-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n storage annotate helmrelease csi-driver-nfs reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n storage get helmrelease csi-driver-nfs -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n storage get pods -l app.kubernetes.io/instance=csi-driver-nfs -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
