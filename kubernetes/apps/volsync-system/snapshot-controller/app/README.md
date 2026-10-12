# snapshot-controller deployment

GitOps deployment README for `kubernetes/apps/volsync-system/snapshot-controller/app/helmrelease.yaml`.

## Summary
- Namespace: `volsync-system`
- HelmRelease: `snapshot-controller`
- Path: `kubernetes/apps/volsync-system/snapshot-controller/app`
- Kustomization: `kubernetes/apps/volsync-system/snapshot-controller/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/volsync-system/snapshot-controller/ks.yaml`
- Chart: chartRef `OCIRepository/snapshot-controller`
- Reconcile interval: `1h`
- Timeout: `not declared`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/volsync-system/snapshot-controller/app >/tmp/snapshot-controller-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n volsync-system annotate helmrelease snapshot-controller reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n volsync-system get helmrelease snapshot-controller -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n volsync-system get pods -l app.kubernetes.io/instance=snapshot-controller -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
