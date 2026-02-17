# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `helmrelease.yaml`
- `kustomization.yaml`
- `ocirepository.yaml`
- `secret.sops.yaml`

## `helmrelease.yaml` values

### Document 1: `HelmRelease` `cloudflare-dns`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `cloudflare-dns` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.chartRef.kind` | `OCIRepository` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.chartRef.name` | `cloudflare-dns` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.interval` | `1h` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.values.fullnameOverride` | `cloudflare-dns` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.provider` | `cloudflare` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.env` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.env.[0].name` | `CF_API_TOKEN` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.extraArgs` | `['--cloudflare-dns-records-per-page=1000', '--cloudflare-proxied', '--crd-source-apiver...` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.triggerLoopOnEvent` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.values.policy` | `sync` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.sources` | `['crd', 'gateway-httproute']` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.txtPrefix` | `k8s.` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.txtOwnerId` | `default` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.domainFilters` | `['${SECRET_DOMAIN}']` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.serviceMonitor.enabled` | `True` | Feature toggle chosen to match this environment's operational requirements. |
| `spec.values.podAnnotations.secret.reloader.stakater.com/reload` | `cloudflare-dns-secret` | Adds controller-specific hints/behaviors needed by tooling in this cluster. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./secret.sops.yaml', './helmrelease.yaml', './ocirepository.yaml']` | Defines which child manifests are composed together as this deployment unit. |


## `ocirepository.yaml` values

### Document 1: `OCIRepository` `cloudflare-dns`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `source.toolkit.fluxcd.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `OCIRepository` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `cloudflare-dns` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `15m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.layerSelector.mediaType` | `application/vnd.cncf.helm.chart.content.v1.tar+gzip` | Set intentionally to match this repository's desired-state for this component. |
| `spec.layerSelector.operation` | `copy` | Set intentionally to match this repository's desired-state for this component. |
| `spec.ref.tag` | `1.19.0` | Locks the application version to avoid unexpected upstream changes. |
| `spec.url` | `oci://ghcr.io/home-operations/charts-mirror/external-dns` | Set intentionally to match this repository's desired-state for this component. |


## `secret.sops.yaml` values

### Document 1: `Secret` `cloudflare-dns-secret`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Secret` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `cloudflare-dns-secret` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `stringData.api-token` | `ENC[AES256_GCM,data:h2hVz8DnPBPMpT7audo8ZNKbuaB9fhqQ9HmEByJlTn9FaUA9EJ0FjA==,iv:DlBpnM9...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].recipient` | `age1sumyxgm2je4txw82k838698mmqmf40wsw6j8eu3jhf5v54g4sslqpchxuf` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].enc` | `-----BEGIN AGE ENCRYPTED FILE----- YWdlLWVuY3J5cHRpb24ub3JnL3YxCi0+IFgyNTUxOSBUanE1S0U4...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.lastmodified` | `2026-02-17T11:15:05Z` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `sops.mac` | `ENC[AES256_GCM,data:8QurYgDgmCyImV5Kw6R9S08zgltcYN+k30ShAsvQ/+21HTjXb9/aZ6z9gy7eCJaMFDC...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.encrypted_regex` | `^(data|stringData)$` | Set intentionally to match this repository's desired-state for this component. |
| `sops.mac_only_encrypted` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `sops.version` | `3.11.0` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
