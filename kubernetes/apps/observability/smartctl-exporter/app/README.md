# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `helmrelease.yaml`
- `kustomization.yaml`
- `prometheusrule.yaml`

## `helmrelease.yaml` values

### Document 1: `OCIRepository` `smartctl-exporter`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `source.toolkit.fluxcd.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `OCIRepository` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `smartctl-exporter` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `5m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.layerSelector.mediaType` | `application/vnd.cncf.helm.chart.content.v1.tar+gzip` | Set intentionally to match this repository's desired-state for this component. |
| `spec.layerSelector.operation` | `copy` | Set intentionally to match this repository's desired-state for this component. |
| `spec.ref.tag` | `0.15.3` | Locks the application version to avoid unexpected upstream changes. |
| `spec.url` | `oci://ghcr.io/prometheus-community/charts/prometheus-smartctl-exporter` | Set intentionally to match this repository's desired-state for this component. |

### Document 2: `HelmRelease` `smartctl-exporter`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `smartctl-exporter` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `1h` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.chartRef.kind` | `OCIRepository` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.chartRef.name` | `smartctl-exporter` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.install.remediation.retries` | `-1` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.upgrade.cleanupOnFail` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.upgrade.remediation.retries` | `3` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.values.fullnameOverride` | `smartctl-exporter` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.serviceMonitor.enabled` | `True` | Feature toggle chosen to match this environment's operational requirements. |
| `spec.values.prometheusRules.enabled` | `False` | Feature toggle chosen to match this environment's operational requirements. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./helmrelease.yaml', './prometheusrule.yaml']` | Defines which child manifests are composed together as this deployment unit. |


## `prometheusrule.yaml` values

### Document 1: `PrometheusRule` `smartctl-exporter-rules`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `monitoring.coreos.com/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `PrometheusRule` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `smartctl-exporter-rules` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.groups` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.groups.[0].name` | `smartctl-exporter.rules` | Set intentionally to match this repository's desired-state for this component. |
