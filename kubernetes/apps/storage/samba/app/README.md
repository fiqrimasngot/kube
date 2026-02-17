# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `helmrelease.yaml`
- `kustomization.yaml`

## `helmrelease.yaml` values

### Document 1: `HelmRelease` `samba`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `samba` | Keeps object identity stable so upgrades and references continue to work predictably. |
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
| `resources` | `['./helmrelease.yaml']` | Defines which child manifests are composed together as this deployment unit. |
