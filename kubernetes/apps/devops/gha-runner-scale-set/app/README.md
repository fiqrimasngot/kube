# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `helmrelease.yaml`
- `kustomization.yaml`

## `helmrelease.yaml` values

### Document 1: `HelmRelease` `gha-runner-scale-set`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `gha-runner-scale-set` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `30m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.chart.spec.chart` | `gha-runner-scale-set` | Selects the specific Helm chart that provides this workload. |
| `spec.chart.spec.version` | `0.13.0` | Pins the chart version for repeatable deployments and controlled upgrades. |
| `spec.install.remediation.retries` | `3` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.upgrade.cleanupOnFail` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.upgrade.remediation.strategy` | `rollback` | Set intentionally to match this repository's desired-state for this component. |
| `spec.upgrade.remediation.retries` | `3` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.valuesFrom` | `list[3]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.valuesFrom.[0].targetPath` | `githubConfigSecret.github_app_id` | Set intentionally to match this repository's desired-state for this component. |
| `spec.valuesFrom.[0].kind` | `Secret` | Set intentionally to match this repository's desired-state for this component. |
| `spec.valuesFrom.[0].name` | `actions-runner-controller-auth-secrets` | Set intentionally to match this repository's desired-state for this component. |
| `spec.valuesFrom.[0].valuesKey` | `ACTION_RUNNER_CONTROLLER_GITHUB_APP_ID` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.nameOverride` | `gha-runner-scale-set` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.runnerScaleSetName` | `gha-runner-scale-set` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.githubConfigUrl` | `https://github.com/fiqrimasngot/AMD-Global` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.minRunners` | `1` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.values.maxRunners` | `5` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.values.containerMode.type` | `dind` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.controllerServiceAccount.name` | `gha-runner-scale-set-controller` | Set intentionally to match this repository's desired-state for this component. |

### Document 2: `HelmRelease` `gha-web-app`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `gha-web-app` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `30m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.chart.spec.chart` | `gha-runner-scale-set` | Selects the specific Helm chart that provides this workload. |
| `spec.chart.spec.version` | `0.13.0` | Pins the chart version for repeatable deployments and controlled upgrades. |
| `spec.install.remediation.retries` | `3` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.upgrade.cleanupOnFail` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.upgrade.remediation.strategy` | `rollback` | Set intentionally to match this repository's desired-state for this component. |
| `spec.upgrade.remediation.retries` | `3` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.valuesFrom` | `list[3]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.valuesFrom.[0].targetPath` | `githubConfigSecret.github_app_id` | Set intentionally to match this repository's desired-state for this component. |
| `spec.valuesFrom.[0].kind` | `Secret` | Set intentionally to match this repository's desired-state for this component. |
| `spec.valuesFrom.[0].name` | `actions-runner-controller-auth-secrets` | Set intentionally to match this repository's desired-state for this component. |
| `spec.valuesFrom.[0].valuesKey` | `ACTION_RUNNER_CONTROLLER_GITHUB_APP_ID` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.runnerScaleSetName` | `gha-web-app` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.githubConfigUrl` | `https://github.com/fiqrimasngot/school-scheduler` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.minRunners` | `1` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.values.maxRunners` | `5` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.values.containerMode.type` | `dind` | Set intentionally to match this repository's desired-state for this component. |

### Document 3: `HelmRelease` `gha-kube`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `gha-kube` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `30m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.chart.spec.chart` | `gha-runner-scale-set` | Selects the specific Helm chart that provides this workload. |
| `spec.chart.spec.version` | `0.13.0` | Pins the chart version for repeatable deployments and controlled upgrades. |
| `spec.install.remediation.retries` | `3` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.upgrade.cleanupOnFail` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.upgrade.remediation.strategy` | `rollback` | Set intentionally to match this repository's desired-state for this component. |
| `spec.upgrade.remediation.retries` | `3` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.valuesFrom` | `list[3]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.valuesFrom.[0].targetPath` | `githubConfigSecret.github_app_id` | Set intentionally to match this repository's desired-state for this component. |
| `spec.valuesFrom.[0].kind` | `Secret` | Set intentionally to match this repository's desired-state for this component. |
| `spec.valuesFrom.[0].name` | `actions-runner-controller-auth-secrets` | Set intentionally to match this repository's desired-state for this component. |
| `spec.valuesFrom.[0].valuesKey` | `ACTION_RUNNER_CONTROLLER_GITHUB_APP_ID` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.runnerScaleSetName` | `gha-kube` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.githubConfigUrl` | `https://github.com/fiqrimasngot/kube` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.minRunners` | `1` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.values.maxRunners` | `10` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.values.containerMode.type` | `dind` | Set intentionally to match this repository's desired-state for this component. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./helmrelease.yaml']` | Defines which child manifests are composed together as this deployment unit. |
