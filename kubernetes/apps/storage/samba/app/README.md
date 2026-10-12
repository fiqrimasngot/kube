# samba deployment

GitOps deployment README for `kubernetes/apps/storage/samba/app/helmrelease.yaml`.

## Summary
- Namespace: `storage`
- HelmRelease: `samba`
- Path: `kubernetes/apps/storage/samba/app`
- Kustomization: `kubernetes/apps/storage/samba/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/storage/samba/ks.yaml`
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `1h`
- Timeout: `not declared`

## Controllers and images
- `samba`: type `Deployment`
  - container `main` image `ghcr.io/crazy-max/samba:4.21.4@sha256:75f5037770eab774b82f298268305af8a18a01a1daad679f8d2d17c54059c847`

## Services
- `main`: smb:445

## Persistence
- `config`: type=`configMap`
- `time-machine`: type=`nfs`, path=`/doc/TimeMachine`
- `camera`: type=`nfs`, path=`/doc/camera`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/storage/samba/app >/tmp/samba-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n storage annotate helmrelease samba reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n storage get helmrelease samba -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n storage get pods -l app.kubernetes.io/instance=samba -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
