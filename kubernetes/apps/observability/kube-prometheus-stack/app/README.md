# kube-prometheus-stack deployment

GitOps deployment README for `kubernetes/apps/observability/kube-prometheus-stack/app/helmrelease.yaml`.

## Summary
- Namespace: `observability`
- HelmRelease: `kube-prometheus-stack`
- Path: `kubernetes/apps/observability/kube-prometheus-stack/app`
- Kustomization: `kubernetes/apps/observability/kube-prometheus-stack/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/observability/kube-prometheus-stack/ks.yaml`
- Chart: chart `kube-prometheus-stack` from `HelmRepository/prometheus-community` version `80.14.4`
- Reconcile interval: `30m`
- Timeout: `not declared`

## Secret manifests
Secret manifest filenames only; do not put decrypted values in this README.
- `secrets.sops.yaml`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/observability/kube-prometheus-stack/app >/tmp/kube-prometheus-stack-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n observability annotate helmrelease kube-prometheus-stack reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n observability get helmrelease kube-prometheus-stack -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n observability get pods -l app.kubernetes.io/instance=kube-prometheus-stack -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
