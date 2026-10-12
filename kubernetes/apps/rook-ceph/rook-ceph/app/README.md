# rook-ceph deployment

GitOps deployment README for `kubernetes/apps/rook-ceph/rook-ceph/app/helmrelease.yaml`.

## Summary
- Namespace: `rook-ceph`
- HelmRelease: `rook-ceph`
- Path: `kubernetes/apps/rook-ceph/rook-ceph/app`
- Kustomization: `kubernetes/apps/rook-ceph/rook-ceph/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/rook-ceph/rook-ceph/ks.yaml`
- Chart: chartRef `OCIRepository/rook-ceph`
- Reconcile interval: `1h`
- Timeout: `not declared`

## Secret manifests
Secret manifest filenames only; do not put decrypted values in this README.
- `secret.sops.yaml`

## Supporting manifests
- `grafanadashboard.yaml`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/rook-ceph/rook-ceph/app >/tmp/rook-ceph-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n rook-ceph annotate helmrelease rook-ceph reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n rook-ceph get helmrelease rook-ceph -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n rook-ceph get pods -l app.kubernetes.io/instance=rook-ceph -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
