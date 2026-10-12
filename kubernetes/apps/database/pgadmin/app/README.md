# pgadmin deployment

GitOps deployment README for `kubernetes/apps/database/pgadmin/app/helmrelease.yaml`.

## Summary
- Namespace: `database`
- HelmRelease: `pgadmin`
- Path: `kubernetes/apps/database/pgadmin/app`
- Kustomization: `kubernetes/apps/database/pgadmin/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/database/pgadmin/ks.yaml`
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `30m`
- Timeout: `not declared`

## Secret manifests
Secret manifest filenames only; do not put decrypted values in this README.
- `secrets.sops.yaml`

## Controllers and images
- `pgadmin`: type `statefulset`
  - container `app` image `dpage/pgadmin4:9.11`

## Services
- `app`: http:80

## Routes
- `app`: hosts `{{ .Release.Name }}.${SECRET_DOMAIN}`, gateways `envoy-internal`

## Persistence
- `server-json`: enabled=`True`, type=`configMap`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/database/pgadmin/app >/tmp/pgadmin-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n database annotate helmrelease pgadmin reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n database get helmrelease pgadmin -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n database get pods -l app.kubernetes.io/instance=pgadmin -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
