# strimzi deployment

GitOps deployment README for `kubernetes/apps/devops/kafka/app/helmrelease.yaml`.

## Summary
- Namespace: `devops`
- HelmRelease: `strimzi`
- Path: `kubernetes/apps/devops/kafka/app`
- Kustomization: `kubernetes/apps/devops/kafka/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/devops/kafka/ks.yaml`
- Chart: chart `strimzi-kafka-operator` from `HelmRepository/strimzi` version `0.49.1`
- Reconcile interval: `30m`
- Timeout: `not declared`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/devops/kafka/app >/tmp/strimzi-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n devops annotate helmrelease strimzi reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n devops get helmrelease strimzi -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n devops get pods -l app.kubernetes.io/instance=strimzi -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
