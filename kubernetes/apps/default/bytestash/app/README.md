# bytestash deployment

GitOps deployment README for `kubernetes/apps/default/bytestash/app/helmrelease.yaml`.

## Summary
- Namespace: `default`
- HelmRelease: `bytestash`
- Path: `kubernetes/apps/default/bytestash/app`
- Kustomization: `kubernetes/apps/default/bytestash/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/default/bytestash/ks.yaml`
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `30m`
- Timeout: `not declared`

## Secret manifests
Secret manifest filenames only; do not put decrypted values in this README.
- `secrets.sops.yaml`

## Controllers and images
- `bytestash`: type `Deployment`
  - container `app` image `ghcr.io/jordan-dalby/bytestash:1.5.9@sha256:9c17b5510ca45c976fe23b0d4705ad416aa58d4bf756a70e03ef1f08cf7801fd`

## Services
- `app`: http:5000

## Routes
- `app`: hosts `{{ .Release.Name }}.${SECRET_DOMAIN}`, gateways `envoy-external`

## Persistence
- `data`: existingClaim=`bytestash`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/default/bytestash/app >/tmp/bytestash-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default annotate helmrelease bytestash reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default get helmrelease bytestash -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default get pods -l app.kubernetes.io/instance=bytestash -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
