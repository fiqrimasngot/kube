# envoy-gateway deployment

GitOps deployment README for `kubernetes/apps/network/envoy-gateway/app/helmrelease.yaml`.

## Summary
- Namespace: `network`
- HelmRelease: `envoy-gateway`
- Path: `kubernetes/apps/network/envoy-gateway/app`
- Kustomization: `kubernetes/apps/network/envoy-gateway/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/network/envoy-gateway/ks.yaml`
- Chart: chartRef `OCIRepository/envoy-gateway`
- Reconcile interval: `1h`
- Timeout: `not declared`

## Supporting manifests
- `certificate.yaml`
- `envoy.yaml`
- `ocirepository.yaml`
- `podmonitor.yaml`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/network/envoy-gateway/app >/tmp/envoy-gateway-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n network annotate helmrelease envoy-gateway reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n network get helmrelease envoy-gateway -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n network get pods -l app.kubernetes.io/instance=envoy-gateway -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
