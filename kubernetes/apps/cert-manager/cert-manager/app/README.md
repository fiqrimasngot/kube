# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `clusterissuer.yaml`
- `helmrelease.yaml`
- `kustomization.yaml`
- `ocirepository.yaml`
- `secret.sops.yaml`

## `clusterissuer.yaml` values

### Document 1: `ClusterIssuer` `letsencrypt-production`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `cert-manager.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `ClusterIssuer` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `letsencrypt-production` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.acme.server` | `https://acme-v02.api.letsencrypt.org/directory` | Set intentionally to match this repository's desired-state for this component. |
| `spec.acme.privateKeySecretRef.name` | `letsencrypt-production` | Set intentionally to match this repository's desired-state for this component. |
| `spec.acme.solvers` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |


## `helmrelease.yaml` values

### Document 1: `HelmRelease` `cert-manager`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `cert-manager` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.chartRef.kind` | `OCIRepository` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.chartRef.name` | `cert-manager` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.interval` | `1h` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.values.crds.enabled` | `True` | Feature toggle chosen to match this environment's operational requirements. |
| `spec.values.replicaCount` | `1` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.values.dns01RecursiveNameservers` | `https://1.1.1.1:443/dns-query,https://1.0.0.1:443/dns-query` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.dns01RecursiveNameserversOnly` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.values.prometheus.enabled` | `True` | Feature toggle chosen to match this environment's operational requirements. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./clusterissuer.yaml', './helmrelease.yaml', './ocirepository.yaml', './secret.sops.y...` | Defines which child manifests are composed together as this deployment unit. |


## `ocirepository.yaml` values

### Document 1: `OCIRepository` `cert-manager`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `source.toolkit.fluxcd.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `OCIRepository` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `cert-manager` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `15m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.layerSelector.mediaType` | `application/vnd.cncf.helm.chart.content.v1.tar+gzip` | Set intentionally to match this repository's desired-state for this component. |
| `spec.layerSelector.operation` | `copy` | Set intentionally to match this repository's desired-state for this component. |
| `spec.ref.tag` | `v1.19.2` | Locks the application version to avoid unexpected upstream changes. |
| `spec.url` | `oci://quay.io/jetstack/charts/cert-manager` | Set intentionally to match this repository's desired-state for this component. |


## `secret.sops.yaml` values

### Document 1: `Secret` `cert-manager-secret`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Secret` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `cert-manager-secret` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `stringData.api-token` | `ENC[AES256_GCM,data:OV9ABwl6l0LI7IVfGHGWGIfYS8ES1NGsfTU2+DABYrF0N8fR6lUTSA==,iv:U/wISqS...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].recipient` | `age1sumyxgm2je4txw82k838698mmqmf40wsw6j8eu3jhf5v54g4sslqpchxuf` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].enc` | `-----BEGIN AGE ENCRYPTED FILE----- YWdlLWVuY3J5cHRpb24ub3JnL3YxCi0+IFgyNTUxOSBsVnVkRzE1...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.lastmodified` | `2026-02-17T11:15:05Z` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `sops.mac` | `ENC[AES256_GCM,data:qIwAuKBhreGK0872GePOLyIqc8U2T+/iu76Y5NpcdvNqxMH72V99ChtkRpa9B/g6ERt...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.encrypted_regex` | `^(data|stringData)$` | Set intentionally to match this repository's desired-state for this component. |
| `sops.mac_only_encrypted` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `sops.version` | `3.11.0` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
