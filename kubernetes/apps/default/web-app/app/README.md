# web-app deployment

GitOps deployment README for `kubernetes/apps/default/web-app/app/helmrelease.yaml`.

## Summary
- Namespace: `default`
- HelmRelease: `web-app`
- Path: `kubernetes/apps/default/web-app/app`
- Kustomization: `kubernetes/apps/default/web-app/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/default/web-app/ks.yaml`
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `30m`
- Timeout: `not declared`

## Controllers and images
- `main`: type `Deployment`
  - container `app` image `fiqrimasngot/bakeryapp:latest`

## Services
- `main`: http:80

## Routes
- `main`: hosts `bakery.${SECRET_DOMAIN}`, gateways `envoy-internal`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/default/web-app/app >/tmp/web-app-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default annotate helmrelease web-app reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default get helmrelease web-app -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default get pods -l app.kubernetes.io/instance=web-app -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
