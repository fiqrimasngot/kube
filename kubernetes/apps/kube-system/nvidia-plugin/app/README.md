# nvidia-device-plugin deployment

GitOps deployment README for `kubernetes/apps/kube-system/nvidia-plugin/app/helmrelease.yaml`.

## Summary
- Namespace: `kube-system`
- HelmRelease: `nvidia-device-plugin`
- Path: `kubernetes/apps/kube-system/nvidia-plugin/app`
- Kustomization: `kubernetes/apps/kube-system/nvidia-plugin/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/kube-system/nvidia-plugin/ks.yaml`
- Chart: chart `nvidia-device-plugin` from `HelmRepository/nvidia-dvp` version `0.18.0`
- Reconcile interval: `15m`
- Timeout: `not declared`

## Supporting manifests
- `class.yaml`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/kube-system/nvidia-plugin/app >/tmp/nvidia-device-plugin-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n kube-system annotate helmrelease nvidia-device-plugin reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n kube-system get helmrelease nvidia-device-plugin -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n kube-system get pods -l app.kubernetes.io/instance=nvidia-device-plugin -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
