# rook-ceph-cluster deployment

GitOps deployment README for `kubernetes/apps/rook-ceph/rook-ceph/cluster/helmrelease.yaml`.

## Summary
- Namespace: `rook-ceph`
- HelmRelease: `rook-ceph-cluster`
- Path: `kubernetes/apps/rook-ceph/rook-ceph/cluster`
- Kustomization: `kubernetes/apps/rook-ceph/rook-ceph/cluster/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/rook-ceph/rook-ceph/ks.yaml`
- Chart: chartRef `OCIRepository/rook-ceph-cluster`
- Reconcile interval: `1h`
- Timeout: `not declared`

## Supporting manifests
- `prometheusrule.yaml`

## Routes
- `dashboard`: hosts `none declared`, gateways `envoy-internal`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/rook-ceph/rook-ceph/cluster >/tmp/rook-ceph-cluster-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n rook-ceph annotate helmrelease rook-ceph-cluster reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n rook-ceph get helmrelease rook-ceph-cluster -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n rook-ceph get pods -l app.kubernetes.io/instance=rook-ceph-cluster -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
