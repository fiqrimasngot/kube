# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `exports.yaml`
- `helmrelease.yaml`
- `kustomization.yaml`
- `pv.yaml`
- `pvc.yaml`
- `secret.sops.yaml`

## `exports.yaml` values

### Document 1: `ConfigMap` `nfs-exports`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `ConfigMap` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `nfs-exports` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `data.exports` | `/export *(rw,fsid=0,crossmnt,no_root_squash,insecure,no_subtree_check)  /export/media 1...` | Set intentionally to match this repository's desired-state for this component. |


## `helmrelease.yaml` values

### Document 1: `HelmRelease` `nfs-server`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `nfs-server` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `1h` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.maxHistory` | `1` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.chartRef.kind` | `OCIRepository` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.chartRef.name` | `app-template` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.install.timeout` | `2m` | Bounds how long reconciliation may run before surfacing failure for faster troubleshooting. |
| `spec.install.remediation.retries` | `1` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.upgrade.timeout` | `2m` | Bounds how long reconciliation may run before surfacing failure for faster troubleshooting. |
| `spec.upgrade.remediation.retries` | `1` | Allows automatic recovery from transient pull/network/startup failures. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./helmrelease.yaml', './pv.yaml', './pvc.yaml', './exports.yaml']` | Defines which child manifests are composed together as this deployment unit. |


## `pv.yaml` values

### Document 1: `PersistentVolume` `media-pv`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `PersistentVolume` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `media-pv` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.accessModes` | `['ReadWriteOnce']` | Matches how many pods/nodes are expected to mount this volume safely. |
| `spec.capacity.storage` | `4398046511104` | Reserves enough storage for expected data growth and retention. |
| `spec.csi.driver` | `zfs.csi.openebs.io` | Set intentionally to match this repository's desired-state for this component. |
| `spec.csi.fsType` | `zfs` | Set intentionally to match this repository's desired-state for this component. |
| `spec.csi.volumeAttributes.openebs.io/poolname` | `bigboi` | Set intentionally to match this repository's desired-state for this component. |
| `spec.csi.volumeHandle` | `media` | Set intentionally to match this repository's desired-state for this component. |
| `spec.nodeAffinity.required.nodeSelectorTerms` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.persistentVolumeReclaimPolicy` | `Retain` | Set intentionally to match this repository's desired-state for this component. |
| `spec.storageClassName` | `zfs-bigboi` | Targets the storage backend that matches persistence and performance expectations. |
| `spec.volumeMode` | `Filesystem` | Set intentionally to match this repository's desired-state for this component. |

### Document 2: `PersistentVolume` `doc-pv`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `PersistentVolume` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `doc-pv` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.accessModes` | `['ReadWriteOnce']` | Matches how many pods/nodes are expected to mount this volume safely. |
| `spec.capacity.storage` | `4398046511104` | Reserves enough storage for expected data growth and retention. |
| `spec.csi.driver` | `zfs.csi.openebs.io` | Set intentionally to match this repository's desired-state for this component. |
| `spec.csi.fsType` | `zfs` | Set intentionally to match this repository's desired-state for this component. |
| `spec.csi.volumeAttributes.openebs.io/poolname` | `k8s-0-library` | Set intentionally to match this repository's desired-state for this component. |
| `spec.csi.volumeHandle` | `doc` | Set intentionally to match this repository's desired-state for this component. |
| `spec.nodeAffinity.required.nodeSelectorTerms` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.persistentVolumeReclaimPolicy` | `Retain` | Set intentionally to match this repository's desired-state for this component. |
| `spec.storageClassName` | `zfs-k8s-0-library` | Targets the storage backend that matches persistence and performance expectations. |
| `spec.volumeMode` | `Filesystem` | Set intentionally to match this repository's desired-state for this component. |

### Document 3: `PersistentVolume` `photos-pv`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `PersistentVolume` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `photos-pv` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.accessModes` | `['ReadWriteOnce']` | Matches how many pods/nodes are expected to mount this volume safely. |
| `spec.capacity.storage` | `4398046511104` | Reserves enough storage for expected data growth and retention. |
| `spec.csi.driver` | `zfs.csi.openebs.io` | Set intentionally to match this repository's desired-state for this component. |
| `spec.csi.fsType` | `zfs` | Set intentionally to match this repository's desired-state for this component. |
| `spec.csi.volumeAttributes.openebs.io/poolname` | `k8s-0-library` | Set intentionally to match this repository's desired-state for this component. |
| `spec.csi.volumeHandle` | `photos` | Set intentionally to match this repository's desired-state for this component. |
| `spec.nodeAffinity.required.nodeSelectorTerms` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.persistentVolumeReclaimPolicy` | `Retain` | Set intentionally to match this repository's desired-state for this component. |
| `spec.storageClassName` | `zfs-k8s-0-library` | Targets the storage backend that matches persistence and performance expectations. |
| `spec.volumeMode` | `Filesystem` | Set intentionally to match this repository's desired-state for this component. |


## `pvc.yaml` values

### Document 1: `PersistentVolumeClaim` `media`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `PersistentVolumeClaim` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `media` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.volumeName` | `media-pv` | Set intentionally to match this repository's desired-state for this component. |
| `spec.accessModes` | `['ReadWriteOnce']` | Matches how many pods/nodes are expected to mount this volume safely. |
| `spec.resources.requests.storage` | `4Ti` | Reserves enough storage for expected data growth and retention. |
| `spec.storageClassName` | `zfs-bigboi` | Targets the storage backend that matches persistence and performance expectations. |

### Document 2: `PersistentVolumeClaim` `doc`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `PersistentVolumeClaim` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `doc` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.volumeName` | `doc-pv` | Set intentionally to match this repository's desired-state for this component. |
| `spec.accessModes` | `['ReadWriteOnce']` | Matches how many pods/nodes are expected to mount this volume safely. |
| `spec.resources.requests.storage` | `4Ti` | Reserves enough storage for expected data growth and retention. |
| `spec.storageClassName` | `zfs-k8s-0-library` | Targets the storage backend that matches persistence and performance expectations. |

### Document 3: `PersistentVolumeClaim` `photos`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `PersistentVolumeClaim` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `photos` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.volumeName` | `photos-pv` | Set intentionally to match this repository's desired-state for this component. |
| `spec.accessModes` | `['ReadWriteOnce']` | Matches how many pods/nodes are expected to mount this volume safely. |
| `spec.resources.requests.storage` | `2Ti` | Reserves enough storage for expected data growth and retention. |
| `spec.storageClassName` | `zfs-k8s-0-library` | Targets the storage backend that matches persistence and performance expectations. |


## `secret.sops.yaml` values

### Document 1: `Secret` `minio-secret`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Secret` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `minio-secret` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `stringData.MINIO_ROOT_USER` | `ENC[AES256_GCM,data:4BYTS8dn,iv:tnXZ/eEUGsjt9nofgnsOUnoxuP51g2v0FOf6sY7m5bw=,tag:zcsuzo...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.MINIO_ROOT_PASSWORD` | `ENC[AES256_GCM,data:nnhBQwm2qr9FxFJUMADFUqdqSvDuT12i0DWX8YJSIM4=,iv:2PaR2qWV5WltsXaJUXi...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].recipient` | `age1sumyxgm2je4txw82k838698mmqmf40wsw6j8eu3jhf5v54g4sslqpchxuf` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].enc` | `-----BEGIN AGE ENCRYPTED FILE----- YWdlLWVuY3J5cHRpb24ub3JnL3YxCi0+IFgyNTUxOSBuT1RObUhY...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.lastmodified` | `2025-12-28T06:30:19Z` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `sops.mac` | `ENC[AES256_GCM,data:9MoThIST3JQHjk7QfKhNjpFGUZ7AkWf/zpFLpY8tHx9Q/2McThbrRh+7EygVUbaPmP3...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.encrypted_regex` | `^(data|stringData)$` | Set intentionally to match this repository's desired-state for this component. |
| `sops.mac_only_encrypted` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `sops.version` | `3.11.0` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
