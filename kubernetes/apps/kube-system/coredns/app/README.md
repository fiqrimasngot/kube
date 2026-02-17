# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `helmrelease.yaml`
- `kustomization.yaml`
- `ocirepository.yaml`

## `helmrelease.yaml` values

### Document 1: `HelmRelease` `coredns`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `coredns` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.chartRef.kind` | `OCIRepository` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.chartRef.name` | `coredns` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.interval` | `1h` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.values.fullnameOverride` | `coredns` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.image.repository` | `mirror.gcr.io/coredns/coredns` | Fixes the container image used at runtime so behavior is predictable across reconciliations. |
| `spec.values.k8sAppLabelOverride` | `kube-dns` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.serviceAccount.create` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.values.service.name` | `kube-dns` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.service.clusterIP` | `10.43.0.10` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.values.replicaCount` | `2` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.values.servers` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.servers.[0].port` | `53` | Uses the network port expected by clients, probes, or upstream services. |
| `spec.values.tolerations` | `list[2]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.tolerations.[0].key` | `CriticalAddonsOnly` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.tolerations.[0].operator` | `Exists` | Set intentionally to match this repository's desired-state for this component. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./helmrelease.yaml', './ocirepository.yaml']` | Defines which child manifests are composed together as this deployment unit. |


## `ocirepository.yaml` values

### Document 1: `OCIRepository` `coredns`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `source.toolkit.fluxcd.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `OCIRepository` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `coredns` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `15m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.layerSelector.mediaType` | `application/vnd.cncf.helm.chart.content.v1.tar+gzip` | Set intentionally to match this repository's desired-state for this component. |
| `spec.layerSelector.operation` | `copy` | Set intentionally to match this repository's desired-state for this component. |
| `spec.url` | `oci://ghcr.io/coredns/charts/coredns` | Set intentionally to match this repository's desired-state for this component. |
| `spec.ref.tag` | `1.45.0` | Locks the application version to avoid unexpected upstream changes. |
