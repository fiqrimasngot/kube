# garage deployment

GitOps deployment README for `kubernetes/apps/storage/garage/app/helmrelease.yaml`.

## Summary
- Namespace: `storage`
- HelmRelease: `garage`
- Path: `kubernetes/apps/storage/garage/app`
- Kustomization: `kubernetes/apps/storage/garage/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/storage/garage/ks.yaml`
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `30m`
- Timeout: `15m`

## Secret manifests
Secret manifest filenames only; do not put decrypted values in this README.
- `secret.sops.yaml`

## Controllers and images
- `garage`: type `Deployment`
  - container `app` image `mirror.gcr.io/dxflrs/garage:v2.4.1@sha256:9c96caa2612d3411acc5b0e6701fb238dbfba33e533a6d7d3d811a4b12d0d020`

## Services
- `app`: s3:3900, rpc:3901, web:3902, admin:3903

## Persistence
- `config`: type=`configMap`
- `secrets`: type=`secret`
- `data`: enabled=`True`, existingClaim=`backups`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/storage/garage/app >/tmp/garage-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n storage annotate helmrelease garage reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n storage get helmrelease garage -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n storage get pods -l app.kubernetes.io/instance=garage -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
