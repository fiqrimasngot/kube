# home-assistant deployment

GitOps deployment README for `kubernetes/apps/default/home-assistant/app/helmrelease.yaml`.

## Summary
- Namespace: `default`
- HelmRelease: `home-assistant`
- Path: `kubernetes/apps/default/home-assistant/app`
- Kustomization: `kubernetes/apps/default/home-assistant/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/default/home-assistant/ks.yaml`
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `15m`
- Timeout: `not declared`

## Secret manifests
Secret manifest filenames only; do not put decrypted values in this README.
- `secrets.sops.yaml`

## Controllers and images
- `main`: type `Deployment`
  - container `main` image `ghcr.io/home-operations/home-assistant:2026.6.3@sha256:82db7a297c96a0288559c5f2849878168c14a06557edc114084d874268c92a9a`
  - container `code` image `ghcr.io/coder/code-server:4.139.1`

## Services
- `main`: http:8123

## Routes
- `main`: hosts `ha.${SECRET_DOMAIN}`, gateways `envoy-external`

## Persistence
- `config`: enabled=`True`, existingClaim=`home-assistant-pvc`
- `usb`: enabled=`True`, type=`hostPath`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/default/home-assistant/app >/tmp/home-assistant-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default annotate helmrelease home-assistant reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default get helmrelease home-assistant -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default get pods -l app.kubernetes.io/instance=home-assistant -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
