# paperless deployment

GitOps deployment README for `kubernetes/apps/default/paperless/app/helmrelease.yaml`.

## Summary
- Namespace: `default`
- HelmRelease: `paperless`
- Path: `kubernetes/apps/default/paperless/app`
- Kustomization: `kubernetes/apps/default/paperless/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/default/paperless/ks.yaml`
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `15m`
- Timeout: `15m`

## Secret manifests
Secret manifest filenames only; do not put decrypted values in this README.
- `secrets.sops.yaml`

## Controllers and images
- `paperless`: type `Deployment`
  - container `app` image `ghcr.io/paperless-ngx/paperless-ngx:2.20.15`
  - container `tika` image `docker.io/apache/tika:3.2.3.0-full`
  - container `gotenberg` image `gotenberg/gotenberg:8.25.1`

## Services
- `app`: http:8000

## Routes
- `app`: hosts `{{ .Release.Name }}.${SECRET_DOMAIN}`, gateways `envoy-external`

## Persistence
- `data`: enabled=`True`, type=`nfs`, path=`/doc/paperless/data`
- `media`: enabled=`True`, type=`nfs`, path=`/doc/paperless/media`
- `consume`: enabled=`True`, type=`nfs`, path=`/doc/paperless/incoming`
- `export`: enabled=`True`, type=`nfs`, path=`/doc/paperless/export`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/default/paperless/app >/tmp/paperless-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default annotate helmrelease paperless reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default get helmrelease paperless -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default get pods -l app.kubernetes.io/instance=paperless -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
