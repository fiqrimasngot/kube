# searxng deployment

GitOps deployment README for `kubernetes/apps/default/searxng/app/helmrelease.yaml`.

## Summary
- Namespace: `default`
- HelmRelease: `searxng`
- Path: `kubernetes/apps/default/searxng/app`
- Kustomization: `kubernetes/apps/default/searxng/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/default/searxng/ks.yaml`
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `30m`
- Timeout: `not declared`

## Secret manifests
Secret manifest filenames only; do not put decrypted values in this README.
- `secrets.sops.yaml`

## Controllers and images
- `searxng`: type `Deployment`
  - container `app` image `docker.io/searxng/searxng:2024.7.7-ef103ba80`

## Services
- `app`: http:8080

## Routes
- `app`: hosts `search.${SECRET_DOMAIN}`, gateways `envoy-external`

## Persistence
- `config`: type=`configMap`
- `tmp`: type=`emptyDir`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/default/searxng/app >/tmp/searxng-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default annotate helmrelease searxng reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default get helmrelease searxng -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default get pods -l app.kubernetes.io/instance=searxng -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
