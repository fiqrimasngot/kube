# volsync deployment

GitOps deployment README for `kubernetes/apps/volsync-system/volsync/app/helmrelease.yaml`.

## Summary
- Namespace: `volsync-system`
- HelmRelease: `volsync`
- Path: `kubernetes/apps/volsync-system/volsync/app`
- Kustomization: `kubernetes/apps/volsync-system/volsync/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/volsync-system/volsync/ks.yaml`
- Chart: chartRef `OCIRepository/volsync`
- Reconcile interval: `1h`
- Timeout: `not declared`

## Supporting manifests
- `prometheusrule.yaml`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/volsync-system/volsync/app >/tmp/volsync-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n volsync-system annotate helmrelease volsync reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n volsync-system get helmrelease volsync -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n volsync-system get pods -l app.kubernetes.io/instance=volsync -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
