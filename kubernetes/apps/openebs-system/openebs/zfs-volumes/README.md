# zfs-volumes manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `backups.yaml`
- `doc.yaml`
- `kustomization.yaml`
- `media.yaml`
- `photos.yaml`

## `backups.yaml` values

### Document 1: `ZFSVolume` `backups`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `zfs.openebs.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `ZFSVolume` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `backups` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `metadata.finalizers` | `['cluster.local/data-protection']` | Set intentionally to match this repository's desired-state for this component. |
| `spec.capacity` | `2199023255552` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.fsType` | `zfs` | Set intentionally to match this repository's desired-state for this component. |
| `spec.ownerNodeID` | `k8s-0` | Set intentionally to match this repository's desired-state for this component. |
| `spec.poolName` | `k8s-0-library` | Set intentionally to match this repository's desired-state for this component. |
| `spec.volumeType` | `DATASET` | Set intentionally to match this repository's desired-state for this component. |
| `spec.shared` | `no` | Set intentionally to match this repository's desired-state for this component. |
| `spec.thinProvision` | `yes` | Set intentionally to match this repository's desired-state for this component. |


## `doc.yaml` values

### Document 1: `ZFSVolume` `doc`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `zfs.openebs.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `ZFSVolume` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `doc` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `metadata.finalizers` | `['cluster.local/data-protection']` | Set intentionally to match this repository's desired-state for this component. |
| `spec.capacity` | `1099511627776` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.fsType` | `zfs` | Set intentionally to match this repository's desired-state for this component. |
| `spec.ownerNodeID` | `k8s-0` | Set intentionally to match this repository's desired-state for this component. |
| `spec.poolName` | `k8s-0-library` | Set intentionally to match this repository's desired-state for this component. |
| `spec.volumeType` | `DATASET` | Set intentionally to match this repository's desired-state for this component. |
| `spec.shared` | `no` | Set intentionally to match this repository's desired-state for this component. |
| `spec.thinProvision` | `yes` | Set intentionally to match this repository's desired-state for this component. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./backups.yaml', './doc.yaml', './media.yaml', './photos.yaml']` | Defines which child manifests are composed together as this deployment unit. |


## `media.yaml` values

### Document 1: `ZFSVolume` `media`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `zfs.openebs.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `ZFSVolume` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `media` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `metadata.finalizers` | `['cluster.local/data-protection']` | Set intentionally to match this repository's desired-state for this component. |
| `spec.capacity` | `4398046511104` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.fsType` | `zfs` | Set intentionally to match this repository's desired-state for this component. |
| `spec.ownerNodeID` | `k8s-0` | Set intentionally to match this repository's desired-state for this component. |
| `spec.poolName` | `bigboi` | Set intentionally to match this repository's desired-state for this component. |
| `spec.volumeType` | `DATASET` | Set intentionally to match this repository's desired-state for this component. |
| `spec.shared` | `no` | Set intentionally to match this repository's desired-state for this component. |
| `spec.thinProvision` | `yes` | Set intentionally to match this repository's desired-state for this component. |


## `photos.yaml` values

### Document 1: `ZFSVolume` `photos`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `zfs.openebs.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `ZFSVolume` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `photos` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `metadata.finalizers` | `['cluster.local/data-protection']` | Set intentionally to match this repository's desired-state for this component. |
| `spec.capacity` | `2199023255552` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.fsType` | `zfs` | Set intentionally to match this repository's desired-state for this component. |
| `spec.ownerNodeID` | `k8s-0` | Set intentionally to match this repository's desired-state for this component. |
| `spec.poolName` | `k8s-0-library` | Set intentionally to match this repository's desired-state for this component. |
| `spec.volumeType` | `DATASET` | Set intentionally to match this repository's desired-state for this component. |
| `spec.shared` | `no` | Set intentionally to match this repository's desired-state for this component. |
| `spec.thinProvision` | `yes` | Set intentionally to match this repository's desired-state for this component. |
