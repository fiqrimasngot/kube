# dragonfly-operator deployment

GitOps deployment README for `kubernetes/apps/database/dragonfly/app/helmrelease.yaml`.

## Summary
- Namespace: `database`
- HelmRelease: `dragonfly-operator`
- Path: `kubernetes/apps/database/dragonfly/app`
- Kustomization: `kubernetes/apps/database/dragonfly/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/database/dragonfly/ks.yaml`
- Chart: chartRef `OCIRepository/dragonfly-operator`
- Reconcile interval: `1h`
- Timeout: `not declared`

## Supporting manifests
- `rbac.yaml`

## Controllers and images
- `dragonfly-operator`: type `Deployment`
  - container `app` image `ghcr.io/dragonflydb/operator:v1.4.0@sha256:b6ceebe49d4687a4fc3e485724a0cfcf0ca2dfba1d5508375543b8db46a66fc1`

## Services
- `app`: http:8081, metrics:8080

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/database/dragonfly/app >/tmp/dragonfly-operator-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n database annotate helmrelease dragonfly-operator reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n database get helmrelease dragonfly-operator -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n database get pods -l app.kubernetes.io/instance=dragonfly-operator -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
