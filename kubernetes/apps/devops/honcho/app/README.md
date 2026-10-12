# honcho deployment

GitOps deployment README for `kubernetes/apps/devops/honcho/app/helmrelease.yaml`.

## Summary
- Namespace: `devops`
- HelmRelease: `honcho`
- Path: `kubernetes/apps/devops/honcho/app`
- Kustomization: `kubernetes/apps/devops/honcho/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/devops/honcho/ks.yaml`
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `30m`
- Timeout: `15m`

## Secret manifests
Secret manifest filenames only; do not put decrypted values in this README.
- `auth-secret.sops.yaml`
- `secrets.sops.yaml`

## Supporting manifests
- `postgres.yaml`

## Controllers and images
- `api`: type `Deployment`
  - container `app` image `ghcr.io/plastic-labs/honcho:latest@sha256:c8f99f1d78d5698c53c559cfff9c00aa1dd4ad8bd57b5ced1e1795eb6a17f16c`
- `deriver`: type `Deployment`
  - container `app` image `ghcr.io/plastic-labs/honcho:latest@sha256:c8f99f1d78d5698c53c559cfff9c00aa1dd4ad8bd57b5ced1e1795eb6a17f16c`

## Services
- `app`: http:8000

## Routes
- `app`: hosts `{{ .Release.Name }}.${SECRET_DOMAIN}`, gateways `envoy-internal`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/devops/honcho/app >/tmp/honcho-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n devops annotate helmrelease honcho reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n devops get helmrelease honcho -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n devops get pods -l app.kubernetes.io/instance=honcho -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
