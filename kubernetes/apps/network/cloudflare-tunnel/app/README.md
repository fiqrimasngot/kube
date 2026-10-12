# cloudflare-tunnel deployment

GitOps deployment README for `kubernetes/apps/network/cloudflare-tunnel/app/helmrelease.yaml`.

## Summary
- Namespace: `network`
- HelmRelease: `cloudflare-tunnel`
- Path: `kubernetes/apps/network/cloudflare-tunnel/app`
- Kustomization: `kubernetes/apps/network/cloudflare-tunnel/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/network/cloudflare-tunnel/ks.yaml`
- Chart: chartRef `OCIRepository/cloudflare-tunnel`
- Reconcile interval: `1h`
- Timeout: `not declared`

## Secret manifests
Secret manifest filenames only; do not put decrypted values in this README.
- `secret.sops.yaml`

## Supporting manifests
- `dnsendpoint.yaml`
- `ocirepository.yaml`

## Controllers and images
- `cloudflare-tunnel`: type `Deployment`
  - container `app` image `docker.io/cloudflare/cloudflared:2026.9.1`

## Services
- `app`: http:8080

## Persistence
- `config-file`: type=`configMap`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/network/cloudflare-tunnel/app >/tmp/cloudflare-tunnel-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n network annotate helmrelease cloudflare-tunnel reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n network get helmrelease cloudflare-tunnel -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n network get pods -l app.kubernetes.io/instance=cloudflare-tunnel -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
