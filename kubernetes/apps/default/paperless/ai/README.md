# paperless-ai deployment

GitOps deployment README for `kubernetes/apps/default/paperless/ai/helmrelease.yaml`.

## Summary
- Namespace: `default`
- HelmRelease: `paperless-ai`
- Path: `kubernetes/apps/default/paperless/ai`
- Kustomization: `kubernetes/apps/default/paperless/ai/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/default/paperless/ks.yaml`
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `15m`
- Timeout: `15m`

## Secret manifests
Secret manifest filenames only; do not put decrypted values in this README.
- `secrets.sops.yaml`

## Controllers and images
- `paperless-ai`: type `Deployment`
  - container `app` image `docker.io/clusterzx/paperless-ai:3.0.9@sha256:2b65888163fd59716f1c8285b31c5bd0b30c9c3c192c42b516688e3887d4ba60`

## Services
- `app`: http:3000

## Routes
- `app`: hosts `paperless-ai.${SECRET_DOMAIN}`, gateways `envoy-internal`

## Persistence
- `data`: enabled=`True`, existingClaim=`paperless-ai`
- `tmpfs`: enabled=`True`, type=`emptyDir`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/default/paperless/ai >/tmp/paperless-ai-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default annotate helmrelease paperless-ai reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default get helmrelease paperless-ai -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default get pods -l app.kubernetes.io/instance=paperless-ai -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
