# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `class.yaml`
- `helmrelease.yaml`
- `kustomization.yaml`

## `class.yaml` values

### Document 1: `RuntimeClass` `nvidia`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `node.k8s.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `RuntimeClass` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `nvidia` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `handler` | `nvidia` | Set intentionally to match this repository's desired-state for this component. |


## `helmrelease.yaml` values

### Document 1: `HelmRepository` `nvidia-dvp`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `source.toolkit.fluxcd.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRepository` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `nvidia-dvp` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `30m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.url` | `https://nvidia.github.io/k8s-device-plugin` | Set intentionally to match this repository's desired-state for this component. |
| `spec.timeout` | `3m` | Bounds how long reconciliation may run before surfacing failure for faster troubleshooting. |

### Document 2: `HelmRelease` `nvidia-device-plugin`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `nvidia-device-plugin` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `15m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.chart.spec.chart` | `nvidia-device-plugin` | Selects the specific Helm chart that provides this workload. |
| `spec.chart.spec.version` | `0.18.0` | Pins the chart version for repeatable deployments and controlled upgrades. |
| `spec.install.crds` | `CreateReplace` | Set intentionally to match this repository's desired-state for this component. |
| `spec.install.remediation.retries` | `3` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.upgrade.cleanupOnFail` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.upgrade.crds` | `CreateReplace` | Set intentionally to match this repository's desired-state for this component. |
| `spec.upgrade.remediation.retries` | `3` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.values.runtimeClassName` | `nvidia` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.securityContext.privileged` | `True` | Applies runtime hardening to reduce privilege and container escape risk. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./helmrelease.yaml', './class.yaml']` | Defines which child manifests are composed together as this deployment unit. |
