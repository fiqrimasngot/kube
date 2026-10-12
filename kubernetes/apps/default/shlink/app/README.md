# shlink deployment

GitOps deployment README for `kubernetes/apps/default/shlink/app/helmrelease.yaml`.

## Summary
- Namespace: `default`
- HelmRelease: `shlink`
- Path: `kubernetes/apps/default/shlink/app`
- Kustomization: `kubernetes/apps/default/shlink/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/default/shlink/ks.yaml`
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `30m`
- Timeout: `not declared`

## Secret manifests
Secret manifest filenames only; do not put decrypted values in this README.
- `secrets.sops.yaml`

## Controllers and images
- `shlink`: type `Deployment`
  - container `app` image `ghcr.io/shlinkio/shlink:4.6.0@sha256:e607cd6f8c7f6bfd4cc734c812538d4123602c455a439c43dd02b35af885948f`

## Services
- `app`: http:80

## Routes
- `main`: hosts `link.${SECRET_DOMAIN}`, gateways `envoy-external`

## Persistence
- `tmp`: type=`emptyDir`
- `tmp-data`: type=`emptyDir`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/default/shlink/app >/tmp/shlink-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default annotate helmrelease shlink reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default get helmrelease shlink -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default get pods -l app.kubernetes.io/instance=shlink -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
