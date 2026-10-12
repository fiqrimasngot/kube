# sabnzbd deployment

GitOps deployment README for `kubernetes/apps/media/sabnzbd/app/helmrelease.yaml`.

## Summary
- Namespace: `media`
- HelmRelease: `sabnzbd`
- Path: `kubernetes/apps/media/sabnzbd/app`
- Kustomization: `kubernetes/apps/media/sabnzbd/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/media/sabnzbd/ks.yaml`
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `30m`
- Timeout: `15m`

## Controllers and images
- `sabnzbd`: type `Deployment`
  - container `app` image `ghcr.io/home-operations/sabnzbd:5.0.4@sha256:0c78c4752607d6d3fca43817af3540dad515c48dbab2c980ef7ef5bc27849b2b`

## Services
- `app`: http:80

## Routes
- `app`: hosts `{{ .Release.Name }}.${SECRET_DOMAIN}`, gateways `envoy-internal`

## Persistence
- `config`: existingClaim=`sabnzbd`
- `downloads`: type=`nfs`, path=`/media/downloads`
- `logs`: type=`emptyDir`
- `tmp`: type=`emptyDir`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/media/sabnzbd/app >/tmp/sabnzbd-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media annotate helmrelease sabnzbd reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media get helmrelease sabnzbd -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media get pods -l app.kubernetes.io/instance=sabnzbd -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
