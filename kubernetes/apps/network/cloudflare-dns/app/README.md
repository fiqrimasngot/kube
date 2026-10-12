# cloudflare-dns deployment

GitOps deployment README for `kubernetes/apps/network/cloudflare-dns/app/helmrelease.yaml`.

## Summary
- Namespace: `network`
- HelmRelease: `cloudflare-dns`
- Path: `kubernetes/apps/network/cloudflare-dns/app`
- Kustomization: `kubernetes/apps/network/cloudflare-dns/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/network/cloudflare-dns/ks.yaml`
- Chart: chartRef `OCIRepository/cloudflare-dns`
- Reconcile interval: `1h`
- Timeout: `not declared`

## Secret manifests
Secret manifest filenames only; do not put decrypted values in this README.
- `secret.sops.yaml`

## Supporting manifests
- `ocirepository.yaml`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/network/cloudflare-dns/app >/tmp/cloudflare-dns-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n network annotate helmrelease cloudflare-dns reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n network get helmrelease cloudflare-dns -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n network get pods -l app.kubernetes.io/instance=cloudflare-dns -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
