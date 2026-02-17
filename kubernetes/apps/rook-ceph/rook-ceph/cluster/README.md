# cluster manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `helmrelease.yaml`
- `kustomization.yaml`
- `prometheusrule.yaml`

## `helmrelease.yaml` values

### Document 1: `OCIRepository` `rook-ceph-cluster`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `source.toolkit.fluxcd.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `OCIRepository` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `rook-ceph-cluster` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `15m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.layerSelector.mediaType` | `application/vnd.cncf.helm.chart.content.v1.tar+gzip` | Set intentionally to match this repository's desired-state for this component. |
| `spec.layerSelector.operation` | `copy` | Set intentionally to match this repository's desired-state for this component. |
| `spec.ref.tag` | `v1.18.8` | Locks the application version to avoid unexpected upstream changes. |
| `spec.url` | `oci://ghcr.io/rook/rook-ceph-cluster` | Set intentionally to match this repository's desired-state for this component. |

### Document 2: `HelmRelease` `rook-ceph-cluster`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `rook-ceph-cluster` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.chartRef.kind` | `OCIRepository` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.chartRef.name` | `rook-ceph-cluster` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.interval` | `1h` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.values.monitoring.enabled` | `True` | Feature toggle chosen to match this environment's operational requirements. |
| `spec.values.monitoring.createPrometheusRules` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.values.toolbox.enabled` | `True` | Feature toggle chosen to match this environment's operational requirements. |
| `spec.values.cephBlockPools` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.cephBlockPools.[0].name` | `ceph-blockpool` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.cephBlockPoolsVolumeSnapshotClass.enabled` | `True` | Feature toggle chosen to match this environment's operational requirements. |
| `spec.values.cephBlockPoolsVolumeSnapshotClass.name` | `csi-ceph-blockpool` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.cephBlockPoolsVolumeSnapshotClass.isDefault` | `False` | Disabled intentionally to reduce risk, noise, or unnecessary overhead in this environment. |
| `spec.values.cephBlockPoolsVolumeSnapshotClass.deletionPolicy` | `Delete` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.cephFileSystems` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.cephFileSystems.[0].name` | `ceph-filesystem` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.cephFileSystemVolumeSnapshotClass.enabled` | `True` | Feature toggle chosen to match this environment's operational requirements. |
| `spec.values.cephFileSystemVolumeSnapshotClass.name` | `csi-ceph-filesystem` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.cephFileSystemVolumeSnapshotClass.isDefault` | `False` | Disabled intentionally to reduce risk, noise, or unnecessary overhead in this environment. |
| `spec.values.cephFileSystemVolumeSnapshotClass.deletionPolicy` | `Delete` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.cephObjectStores` | `[]` | Set intentionally to match this repository's desired-state for this component. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./helmrelease.yaml', './prometheusrule.yaml']` | Defines which child manifests are composed together as this deployment unit. |


## `prometheusrule.yaml` values

### Document 1: `PrometheusRule` `ceph-diagnostic-alerts`

- `metadata.namespace`: `rook-ceph` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `monitoring.coreos.com/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `PrometheusRule` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `ceph-diagnostic-alerts` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.groups` | `list[3]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.groups.[0].name` | `ceph.disk-io` | Set intentionally to match this repository's desired-state for this component. |
| `spec.groups.[0].interval` | `30s` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
