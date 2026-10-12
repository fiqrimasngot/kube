# cloudnative-pg deployment

GitOps deployment README for `kubernetes/apps/database/cloudnative-pg/app/helmrelease.yaml`.

## Summary
- Namespace: `database`
- HelmRelease: `cloudnative-pg`
- Path: `kubernetes/apps/database/cloudnative-pg/app`
- Kustomization: `kubernetes/apps/database/cloudnative-pg/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/database/cloudnative-pg/ks.yaml`
- Chart: chart `cloudnative-pg` from `HelmRepository/cloudnative-pg` version `0.27.0`
- Reconcile interval: `30m`
- Timeout: `not declared`

## Secret manifests
Secret manifest filenames only; do not put decrypted values in this README.
- `secrets.sops.yaml`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/database/cloudnative-pg/app >/tmp/cloudnative-pg-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n database annotate helmrelease cloudnative-pg reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n database get helmrelease cloudnative-pg -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n database get pods -l app.kubernetes.io/instance=cloudnative-pg -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
