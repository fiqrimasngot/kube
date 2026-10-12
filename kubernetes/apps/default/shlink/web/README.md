# shlink-web deployment

GitOps deployment README for `kubernetes/apps/default/shlink/web/helmrelease.yaml`.

## Summary
- Namespace: `default`
- HelmRelease: `shlink-web`
- Path: `kubernetes/apps/default/shlink/web`
- Kustomization: `kubernetes/apps/default/shlink/web/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/default/shlink/ks.yaml`
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `30m`
- Timeout: `not declared`

## Secret manifests
Secret manifest filenames only; do not put decrypted values in this README.
- `secrets.sops.yaml`

## Controllers and images
- `shlink-web`: type `Deployment`
  - container `app` image `ghcr.io/shlinkio/shlink-web-client:4.6.2`

## Services
- `app`: http:8080

## Routes
- `main`: hosts `{{ .Release.Name }}.${SECRET_DOMAIN}`, gateways `envoy-external`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/default/shlink/web >/tmp/shlink-web-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default annotate helmrelease shlink-web reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default get helmrelease shlink-web -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default get pods -l app.kubernetes.io/instance=shlink-web -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
