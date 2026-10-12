# kiwix deployment

GitOps deployment README for `kubernetes/apps/default/kiwix/app/helmrelease.yaml`.

## Summary
- Namespace: `default`
- HelmRelease: `kiwix`
- Path: `kubernetes/apps/default/kiwix/app`
- Kustomization: `kubernetes/apps/default/kiwix/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/default/kiwix/ks.yaml`
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `30m`
- Timeout: `not declared`

## Controllers and images
- `main`: type `Deployment`
  - container `app` image `ghcr.io/kiwix/kiwix-serve:latest`

## Services
- `app`: http:8080

## Routes
- `main`: hosts `{{ .Release.Name }}.${SECRET_DOMAIN}`, gateways `envoy-internal`

## Persistence
- `config`: existingClaim=`kiwix`
- `data`: existingClaim=`kiwix-library`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/default/kiwix/app >/tmp/kiwix-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default annotate helmrelease kiwix reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default get helmrelease kiwix -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default get pods -l app.kubernetes.io/instance=kiwix -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
