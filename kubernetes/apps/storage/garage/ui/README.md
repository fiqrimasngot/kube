# garage-webui deployment

GitOps deployment README for `kubernetes/apps/storage/garage/ui/helmrelease.yaml`.

## Summary
- Namespace: `storage`
- HelmRelease: `garage-webui`
- Path: `kubernetes/apps/storage/garage/ui`
- Kustomization: `kubernetes/apps/storage/garage/ui/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/storage/garage/ks.yaml`
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `1h`
- Timeout: `not declared`

## Controllers and images
- `garage-webui`: type `Deployment`
  - container `app` image `docker.io/khairul169/garage-webui:1.1.0@sha256:17c793551873155065bf9a022dabcde874de808a1f26e648d4b82e168806439c`

## Services
- `app`: http:3909

## Routes
- `app`: hosts `garage.${SECRET_DOMAIN}`, gateways `envoy-internal`

## Persistence
- `config`: type=`secret`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/storage/garage/ui >/tmp/garage-webui-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n storage annotate helmrelease garage-webui reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n storage get helmrelease garage-webui -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n storage get pods -l app.kubernetes.io/instance=garage-webui -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
