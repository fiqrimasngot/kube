# ollama deployment

GitOps deployment README for `kubernetes/apps/devops/ollama/backend/helmrelease.yaml`.

## Summary
- Namespace: `devops`
- HelmRelease: `ollama`
- Path: `kubernetes/apps/devops/ollama/backend`
- Kustomization: `kubernetes/apps/devops/ollama/backend/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/devops/ollama/ks.yaml`
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `30m`
- Timeout: `not declared`

## Controllers and images
- `ollama`: type `Deployment`, replicas `1`
  - container `app` image `docker.io/ollama/ollama:0.19.0`

## Services
- `app`: http:11434

## Routes
- `app`: hosts `{{ .Release.Name }}.${SECRET_DOMAIN}`, gateways `envoy-internal`

## Persistence
- `config`: existingClaim=`ollama`
- `models`: existingClaim=`ollama-model`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/devops/ollama/backend >/tmp/ollama-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n devops annotate helmrelease ollama reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n devops get helmrelease ollama -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n devops get pods -l app.kubernetes.io/instance=ollama -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
