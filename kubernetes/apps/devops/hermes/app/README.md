# hermes deployment

GitOps deployment README for `kubernetes/apps/devops/hermes/app/helmrelease.yaml`.

## Summary
- Namespace: `devops`
- HelmRelease: `hermes`
- Path: `kubernetes/apps/devops/hermes/app`
- Kustomization: `kubernetes/apps/devops/hermes/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/devops/hermes/ks.yaml`
- Chart: chartRef `OCIRepository/hermes`
- Reconcile interval: `1h`
- Timeout: `not declared`

## Secret manifests
Secret manifest filenames only; do not put decrypted values in this README.
- `secret.sops.yaml`

## Supporting manifests
- `ocirepository.yaml`

## Controllers and images
- `hermes`: type `Deployment`
  - container `app` image `nousresearch/hermes-agent:v2026.9.24@sha256:fca358f12efd65bfaaca05884166f15c0e2788375ca30d77061ac1ebc96452b7`
- `codeserver`: type `Deployment`
  - container `codeserver` image `ghcr.io/coder/code-server:4.139.1@sha256:0c067c3cf09ed1830ce282387826be8feefef8a5828f462791c2df3f1007ee17`

## Services
- `hermes`: dashboard:9119, agent:8642
- `codeserver`: http:12321

## Routes
- `hermes`: hosts `hermes.${SECRET_DOMAIN}`, gateways `envoy-external, envoy-internal`
- `codeserver`: hosts `hermesconf.${SECRET_DOMAIN}`, gateways `envoy-internal`

## Persistence
- `data`: existingClaim=`{{ .Release.Name }}`
- `tmp`: type=`emptyDir`
- `config`: type=`configMap`

## Validate changes
```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/devops/hermes/app >/tmp/hermes-render.yaml
git diff --check
```

## Reconcile and inspect
```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n devops annotate helmrelease hermes reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n devops get helmrelease hermes -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n devops get pods -l app.kubernetes.io/instance=hermes -o wide
```

## Troubleshooting notes
- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
