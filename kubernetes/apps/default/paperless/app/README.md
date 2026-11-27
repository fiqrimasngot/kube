# paperless deployment

GitOps deployment README for `kubernetes/apps/default/paperless/app/helmrelease.yaml`.

## Summary

- Namespace: `default`
- HelmRelease: `paperless`
- Path: `kubernetes/apps/default/paperless/app`
- Kustomization: `kubernetes/apps/default/paperless/app/kustomization.yaml`
- Flux app Kustomization: `kubernetes/apps/default/paperless/ks.yaml`
- Chart: chartRef `OCIRepository/app-template`
- Reconcile interval: `15m`
- Timeout: `15m`

## Secret manifests

Secret manifest filenames only; do not put decrypted values in this README.

- `secrets.sops.yaml`

## Controllers and images

- `paperless`: type `Deployment`
    - container `app` image `ghcr.io/paperless-ngx/paperless-ngx:3.5.1`
    - container `tika` image `docker.io/apache/tika:3.4.0.0-full`
    - container `gotenberg` image `gotenberg/gotenberg:9.10.2`

### Gotenberg 9 compatibility

Paperless 3.5.1 bundles `gotenberg-client` 1.0.0, which still sends Gotenberg 8
requests. Gotenberg 9 removed `/forms/pdfengines/merge` and the `pdfa` field.
The app-only `PYTHONPATH` loads `compat/sitecustomize.py` from a read-only
ConfigMap. It translates merge requests to `/forms/pdf/pipe` with a merge
stage, then converts `pdfa` to a final remediation stage. HTML and Office
conversion get the same PDF/A translation. PDF/A is not disabled.

The ConfigMap name includes a content hash and Kustomize rewrites the
HelmRelease reference. Changing the shim therefore rolls out a new pod.
No packages are installed at startup and no image files are overwritten.
This is a temporary, narrowly scoped adapter, not a full Gotenberg 8 proxy.
It rejects requests if the client version changes until compatibility is
revalidated. Remove the ConfigMap, mount, `PYTHONPATH` and name-reference
configuration once Paperless ships native Gotenberg 9 support.

Run the unit tests with the exact bundled client, then the synthetic probe
inside the app container. The probe does not import documents or modify mail.

```bash
uv run --no-project --with 'gotenberg-client[httpx]==1.0.0' python kubernetes/apps/default/paperless/app/tests/test_compat.py -v
kubectl -n default exec -i deploy/paperless -c app -- python3 - < kubernetes/apps/default/paperless/app/tests/probe_gotenberg.py
```

The probe must print PASS for multi-page merge, single-input merge,
HTML-to-PDF/A and Office-to-PDF/A. Each checks HTTP 200, PDF bytes, page
count and PDF/A-2b metadata. It does not replace a full conformance validator.
After repair, replay failed email separately using its exact rule, folder,
UID and UID validity; do not clear all processed-mail records.

API reference: https://gotenberg.dev/docs/getting-started/upgrade

## Services

- `app`: http:8000

## Routes

- `app`: hosts `{{ .Release.Name }}.${SECRET_DOMAIN}`, gateways `envoy-external`

## Persistence

- `data`: enabled=`True`, type=`nfs`, path=`/doc/paperless/data`
- `media`: enabled=`True`, type=`nfs`, path=`/doc/paperless/media`
- `consume`: enabled=`True`, type=`nfs`, path=`/doc/paperless/incoming`
- `export`: enabled=`True`, type=`nfs`, path=`/doc/paperless/export`

## Validate changes

```bash
cd /opt/data/workspace/kube
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig kustomize kubernetes/apps/default/paperless/app >/tmp/paperless-render.yaml
git diff --check
```

## Reconcile and inspect

```bash
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default annotate helmrelease paperless reconcile.fluxcd.io/requestedAt="$(date -u +%Y-%m-%dT%H:%M:%SZ)" --overwrite
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default get helmrelease paperless -o wide
/opt/data/cache/scratch/kubectl --kubeconfig /opt/data/workspace/kube/kubeconfig -n default get pods -l app.kubernetes.io/instance=paperless -o wide
```

## Troubleshooting notes

- Check the Flux `Kustomization` before debugging pods if manifests are not applied.
- Check `HelmRelease` conditions and events for chart/render/apply failures.
- Check pod logs and service endpoints after the HelmRelease is `Ready=True`.
- Keep Git and template mirrors in sync when this deployment also exists under `template/config/**`.
