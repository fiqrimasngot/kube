# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `grafanadashboard.yaml`
- `helmrelease.yaml`
- `kustomization.yaml`
- `secret.sops.yaml`

## `grafanadashboard.yaml` values

### Document 1: `GrafanaDashboard` `ceph-cluster`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `grafana.integreatly.org/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `GrafanaDashboard` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `ceph-cluster` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.allowCrossNamespaceImport` | `True` | Uses the network port expected by clients, probes, or upstream services. |
| `spec.instanceSelector.matchLabels.grafana.internal/instance` | `grafana` | Supports selectors, grouping, and operational discoverability. |
| `spec.datasources` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.datasources.[0].datasourceName` | `prometheus` | Set intentionally to match this repository's desired-state for this component. |
| `spec.datasources.[0].inputName` | `DS_PROMETHEUS` | Set intentionally to match this repository's desired-state for this component. |
| `spec.url` | `https://grafana.com/api/dashboards/2842/revisions/18/download` | Set intentionally to match this repository's desired-state for this component. |

### Document 2: `GrafanaDashboard` `ceph-osd`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `grafana.integreatly.org/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `GrafanaDashboard` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `ceph-osd` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.allowCrossNamespaceImport` | `True` | Uses the network port expected by clients, probes, or upstream services. |
| `spec.instanceSelector.matchLabels.grafana.internal/instance` | `grafana` | Supports selectors, grouping, and operational discoverability. |
| `spec.datasources` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.datasources.[0].datasourceName` | `prometheus` | Set intentionally to match this repository's desired-state for this component. |
| `spec.datasources.[0].inputName` | `DS_PROMETHEUS` | Set intentionally to match this repository's desired-state for this component. |
| `spec.url` | `https://grafana.com/api/dashboards/5336/revisions/9/download` | Set intentionally to match this repository's desired-state for this component. |

### Document 3: `GrafanaDashboard` `ceph-pools`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `grafana.integreatly.org/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `GrafanaDashboard` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `ceph-pools` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.allowCrossNamespaceImport` | `True` | Uses the network port expected by clients, probes, or upstream services. |
| `spec.instanceSelector.matchLabels.grafana.internal/instance` | `grafana` | Supports selectors, grouping, and operational discoverability. |
| `spec.datasources` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.datasources.[0].datasourceName` | `prometheus` | Set intentionally to match this repository's desired-state for this component. |
| `spec.datasources.[0].inputName` | `DS_PROMETHEUS` | Set intentionally to match this repository's desired-state for this component. |
| `spec.url` | `https://grafana.com/api/dashboards/5342/revisions/9/download` | Set intentionally to match this repository's desired-state for this component. |


## `helmrelease.yaml` values

### Document 1: `OCIRepository` `rook-ceph`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `source.toolkit.fluxcd.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `OCIRepository` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `rook-ceph` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `15m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.layerSelector.mediaType` | `application/vnd.cncf.helm.chart.content.v1.tar+gzip` | Set intentionally to match this repository's desired-state for this component. |
| `spec.layerSelector.operation` | `copy` | Set intentionally to match this repository's desired-state for this component. |
| `spec.ref.tag` | `v1.18.8` | Locks the application version to avoid unexpected upstream changes. |
| `spec.url` | `oci://ghcr.io/rook/rook-ceph` | Set intentionally to match this repository's desired-state for this component. |

### Document 2: `HelmRelease` `rook-ceph`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `rook-ceph` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.chartRef.kind` | `OCIRepository` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.chartRef.name` | `rook-ceph` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.interval` | `1h` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.values.csi.cephFSKernelMountOptions` | `ms_mode=prefer-crc` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.csi.enableLiveness` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.values.image.repository` | `ghcr.io/rook/ceph` | Fixes the container image used at runtime so behavior is predictable across reconciliations. |
| `spec.values.monitoring.enabled` | `True` | Feature toggle chosen to match this environment's operational requirements. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./helmrelease.yaml', './secret.sops.yaml']` | Defines which child manifests are composed together as this deployment unit. |


## `secret.sops.yaml` values

### Document 1: `Secret` `rook-ceph-dashboard-password`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Secret` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `rook-ceph-dashboard-password` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `stringData.password` | `ENC[AES256_GCM,data:A30yjM5M0VLCmeRn3070+6FlMYllsNFIq3adgY+VjSRYRLZYrM/MA8nfgFpMOsVqTgk...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].recipient` | `age1sumyxgm2je4txw82k838698mmqmf40wsw6j8eu3jhf5v54g4sslqpchxuf` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].enc` | `-----BEGIN AGE ENCRYPTED FILE----- YWdlLWVuY3J5cHRpb24ub3JnL3YxCi0+IFgyNTUxOSBNWVYrNW1Y...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.lastmodified` | `2026-02-17T11:15:05Z` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `sops.mac` | `ENC[AES256_GCM,data:lIUrBQIOS/QuUu3hg90OcEnQEIujjYl73vBRx4pp9kYKyvaDm3rIjWeE7w9BTfeMToI...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.encrypted_regex` | `^(data|stringData)$` | Set intentionally to match this repository's desired-state for this component. |
| `sops.mac_only_encrypted` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `sops.version` | `3.11.0` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
