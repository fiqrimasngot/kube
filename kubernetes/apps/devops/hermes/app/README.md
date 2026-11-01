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

## Skill resolution

Profile skills take precedence over shared skills in `external_dirs`. Project skills take precedence over both. The init container patches a copy of the pinned image's resolver and fails startup if the expected source changes; it does not modify skill data. Different skills with the same name remain ambiguous across the entire project tier or within one profile or external root. A category path can select a shared skill only when that path does not also exist in a higher-priority root.

Existing local copies, even copies initially identical to shared skills, still shadow later shared updates. This patch does not identify or remove those copies because there is no trusted baseline. Shared updates are visible when no higher-priority copy matches.

The patch checks the exact source and patched SHA-256 hashes. A changed image fails the init container until the patch is reviewed and both hashes are updated. The patch script has its own content-hashed ConfigMap; changing it updates the pod template and triggers a rollout without a reloader. This restarts Hermes and can interrupt active sessions.

Run the resolver tests against an extracted copy of the pinned image source with its Python environment. Set `APP_TEMPLATE_CHART` to the app-template 5.3.0 chart archive to include the full Helm rollout render test:

```bash
HERMES_SOURCE=/opt/hermes APP_TEMPLATE_CHART=/path/to/app-template-5.3.0.tgz /opt/hermes/.venv/bin/python -m unittest discover -s kubernetes/apps/devops/hermes/app/tests -v
```

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
