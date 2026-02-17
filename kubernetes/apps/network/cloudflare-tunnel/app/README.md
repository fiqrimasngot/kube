# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `dnsendpoint.yaml`
- `helmrelease.yaml`
- `kustomization.yaml`
- `ocirepository.yaml`
- `secret.sops.yaml`

## `dnsendpoint.yaml` values

### Document 1: `DNSEndpoint` `cloudflare-tunnel`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `externaldns.k8s.io/v1alpha1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `DNSEndpoint` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `cloudflare-tunnel` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.endpoints` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.endpoints.[0].dnsName` | `external.${SECRET_DOMAIN}` | Set intentionally to match this repository's desired-state for this component. |
| `spec.endpoints.[0].recordType` | `CNAME` | Set intentionally to match this repository's desired-state for this component. |


## `helmrelease.yaml` values

### Document 1: `HelmRelease` `cloudflare-tunnel`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `cloudflare-tunnel` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.chartRef.kind` | `OCIRepository` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.chartRef.name` | `cloudflare-tunnel` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.interval` | `1h` | Uses a reconcile interval that balances configuration freshness with API/controller load. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./dnsendpoint.yaml', './secret.sops.yaml', './helmrelease.yaml', './ocirepository.yaml']` | Defines which child manifests are composed together as this deployment unit. |


## `ocirepository.yaml` values

### Document 1: `OCIRepository` `cloudflare-tunnel`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `source.toolkit.fluxcd.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `OCIRepository` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `cloudflare-tunnel` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `15m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.layerSelector.mediaType` | `application/vnd.cncf.helm.chart.content.v1.tar+gzip` | Set intentionally to match this repository's desired-state for this component. |
| `spec.layerSelector.operation` | `copy` | Set intentionally to match this repository's desired-state for this component. |
| `spec.ref.tag` | `4.5.0` | Locks the application version to avoid unexpected upstream changes. |
| `spec.url` | `oci://ghcr.io/bjw-s-labs/helm/app-template` | Set intentionally to match this repository's desired-state for this component. |


## `secret.sops.yaml` values

### Document 1: `Secret` `cloudflare-tunnel-secret`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Secret` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `cloudflare-tunnel-secret` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `stringData.TUNNEL_TOKEN` | `ENC[AES256_GCM,data:heypMDEVAWKmK8yfWfL3VHxaIVBmEJri97ji2r8DZ22KNkL3sjPHvZ9N3cGmtotTSKU...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].recipient` | `age1sumyxgm2je4txw82k838698mmqmf40wsw6j8eu3jhf5v54g4sslqpchxuf` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].enc` | `-----BEGIN AGE ENCRYPTED FILE----- YWdlLWVuY3J5cHRpb24ub3JnL3YxCi0+IFgyNTUxOSBWZEFoQm1m...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.lastmodified` | `2026-02-17T11:15:05Z` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `sops.mac` | `ENC[AES256_GCM,data:exwhc6XUn11YHbwd/dB9PxiNqui1QnLsFTLGlmtrvWbuScza/yJPSje2WpLRiNkGlFm...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.encrypted_regex` | `^(data|stringData)$` | Set intentionally to match this repository's desired-state for this component. |
| `sops.mac_only_encrypted` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `sops.version` | `3.11.0` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
