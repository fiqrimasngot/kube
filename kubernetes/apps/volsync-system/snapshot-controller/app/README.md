# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `helmrelease.yaml`
- `kustomization.yaml`

## `helmrelease.yaml` values

### Document 1: `OCIRepository` `snapshot-controller`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `source.toolkit.fluxcd.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `OCIRepository` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `snapshot-controller` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `15m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.layerSelector.mediaType` | `application/vnd.cncf.helm.chart.content.v1.tar+gzip` | Set intentionally to match this repository's desired-state for this component. |
| `spec.layerSelector.operation` | `copy` | Set intentionally to match this repository's desired-state for this component. |
| `spec.ref.tag` | `4.2.0` | Locks the application version to avoid unexpected upstream changes. |
| `spec.url` | `oci://ghcr.io/piraeusdatastore/helm-charts/snapshot-controller` | Set intentionally to match this repository's desired-state for this component. |

### Document 2: `HelmRelease` `snapshot-controller`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `snapshot-controller` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.chartRef.kind` | `OCIRepository` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.chartRef.name` | `snapshot-controller` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.interval` | `1h` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.values.controller.replicaCount` | `2` | Numeric value tuned for current workload size, reliability, and cluster capacity. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./helmrelease.yaml']` | Defines which child manifests are composed together as this deployment unit. |
