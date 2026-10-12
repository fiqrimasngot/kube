# wallabag deployment

GitOps deployment README for `kubernetes/apps/default/wallabag/app/helmrelease.yaml`.

## Summary
- Namespace: `default`
- HelmRelease: `wallabag`
- Path: `kubernetes/apps/default/wallabag/app`
- Kustomization: `kubernetes/apps/default/wallabag/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/default/wallabag/ks.yaml`
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `30m`
- Timeout: `15m`

## Secret manifests
Secret manifest filenames only; do not put decrypted values in this README.
- `secrets.sops.yaml`

## Controllers and images
- `wallabag`: type `Deployment`
  - container `app` image `wallabag/wallabag:2.6.14`

## Services
- `app`: http:80

## Routes
- `main`: hosts `{{ .Release.Name }}.${SECRET_DOMAIN}`, gateways `envoy-external`

## Persistence
- `config`: enabled=`True`, existingClaim=`wallabag`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/default/wallabag/app >/tmp/wallabag-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default annotate helmrelease wallabag reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default get helmrelease wallabag -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default get pods -l app.kubernetes.io/instance=wallabag -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
