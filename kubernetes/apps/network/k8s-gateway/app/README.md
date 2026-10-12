# k8s-gateway deployment

GitOps deployment README for `kubernetes/apps/network/k8s-gateway/app/helmrelease.yaml`.

## Summary
- Namespace: `network`
- HelmRelease: `k8s-gateway`
- Path: `kubernetes/apps/network/k8s-gateway/app`
- Kustomization: `kubernetes/apps/network/k8s-gateway/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/network/k8s-gateway/ks.yaml`
- Chart: chartRef `OCIRepository/k8s-gateway`
- Reconcile interval: `1h`
- Timeout: `not declared`

## Supporting manifests
- `ocirepository.yaml`

## Services
- `type`
- `port`
- `annotations`
- `externalTrafficPolicy`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/network/k8s-gateway/app >/tmp/k8s-gateway-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n network annotate helmrelease k8s-gateway reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n network get helmrelease k8s-gateway -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n network get pods -l app.kubernetes.io/instance=k8s-gateway -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
