# promtail deployment

GitOps deployment README for `kubernetes/apps/observability/promtail/app/helmrelease.yaml`.

## Summary
- Namespace: `observability`
- HelmRelease: `promtail`
- Path: `kubernetes/apps/observability/promtail/app`
- Kustomization: `kubernetes/apps/observability/promtail/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/observability/promtail/ks.yaml`
- Chart: chart `promtail` from `HelmRepository/grafana` version `6.17.1`
- Reconcile interval: `5m`
- Timeout: `not declared`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/observability/promtail/app >/tmp/promtail-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n observability annotate helmrelease promtail reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n observability get helmrelease promtail -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n observability get pods -l app.kubernetes.io/instance=promtail -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
