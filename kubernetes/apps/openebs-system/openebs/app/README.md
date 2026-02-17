# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `helmrelease.yaml`
- `kustomization.yaml`
- `snapshotclass.yaml`
- `storageclass.yaml`

## `helmrelease.yaml` values

### Document 1: `OCIRepository` `openebs`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `source.toolkit.fluxcd.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `OCIRepository` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `openebs` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `1h` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.layerSelector.mediaType` | `application/vnd.cncf.helm.chart.content.v1.tar+gzip` | Set intentionally to match this repository's desired-state for this component. |
| `spec.layerSelector.operation` | `copy` | Set intentionally to match this repository's desired-state for this component. |
| `spec.ref.tag` | `4.4.0` | Locks the application version to avoid unexpected upstream changes. |
| `spec.url` | `oci://ghcr.io/openebs/charts/openebs` | Set intentionally to match this repository's desired-state for this component. |

### Document 2: `HelmRelease` `openebs`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `openebs` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `1h` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.maxHistory` | `1` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.chartRef.kind` | `OCIRepository` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.chartRef.name` | `openebs` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.install.disableHooks` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.install.timeout` | `2m` | Bounds how long reconciliation may run before surfacing failure for faster troubleshooting. |
| `spec.install.remediation.retries` | `1` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.upgrade.disableHooks` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.upgrade.timeout` | `2m` | Bounds how long reconciliation may run before surfacing failure for faster troubleshooting. |
| `spec.upgrade.remediation.retries` | `1` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.values.loki.enabled` | `False` | Feature toggle chosen to match this environment's operational requirements. |
| `spec.values.alloy.enabled` | `False` | Feature toggle chosen to match this environment's operational requirements. |
| `spec.values.localpv-provisioner.enabled` | `True` | Feature toggle chosen to match this environment's operational requirements. |
| `spec.values.zfs-localpv.enabled` | `True` | Feature toggle chosen to match this environment's operational requirements. |
| `spec.values.lvm-localpv.enabled` | `False` | Feature toggle chosen to match this environment's operational requirements. |
| `spec.values.mayastor.enabled` | `False` | Feature toggle chosen to match this environment's operational requirements. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./helmrelease.yaml', './storageclass.yaml']` | Defines which child manifests are composed together as this deployment unit. |


## `snapshotclass.yaml` values

### Document 1: `VolumeSnapshotClass` `openebs-zfs`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `kind` | `VolumeSnapshotClass` | Declares which Kubernetes object/controller should process this manifest. |
| `apiVersion` | `snapshot.storage.k8s.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `metadata.name` | `openebs-zfs` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `driver` | `zfs.csi.openebs.io` | Set intentionally to match this repository's desired-state for this component. |
| `deletionPolicy` | `Delete` | Set intentionally to match this repository's desired-state for this component. |


## `storageclass.yaml` values

### Document 1: `StorageClass` `zfs-k8s-0-library`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `storage.k8s.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `StorageClass` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `zfs-k8s-0-library` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `provisioner` | `zfs.csi.openebs.io` | Set intentionally to match this repository's desired-state for this component. |
| `parameters.poolname` | `k8s-0-library` | Set intentionally to match this repository's desired-state for this component. |
| `parameters.compression` | `lz4` | Set intentionally to match this repository's desired-state for this component. |
| `parameters.recordsize` | `16k` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `volumeBindingMode` | `WaitForFirstConsumer` | Set intentionally to match this repository's desired-state for this component. |
| `reclaimPolicy` | `Delete` | Set intentionally to match this repository's desired-state for this component. |
| `allowVolumeExpansion` | `True` | Enabled because this behavior is required for reliable operation in this environment. |

### Document 2: `StorageClass` `zfs-bigboi`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `storage.k8s.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `StorageClass` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `zfs-bigboi` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `provisioner` | `zfs.csi.openebs.io` | Set intentionally to match this repository's desired-state for this component. |
| `parameters.poolname` | `bigboi` | Set intentionally to match this repository's desired-state for this component. |
| `parameters.compression` | `lz4` | Set intentionally to match this repository's desired-state for this component. |
| `parameters.recordsize` | `16k` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `volumeBindingMode` | `WaitForFirstConsumer` | Set intentionally to match this repository's desired-state for this component. |
| `reclaimPolicy` | `Delete` | Set intentionally to match this repository's desired-state for this component. |
| `allowVolumeExpansion` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
