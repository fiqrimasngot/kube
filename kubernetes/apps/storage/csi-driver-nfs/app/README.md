# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `helmrelease.yaml`
- `kustomization.yaml`
- `storageclass.yaml`

## `helmrelease.yaml` values

### Document 1: `HelmRepository` `csi-driver-nfs`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `source.toolkit.fluxcd.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRepository` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `csi-driver-nfs` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `2h` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.url` | `https://raw.githubusercontent.com/kubernetes-csi/csi-driver-nfs/master/charts` | Set intentionally to match this repository's desired-state for this component. |

### Document 2: `HelmRelease` `csi-driver-nfs`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `csi-driver-nfs` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `30m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.chart.spec.chart` | `csi-driver-nfs` | Selects the specific Helm chart that provides this workload. |
| `spec.chart.spec.version` | `4.12.1` | Pins the chart version for repeatable deployments and controlled upgrades. |
| `spec.maxHistory` | `2` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.install.remediation.retries` | `3` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.upgrade.cleanupOnFail` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.upgrade.remediation.retries` | `3` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.uninstall.keepHistory` | `False` | Disabled intentionally to reduce risk, noise, or unnecessary overhead in this environment. |
| `spec.values.externalSnapshotter.enabled` | `False` | Feature toggle chosen to match this environment's operational requirements. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./helmrelease.yaml', './storageclass.yaml']` | Defines which child manifests are composed together as this deployment unit. |


## `storageclass.yaml` values

### Document 1: `StorageClass` `nfs-csi`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `storage.k8s.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `StorageClass` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `nfs-csi` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `provisioner` | `nfs.csi.k8s.io` | Set intentionally to match this repository's desired-state for this component. |
| `parameters.server` | `${SECRET_NFS_SVC}` | Set intentionally to match this repository's desired-state for this component. |
| `parameters.share` | `/` | Set intentionally to match this repository's desired-state for this component. |
| `reclaimPolicy` | `Delete` | Set intentionally to match this repository's desired-state for this component. |
| `volumeBindingMode` | `Immediate` | Set intentionally to match this repository's desired-state for this component. |
| `mountOptions` | `['hard', 'noatime']` | Set intentionally to match this repository's desired-state for this component. |
