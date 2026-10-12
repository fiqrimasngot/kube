# cilium deployment

GitOps deployment README for `kubernetes/apps/kube-system/cilium/app/helmrelease.yaml`.

## Summary
- Namespace: `kube-system`
- HelmRelease: `cilium`
- Path: `kubernetes/apps/kube-system/cilium/app`
- Kustomization: `kubernetes/apps/kube-system/cilium/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/kube-system/cilium/ks.yaml`
- Chart: chartRef `OCIRepository/cilium`
- Reconcile interval: `1h`
- Timeout: `not declared`

## Supporting manifests
- `networks.yaml`
- `ocirepository.yaml`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/kube-system/cilium/app >/tmp/cilium-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n kube-system annotate helmrelease cilium reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n kube-system get helmrelease cilium -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n kube-system get pods -l app.kubernetes.io/instance=cilium -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
