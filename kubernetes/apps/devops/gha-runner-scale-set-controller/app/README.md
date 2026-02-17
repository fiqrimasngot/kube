# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `helmrelease.yaml`
- `kustomization.yaml`
- `secrets.sops.yaml`

## `helmrelease.yaml` values

### Document 1: `HelmRepository` `actions-runner-controller`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `source.toolkit.fluxcd.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRepository` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `actions-runner-controller` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.type` | `oci` | Set intentionally to match this repository's desired-state for this component. |
| `spec.interval` | `5m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.url` | `oci://ghcr.io/actions/actions-runner-controller-charts` | Set intentionally to match this repository's desired-state for this component. |

### Document 2: `HelmRelease` `actions-runner-controller`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `actions-runner-controller` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `30m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.chart.spec.chart` | `gha-runner-scale-set-controller` | Selects the specific Helm chart that provides this workload. |
| `spec.chart.spec.version` | `0.13.0` | Pins the chart version for repeatable deployments and controlled upgrades. |
| `spec.install.crds` | `CreateReplace` | Set intentionally to match this repository's desired-state for this component. |
| `spec.install.remediation.retries` | `3` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.upgrade.cleanupOnFail` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.upgrade.crds` | `CreateReplace` | Set intentionally to match this repository's desired-state for this component. |
| `spec.upgrade.remediation.retries` | `3` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.uninstall.keepHistory` | `False` | Disabled intentionally to reduce risk, noise, or unnecessary overhead in this environment. |
| `spec.values.fullnameOverride` | `gha-runner-scale-set-controller` | Set intentionally to match this repository's desired-state for this component. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./secrets.sops.yaml', './helmrelease.yaml']` | Defines which child manifests are composed together as this deployment unit. |


## `secrets.sops.yaml` values

### Document 1: `Secret` `actions-runner-controller-auth-secrets`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Secret` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `actions-runner-controller-auth-secrets` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `stringData.ACTION_RUNNER_CONTROLLER_GITHUB_APP_ID` | `ENC[AES256_GCM,data:JQRx/99y,iv:RgQ1jW4mI6TP8fIuRsuwyo/irii7wi6J5NP4v30KyJI=,tag:X0LyEK...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.ACTION_RUNNER_CONTROLLER_GITHUB_INSTALLATION_ID` | `ENC[AES256_GCM,data:lrJf/A88DpY=,iv:xuLrKN+C6EjuAZpvAcLOceG66ue7P8CkODDiciICKdA=,tag:pj...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.ACTION_RUNNER_CONTROLLER_GITHUB_WEBHOOK_SECRET_TOKEN` | `ENC[AES256_GCM,data:/eRK2hB8xU2A1X7fpSVWQdkb/6X9b6pf5ynOVO9PTTg=,iv:kbzjZf7tJgvBF/ZTGkY...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.ACTION_RUNNER_CONTROLLER_GITHUB_PRIVATE_KEY` | `ENC[AES256_GCM,data:U+JL6DLzBzUwnu3BJpDNQ9QTgAeb4TofcbEgZt7UaKCJogyg/ErwgbOrNNuCBfyHb/q...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].recipient` | `age1sumyxgm2je4txw82k838698mmqmf40wsw6j8eu3jhf5v54g4sslqpchxuf` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].enc` | `-----BEGIN AGE ENCRYPTED FILE----- YWdlLWVuY3J5cHRpb24ub3JnL3YxCi0+IFgyNTUxOSBTZXpKR1BZ...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.lastmodified` | `2026-02-17T11:15:04Z` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `sops.mac` | `ENC[AES256_GCM,data:9FgBAAEZ+uZlno4nWyOfmTMXcEYR2q/OIWeJtqRnFskCO2BP8vnrscMYOS2RHFyvVtj...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.encrypted_regex` | `^(data|stringData)$` | Set intentionally to match this repository's desired-state for this component. |
| `sops.mac_only_encrypted` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `sops.version` | `3.11.0` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
