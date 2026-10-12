# open-webui deployment

GitOps deployment README for `kubernetes/apps/devops/ollama/ui/helmrelease.yaml`.

## Summary
- Namespace: `devops`
- HelmRelease: `open-webui`
- Path: `kubernetes/apps/devops/ollama/ui`
- Kustomization: `kubernetes/apps/devops/ollama/ui/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/devops/ollama/ks.yaml`
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `1h`
- Timeout: `not declared`

## Secret manifests
Secret manifest filenames only; do not put decrypted values in this README.
- `secrets.sops.yaml`

## Controllers and images
- `open-webui`: type `Deployment`
  - container `app` image `ghcr.io/open-webui/open-webui:0.7.2@sha256:16d9a3615b45f14a0c89f7ad7a3bf151f923ed32c2e68f9204eb17d1ce40774b`

## Services
- `app`: http:80

## Routes
- `app`: hosts `chad.${SECRET_DOMAIN}`, gateways `envoy-external`

## Persistence
- `data`: existingClaim=`ollama`
- `tmpfs`: type=`emptyDir`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/devops/ollama/ui >/tmp/open-webui-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n devops annotate helmrelease open-webui reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n devops get helmrelease open-webui -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n devops get pods -l app.kubernetes.io/instance=open-webui -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
