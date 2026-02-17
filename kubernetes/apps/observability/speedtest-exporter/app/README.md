# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `helmrelease.yaml`
- `kustomization.yaml`
- `prometheusrule.yaml`

## `helmrelease.yaml` values

### Document 1: `HelmRelease` `speedtest-exporter`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `speedtest-exporter` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `30m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.chartRef.kind` | `OCIRepository` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.chartRef.name` | `app-template` | Binds this release to a known source object so artifact resolution is deterministic. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./helmrelease.yaml', './prometheusrule.yaml']` | Defines which child manifests are composed together as this deployment unit. |


## `prometheusrule.yaml` values

### Document 1: `PrometheusRule` `speedtest-exporter`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `monitoring.coreos.com/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `PrometheusRule` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `speedtest-exporter` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `metadata.labels.app.kubernetes.io/instance` | `speedtest-exporter` | Supports selectors, grouping, and operational discoverability. |
| `metadata.labels.app.kubernetes.io/name` | `speedtest-exporter` | Supports selectors, grouping, and operational discoverability. |
| `spec.groups` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.groups.[0].name` | `speedtest-exporter` | Set intentionally to match this repository's desired-state for this component. |
