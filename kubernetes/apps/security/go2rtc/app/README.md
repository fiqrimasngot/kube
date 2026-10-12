# go2rtc deployment

GitOps deployment README for `kubernetes/apps/security/go2rtc/app/helmrelease.yaml`.

## Summary
- Namespace: `security`
- HelmRelease: `go2rtc`
- Path: `kubernetes/apps/security/go2rtc/app`
- Kustomization: `kubernetes/apps/security/go2rtc/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/security/go2rtc/ks.yaml`
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `1h`
- Timeout: `not declared`

## Controllers and images
- `go2rtc`: type `Deployment`
  - container `app` image `ghcr.io/alexxit/go2rtc:1.9.14@sha256:675c318b23c06fd862a61d262240c9a63436b4050d177ffc68a32710d9e05bae`

## Services
- `app`: http:80, rtsp:554, webrtc-tcp:8555, webrtc-udp:8555

## Routes
- `app`: hosts `go2rtc.${SECRET_DOMAIN}`, gateways `envoy-internal`

## Persistence
- `config`: existingClaim=`go2rtc`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/security/go2rtc/app >/tmp/go2rtc-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n security annotate helmrelease go2rtc reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n security get helmrelease go2rtc -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n security get pods -l app.kubernetes.io/instance=go2rtc -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
