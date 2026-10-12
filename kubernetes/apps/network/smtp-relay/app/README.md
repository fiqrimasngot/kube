# smtp-relay deployment

GitOps deployment README for `kubernetes/apps/network/smtp-relay/app/helmrelease.yaml`.

## Summary
- Namespace: `network`
- HelmRelease: `smtp-relay`
- Path: `kubernetes/apps/network/smtp-relay/app`
- Kustomization: `kubernetes/apps/network/smtp-relay/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/network/smtp-relay/ks.yaml`
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `1h`
- Timeout: `not declared`

## Secret manifests
Secret manifest filenames only; do not put decrypted values in this README.
- `secret.sops.yaml`

## Supporting manifests
- `certificate.yaml`

## Controllers and images
- `smtp-relay`: type `Deployment`
  - container `app` image `ghcr.io/foxcpp/maddy:0.8.2@sha256:eeb5813fc4d101ec5d8f7b08b7255fd76ced2a06884ea94450c8a9a22fd6a08d`

## Services
- `app`: http:8080, smtp:25

## Persistence
- `config`: type=`configMap`
- `cache`: type=`emptyDir`
- `tls`: type=`secret`
- `state`: type=`emptyDir`
- `runtime`: type=`emptyDir`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/network/smtp-relay/app >/tmp/smtp-relay-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n network annotate helmrelease smtp-relay reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n network get helmrelease smtp-relay -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n network get pods -l app.kubernetes.io/instance=smtp-relay -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
