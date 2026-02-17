# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `helmrelease.yaml`
- `kustomization.yaml`

## `helmrelease.yaml` values

### Document 1: `HelmRepository` `strimzi`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `source.toolkit.fluxcd.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRepository` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `strimzi` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `1h` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.url` | `https://strimzi.io/charts/` | Set intentionally to match this repository's desired-state for this component. |

### Document 2: `HelmRelease` `strimzi`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `strimzi` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `30m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.chart.spec.chart` | `strimzi-kafka-operator` | Selects the specific Helm chart that provides this workload. |
| `spec.chart.spec.version` | `0.49.1` | Pins the chart version for repeatable deployments and controlled upgrades. |
| `spec.install.remediation.retries` | `3` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.maxHistory` | `3` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.upgrade.cleanupOnFail` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.upgrade.remediation.retries` | `3` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.uninstall.keepHistory` | `False` | Disabled intentionally to reduce risk, noise, or unnecessary overhead in this environment. |
| `spec.values.fullReconciliationIntervalMs` | `120000` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.values.operationTimeoutMs` | `300000` | Bounds how long reconciliation may run before surfacing failure for faster troubleshooting. |
| `spec.values.kubernetesServiceDnsDomain` | `cluster.local` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.featureGates` | `` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.tmpDirSizeLimit` | `1Mi` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.values.dashboards.enabled` | `False` | Feature toggle chosen to match this environment's operational requirements. |
| `spec.values.livenessProbe.initialDelaySeconds` | `10` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.values.livenessProbe.periodSeconds` | `30` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.values.readinessProbe.initialDelaySeconds` | `10` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.values.readinessProbe.periodSeconds` | `30` | Numeric value tuned for current workload size, reliability, and cluster capacity. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./helmrelease.yaml']` | Defines which child manifests are composed together as this deployment unit. |
