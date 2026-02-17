# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `helmrelease.yaml`
- `kustomization.yaml`

## `helmrelease.yaml` values

### Document 1: `HelmRepository` `node-feature-discovery`

- `metadata.namespace`: `flux-system` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `source.toolkit.fluxcd.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRepository` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `node-feature-discovery` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `1h` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.url` | `https://kubernetes-sigs.github.io/node-feature-discovery/charts` | Set intentionally to match this repository's desired-state for this component. |

### Document 2: `HelmRelease` `node-feature-discovery`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `node-feature-discovery` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `15m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.chart.spec.chart` | `node-feature-discovery` | Selects the specific Helm chart that provides this workload. |
| `spec.chart.spec.version` | `0.18.3` | Pins the chart version for repeatable deployments and controlled upgrades. |
| `spec.chart.spec.interval` | `15m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.driftDetection.mode` | `enabled` | Set intentionally to match this repository's desired-state for this component. |
| `spec.maxHistory` | `3` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.install.crds` | `CreateReplace` | Set intentionally to match this repository's desired-state for this component. |
| `spec.install.remediation.retries` | `3` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.upgrade.crds` | `CreateReplace` | Set intentionally to match this repository's desired-state for this component. |
| `spec.upgrade.cleanupOnFail` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.upgrade.remediation.retries` | `3` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.values.nodeFeatureRule.createCRD` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.values.prometheus.enable` | `True` | Enabled because this behavior is required for reliable operation in this environment. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./helmrelease.yaml']` | Defines which child manifests are composed together as this deployment unit. |
