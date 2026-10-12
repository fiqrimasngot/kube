# authentik deployment

GitOps deployment README for `kubernetes/apps/security/authentik/app/helmrelease.yaml`.

## Summary
- Namespace: `security`
- HelmRelease: `authentik`
- Path: `kubernetes/apps/security/authentik/app`
- Kustomization: `kubernetes/apps/security/authentik/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/security/authentik/ks.yaml`
- Chart: chart `authentik` from `HelmRepository/authentik` version `2026.5.3`
- Reconcile interval: `30m`
- Timeout: `not declared`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/security/authentik/app >/tmp/authentik-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n security annotate helmrelease authentik reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n security get helmrelease authentik -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n security get pods -l app.kubernetes.io/instance=authentik -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
