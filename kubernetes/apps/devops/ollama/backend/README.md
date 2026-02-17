# backend manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `helmrelease.yaml`
- `kustomization.yaml`

## `helmrelease.yaml` values

### Document 1: `HelmRelease` `ollama`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `ollama` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `30m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.chartRef.kind` | `OCIRepository` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.chartRef.name` | `app-template` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.maxHistory` | `3` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.install.remediation.retries` | `5` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.upgrade.remediation.retries` | `5` | Allows automatic recovery from transient pull/network/startup failures. |

### Document 2: `PersistentVolumeClaim` `ollama-model`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `PersistentVolumeClaim` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `ollama-model` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.accessModes` | `['ReadWriteOnce']` | Matches how many pods/nodes are expected to mount this volume safely. |
| `spec.resources.requests.storage` | `50Gi` | Reserves enough storage for expected data growth and retention. |
| `spec.storageClassName` | `ceph-block` | Targets the storage backend that matches persistence and performance expectations. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./helmrelease.yaml']` | Defines which child manifests are composed together as this deployment unit. |
