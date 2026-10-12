# flux-instance deployment

GitOps deployment README for `kubernetes/apps/flux-system/flux-instance/app/helmrelease.yaml`.

## Summary
- Namespace: `flux-system`
- HelmRelease: `flux-instance`
- Path: `kubernetes/apps/flux-system/flux-instance/app`
- Kustomization: `kubernetes/apps/flux-system/flux-instance/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/flux-system/flux-instance/ks.yaml`
- Chart: chartRef `OCIRepository/flux-instance`
- Reconcile interval: `1h`
- Timeout: `not declared`

## Secret manifests
Secret manifest filenames only; do not put decrypted values in this README.
- `secret.sops.yaml`

## Supporting manifests
- `httproute.yaml`
- `ocirepository.yaml`
- `receiver.yaml`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/flux-system/flux-instance/app >/tmp/flux-instance-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n flux-system annotate helmrelease flux-instance reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n flux-system get helmrelease flux-instance -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n flux-system get pods -l app.kubernetes.io/instance=flux-instance -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
