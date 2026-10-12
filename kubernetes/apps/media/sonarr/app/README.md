# sonarr deployment

GitOps deployment README for `kubernetes/apps/media/sonarr/app/helmrelease.yaml`.

## Summary
- Namespace: `media`
- HelmRelease: `sonarr`
- Path: `kubernetes/apps/media/sonarr/app`
- Kustomization: `kubernetes/apps/media/sonarr/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/media/sonarr/ks.yaml`
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `30m`
- Timeout: `15m`

## Controllers and images
- `sonarr`: type `Deployment`
  - container `app` image `ghcr.io/home-operations/sonarr:4.0.17.2969@sha256:6806001ccc2ec95d941c9c0de012dbcb59c6a33932cfc17f71e300bdd48cabfe`

## Services
- `app`: http:80

## Routes
- `app`: hosts `{{ .Release.Name }}.${SECRET_DOMAIN}`, gateways `envoy-internal`

## Persistence
- `config`: existingClaim=`sonarr`
- `tmp`: type=`emptyDir`
- `tv`: type=`nfs`, path=`/media/tv`
- `downloads`: type=`nfs`, path=`/media/downloads`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/media/sonarr/app >/tmp/sonarr-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media annotate helmrelease sonarr reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media get helmrelease sonarr -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n media get pods -l app.kubernetes.io/instance=sonarr -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
