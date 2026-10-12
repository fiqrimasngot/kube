# coredns deployment

GitOps deployment README for `kubernetes/apps/kube-system/coredns/app/helmrelease.yaml`.

## Summary
- Namespace: `kube-system`
- HelmRelease: `coredns`
- Path: `kubernetes/apps/kube-system/coredns/app`
- Kustomization: `kubernetes/apps/kube-system/coredns/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/kube-system/coredns/ks.yaml`
- Chart: chartRef `OCIRepository/coredns`
- Reconcile interval: `1h`
- Timeout: `not declared`

## Supporting manifests
- `ocirepository.yaml`

## Services
- `name`
- `clusterIP`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/kube-system/coredns/app >/tmp/coredns-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n kube-system annotate helmrelease coredns reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n kube-system get helmrelease coredns -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n kube-system get pods -l app.kubernetes.io/instance=coredns -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
