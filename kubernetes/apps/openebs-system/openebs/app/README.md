# openebs deployment

GitOps deployment README for `kubernetes/apps/openebs-system/openebs/app/helmrelease.yaml`.

## Summary
- Namespace: `openebs-system`
- HelmRelease: `openebs`
- Path: `kubernetes/apps/openebs-system/openebs/app`
- Kustomization: `kubernetes/apps/openebs-system/openebs/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/openebs-system/openebs/ks.yaml`
- Chart: chartRef `OCIRepository/openebs`
- Reconcile interval: `1h`
- Timeout: `not declared`

## Supporting manifests
- `snapshotclass.yaml`
- `storageclass.yaml`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/openebs-system/openebs/app >/tmp/openebs-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n openebs-system annotate helmrelease openebs reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n openebs-system get helmrelease openebs -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n openebs-system get pods -l app.kubernetes.io/instance=openebs -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
