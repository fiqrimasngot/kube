# cyberchef deployment

GitOps deployment README for `kubernetes/apps/default/cyberchef/app/helmrelease.yaml`.

## Summary
- Namespace: `default`
- HelmRelease: `cyberchef`
- Path: `kubernetes/apps/default/cyberchef/app`
- Kustomization: `kubernetes/apps/default/cyberchef/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/default/cyberchef/ks.yaml`
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `15m`
- Timeout: `not declared`

## Controllers and images
- `cyberchef`: type `Deployment`, replicas `1`
  - container `app` image `docker.io/mpepping/cyberchef:v10.19.4`

## Services
- `app`: http:8000

## Routes
- `main`: hosts `{{ .Release.Name }}.${SECRET_DOMAIN}`, gateways `envoy-external`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/default/cyberchef/app >/tmp/cyberchef-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default annotate helmrelease cyberchef reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default get helmrelease cyberchef -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default get pods -l app.kubernetes.io/instance=cyberchef -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
