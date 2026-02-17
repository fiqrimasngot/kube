# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `alerts.yaml`
- `helmrelease.yaml`
- `kustomization.yaml`

## `alerts.yaml` values

### Document 1: `PrometheusRule` `gpu.rules`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `monitoring.coreos.com/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `PrometheusRule` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `gpu.rules` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.groups` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.groups.[0].name` | `dcgm-exporter` | Set intentionally to match this repository's desired-state for this component. |


## `helmrelease.yaml` values

### Document 1: `HelmRepository` `dcgm-exporter`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `source.toolkit.fluxcd.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRepository` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `dcgm-exporter` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `1h` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.url` | `https://nvidia.github.io/dcgm-exporter/helm-charts` | Set intentionally to match this repository's desired-state for this component. |

### Document 2: `HelmRelease` `dcgm-exporter`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `dcgm-exporter` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `15m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.chart.spec.chart` | `dcgm-exporter` | Selects the specific Helm chart that provides this workload. |
| `spec.chart.spec.version` | `4.7.1` | Pins the chart version for repeatable deployments and controlled upgrades. |
| `spec.chart.spec.interval` | `15m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.maxHistory` | `2` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.install.createNamespace` | `True` | Separates this component into the correct tenancy boundary and avoids cross-namespace sprawl. |
| `spec.install.remediation.retries` | `3` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.upgrade.cleanupOnFail` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.upgrade.remediation.retries` | `3` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.values.image.repository` | `nvcr.io/nvidia/k8s/dcgm-exporter` | Fixes the container image used at runtime so behavior is predictable across reconciliations. |
| `spec.values.image.tag` | `3.3.8-3.6.0-ubuntu22.04` | Fixes the container image used at runtime so behavior is predictable across reconciliations. |
| `spec.values.extraEnv.NVIDIA_DRIVER_CAPABILITIES` | `all` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.extraEnv.NVIDIA_VISIBLE_DEVICES` | `all` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.runtimeClassName` | `nvidia` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.serviceMonitor.interval` | `15s` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.values.serviceMonitor.honorLabels` | `True` | Supports selectors, grouping, and operational discoverability. |
| `spec.values.securityContext.privileged` | `True` | Applies runtime hardening to reduce privilege and container escape risk. |
| `spec.values.securityContext.allowPrivilegeEscalation` | `True` | Applies runtime hardening to reduce privilege and container escape risk. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./helmrelease.yaml', './alerts.yaml']` | Defines which child manifests are composed together as this deployment unit. |
