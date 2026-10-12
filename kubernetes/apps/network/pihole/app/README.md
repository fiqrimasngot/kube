# pihole deployment

GitOps deployment README for `kubernetes/apps/network/pihole/app/helmrelease.yaml`.

## Summary
- Namespace: `network`
- HelmRelease: `pihole`
- Path: `kubernetes/apps/network/pihole/app`
- Kustomization: `kubernetes/apps/network/pihole/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/network/pihole/ks.yaml`
- Chart: chart `pihole` from `HelmRepository/pihole` version `2.38.0`
- Reconcile interval: `15m`
- Timeout: `not declared`

## Secret manifests
Secret manifest filenames only; do not put decrypted values in this README.
- `secret.sops.yaml`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/network/pihole/app >/tmp/pihole-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n network annotate helmrelease pihole reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n network get helmrelease pihole -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n network get pods -l app.kubernetes.io/instance=pihole -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
