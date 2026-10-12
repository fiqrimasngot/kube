# obsidian-couchdb deployment

GitOps deployment README for `kubernetes/apps/database/obsidian-couchdb/app/helmrelease.yaml`.

## Summary
- Namespace: `database`
- HelmRelease: `obsidian-couchdb`
- Path: `kubernetes/apps/database/obsidian-couchdb/app`
- Kustomization: `kubernetes/apps/database/obsidian-couchdb/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/database/obsidian-couchdb/ks.yaml`
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `30m`
- Timeout: `not declared`

## Secret manifests
Secret manifest filenames only; do not put decrypted values in this README.
- `secrets.sops.yaml`

## Controllers and images
- `main`: type `statefulset`
  - container `main` image `public.ecr.aws/docker/library/couchdb:3.5.1`

## Services
- `main`: http:5984

## Routes
- `main`: hosts `{{ .Release.Name }}.${SECRET_DOMAIN}`, gateways `envoy-external`

## Persistence
- `config`: type=`configMap`
- `config-storage`: type=`emptyDir`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/database/obsidian-couchdb/app >/tmp/obsidian-couchdb-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n database annotate helmrelease obsidian-couchdb reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n database get helmrelease obsidian-couchdb -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n database get pods -l app.kubernetes.io/instance=obsidian-couchdb -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
