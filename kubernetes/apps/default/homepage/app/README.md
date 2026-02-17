# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `helmrelease.yaml`
- `kustomization.yaml`
- `rbac.yaml`

## `helmrelease.yaml` values

### Document 1: `HelmRelease` `homepage`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `homepage` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `30m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.chartRef.kind` | `OCIRepository` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.chartRef.name` | `app-template` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.install.remediation.retries` | `3` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.upgrade.cleanupOnFail` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.upgrade.remediation.strategy` | `rollback` | Set intentionally to match this repository's desired-state for this component. |
| `spec.upgrade.remediation.retries` | `3` | Allows automatic recovery from transient pull/network/startup failures. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./helmrelease.yaml']` | Defines which child manifests are composed together as this deployment unit. |
| `configMapGenerator` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `configMapGenerator.[0].name` | `homepage-config` | Set intentionally to match this repository's desired-state for this component. |
| `generatorOptions.disableNameSuffixHash` | `True` | Enabled because this behavior is required for reliable operation in this environment. |


## `rbac.yaml` values

### Document 1: `ClusterRole` `homepage`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `rbac.authorization.k8s.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `ClusterRole` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `homepage` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `metadata.labels.app.kubernetes.io/instance` | `homepage` | Supports selectors, grouping, and operational discoverability. |
| `metadata.labels.app.kubernetes.io/name` | `homepage` | Supports selectors, grouping, and operational discoverability. |
| `rules` | `list[4]` | Set intentionally to match this repository's desired-state for this component. |

### Document 2: `ClusterRoleBinding` `homepage`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `rbac.authorization.k8s.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `ClusterRoleBinding` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `homepage` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `roleRef.apiGroup` | `rbac.authorization.k8s.io` | Set intentionally to match this repository's desired-state for this component. |
| `roleRef.kind` | `ClusterRole` | Set intentionally to match this repository's desired-state for this component. |
| `roleRef.name` | `homepage` | Set intentionally to match this repository's desired-state for this component. |
| `subjects` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `subjects.[0].kind` | `ServiceAccount` | Set intentionally to match this repository's desired-state for this component. |
| `subjects.[0].name` | `homepage` | Set intentionally to match this repository's desired-state for this component. |
| `subjects.[0].namespace` | `default` | Separates this component into the correct tenancy boundary and avoids cross-namespace sprawl. |
