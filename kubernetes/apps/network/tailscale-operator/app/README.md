# tailscale-operator deployment

GitOps deployment README for `kubernetes/apps/network/tailscale-operator/app/helmrelease.yaml`.

## Summary
- Namespace: `network`
- HelmRelease: `tailscale-operator`
- Path: `kubernetes/apps/network/tailscale-operator/app`
- Kustomization: `kubernetes/apps/network/tailscale-operator/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/network/tailscale-operator/ks.yaml`
- Chart: chart `tailscale-operator` from `HelmRepository/tailscale` version `1.102.4`
- Reconcile interval: `30m`
- Timeout: `not declared`

## Secret manifests
Secret manifest filenames only; do not put decrypted values in this README.
- `secret.sops.yaml`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/network/tailscale-operator/app >/tmp/tailscale-operator-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n network annotate helmrelease tailscale-operator reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n network get helmrelease tailscale-operator -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n network get pods -l app.kubernetes.io/instance=tailscale-operator -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
