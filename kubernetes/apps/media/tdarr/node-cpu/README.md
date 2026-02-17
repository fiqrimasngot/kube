# node-cpu manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `helmrelease.yaml`
- `hpa.yaml`
- `kustomization.yaml`

## `helmrelease.yaml` values

### Document 1: `HelmRelease` `tdarr-node-cpu`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `tdarr-node-cpu` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `30m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.chartRef.kind` | `OCIRepository` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.chartRef.name` | `app-template` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.install.remediation.retries` | `3` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.upgrade.cleanupOnFail` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.upgrade.remediation.strategy` | `rollback` | Set intentionally to match this repository's desired-state for this component. |
| `spec.upgrade.remediation.retries` | `3` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.values.defaultPodOptions.priorityClassName` | `tdarr-priority` | Set intentionally to match this repository's desired-state for this component. |


## `hpa.yaml` values

### Document 1: `HorizontalPodAutoscaler` `tdarr-node-cpu`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `autoscaling/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HorizontalPodAutoscaler` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `tdarr-node-cpu` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.scaleTargetRef.apiVersion` | `apps/v1` | Set intentionally to match this repository's desired-state for this component. |
| `spec.scaleTargetRef.kind` | `Deployment` | Set intentionally to match this repository's desired-state for this component. |
| `spec.scaleTargetRef.name` | `tdarr-node-cpu` | Set intentionally to match this repository's desired-state for this component. |
| `spec.minReplicas` | `1` | Sets desired availability versus resource cost for this service. |
| `spec.maxReplicas` | `2` | Sets desired availability versus resource cost for this service. |
| `spec.metrics` | `list[2]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.metrics.[0].type` | `Resource` | Set intentionally to match this repository's desired-state for this component. |
| `spec.behavior.scaleDown.stabilizationWindowSeconds` | `600` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.behavior.scaleDown.policies` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.behavior.scaleDown.policies.[0].type` | `Pods` | Set intentionally to match this repository's desired-state for this component. |
| `spec.behavior.scaleDown.policies.[0].value` | `1` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.behavior.scaleDown.policies.[0].periodSeconds` | `300` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.behavior.scaleUp.stabilizationWindowSeconds` | `30` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.behavior.scaleUp.policies` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.behavior.scaleUp.policies.[0].type` | `Pods` | Set intentionally to match this repository's desired-state for this component. |
| `spec.behavior.scaleUp.policies.[0].value` | `2` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.behavior.scaleUp.policies.[0].periodSeconds` | `120` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.behavior.scaleUp.selectPolicy` | `Max` | Set intentionally to match this repository's desired-state for this component. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['helmrelease.yaml']` | Defines which child manifests are composed together as this deployment unit. |
