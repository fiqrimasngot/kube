# actions-runner-controller deployment

GitOps deployment README for `kubernetes/apps/devops/gha-runner-scale-set-controller/app/helmrelease.yaml`.

## Summary
- Namespace: `devops`
- HelmRelease: `actions-runner-controller`
- Path: `kubernetes/apps/devops/gha-runner-scale-set-controller/app`
- Kustomization: `kubernetes/apps/devops/gha-runner-scale-set-controller/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/devops/gha-runner-scale-set-controller/ks.yaml`
- Chart: chart `gha-runner-scale-set-controller` from `HelmRepository/actions-runner-controller` version `0.13.0`
- Reconcile interval: `30m`
- Timeout: `not declared`

## Secret manifests
Secret manifest filenames only; do not put decrypted values in this README.
- `secrets.sops.yaml`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/devops/gha-runner-scale-set-controller/app >/tmp/actions-runner-controller-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n devops annotate helmrelease actions-runner-controller reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n devops get helmrelease actions-runner-controller -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n devops get pods -l app.kubernetes.io/instance=actions-runner-controller -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
