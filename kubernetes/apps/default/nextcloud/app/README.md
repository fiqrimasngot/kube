# nextcloud deployment

GitOps deployment README for `kubernetes/apps/default/nextcloud/app/helmrelease.yaml`.

## Summary
- Namespace: `default`
- HelmRelease: `nextcloud`
- Path: `kubernetes/apps/default/nextcloud/app`
- Kustomization: `kubernetes/apps/default/nextcloud/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/default/nextcloud/ks.yaml`
- Chart: chart `nextcloud` from `HelmRepository/nextcloud` version `8.7.0`
- Reconcile interval: `2h`
- Timeout: `not declared`

## Secret manifests
Secret manifest filenames only; do not put decrypted values in this README.
- `secrets.sops.yaml`

## Persistence

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/default/nextcloud/app >/tmp/nextcloud-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default annotate helmrelease nextcloud reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default get helmrelease nextcloud -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default get pods -l app.kubernetes.io/instance=nextcloud -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
