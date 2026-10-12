# mealie deployment

GitOps deployment README for `kubernetes/apps/default/mealie/app/helmrelease.yaml`.

## Summary
- Namespace: `default`
- HelmRelease: `mealie`
- Path: `kubernetes/apps/default/mealie/app`
- Kustomization: `kubernetes/apps/default/mealie/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/default/mealie/ks.yaml`
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `30m`
- Timeout: `15m`

## Secret manifests
Secret manifest filenames only; do not put decrypted values in this README.
- `secrets.sops.yaml`

## Controllers and images
- `mealie`: type `Deployment`
  - container `app` image `ghcr.io/mealie-recipes/mealie:v3.28.0`

## Services
- `app`: http:9000

## Routes
- `app`: hosts `recipes.${SECRET_DOMAIN}`, gateways `envoy-internal`

## Persistence
- `data`: existingClaim=`mealie`
- `tmp`: type=`emptyDir`
- `nltk`: type=`emptyDir`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/default/mealie/app >/tmp/mealie-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default annotate helmrelease mealie reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default get helmrelease mealie -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default get pods -l app.kubernetes.io/instance=mealie -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
