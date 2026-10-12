# cert-manager deployment

GitOps deployment README for `kubernetes/apps/cert-manager/cert-manager/app/helmrelease.yaml`.

## Summary
- Namespace: `cert-manager`
- HelmRelease: `cert-manager`
- Path: `kubernetes/apps/cert-manager/cert-manager/app`
- Kustomization: `kubernetes/apps/cert-manager/cert-manager/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/cert-manager/cert-manager/ks.yaml`
- Chart: chartRef `OCIRepository/cert-manager`
- Reconcile interval: `1h`
- Timeout: `not declared`

## Secret manifests
Secret manifest filenames only; do not put decrypted values in this README.
- `secret.sops.yaml`

## Supporting manifests
- `clusterissuer.yaml`
- `ocirepository.yaml`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/cert-manager/cert-manager/app >/tmp/cert-manager-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n cert-manager annotate helmrelease cert-manager reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n cert-manager get helmrelease cert-manager -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n cert-manager get pods -l app.kubernetes.io/instance=cert-manager -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
