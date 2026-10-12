# minio deployment

GitOps deployment README for `kubernetes/apps/storage/minio/app/helmrelease.yaml`.

## Summary
- Namespace: `storage`
- HelmRelease: `minio`
- Path: `kubernetes/apps/storage/minio/app`
- Kustomization: `kubernetes/apps/storage/minio/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/storage/minio/ks.yaml`
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `30m`
- Timeout: `15m`

## Secret manifests
Secret manifest filenames only; do not put decrypted values in this README.
- `secret.sops.yaml`

## Controllers and images
- `minio`: type `Deployment`, replicas `0`
  - container `app` image `docker.io/pgsty/silo:RELEASE.2026-09-16T00-00-00Z@sha256:635197cb9f36d01bee221d34d1c7d7960f6a95c48b0b6c01d99cd13bdae51a46`

## Services
- `app`: http:9001, s3:9000

## Routes
- `app`: hosts `{{ .Release.Name }}.${SECRET_DOMAIN}`, gateways `envoy-internal`
- `s3`: hosts `s3.${SECRET_DOMAIN}`, gateways `envoy-internal`

## Persistence
- `config`: enabled=`True`, existingClaim=`backups`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/storage/minio/app >/tmp/minio-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n storage annotate helmrelease minio reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n storage get helmrelease minio -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n storage get pods -l app.kubernetes.io/instance=minio -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
