# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `helmrelease.yaml`
- `kustomization.yaml`
- `secrets.sops.yaml`

## `helmrelease.yaml` values

### Document 1: `HelmRepository` `cloudnative-pg`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `source.toolkit.fluxcd.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRepository` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `cloudnative-pg` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `2h` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.url` | `https://cloudnative-pg.github.io/charts` | Set intentionally to match this repository's desired-state for this component. |

### Document 2: `HelmRelease` `cloudnative-pg`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `cloudnative-pg` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `30m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.chart.spec.chart` | `cloudnative-pg` | Selects the specific Helm chart that provides this workload. |
| `spec.chart.spec.version` | `0.27.0` | Pins the chart version for repeatable deployments and controlled upgrades. |
| `spec.maxHistory` | `2` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.install.remediation.retries` | `3` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.upgrade.cleanupOnFail` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.upgrade.remediation.retries` | `3` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.uninstall.keepHistory` | `False` | Disabled intentionally to reduce risk, noise, or unnecessary overhead in this environment. |
| `spec.values.crds.create` | `True` | Enabled because this behavior is required for reliable operation in this environment. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./helmrelease.yaml', './secrets.sops.yaml']` | Defines which child manifests are composed together as this deployment unit. |


## `secrets.sops.yaml` values

### Document 1: `Secret` `cloudnative-pg`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Secret` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `cloudnative-pg` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `metadata.labels.cnpg.io/reload` | `true` | Supports selectors, grouping, and operational discoverability. |
| `stringData.aws-access-key-id` | `ENC[AES256_GCM,data:a29cxPR1GcW8QoT1TNXQ4+MtMwQ=,iv:zdA1bhPPCuMxBDZ738hjHJy304jAVw0Cx+Z...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.aws-secret-access-key` | `ENC[AES256_GCM,data:XN13xsn12MM4tF+xikDJmZxQ7PQBr9ETNhl++kMoW8EisGGpUfjD6Q==,iv:tdBdfh6...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.username` | `ENC[AES256_GCM,data:vBpOxu6bqtQ=,iv:yhgnvlQK9xIrwdgF2+pqA9EcaYtL1O2Ntm4rA0TDKCM=,tag:3l...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.password` | `ENC[AES256_GCM,data:EbmYY6gEZ4b8wck=,iv:bOkBNvE4qcrN+kENRyQY2H1EBoSgugEYLkhqLH94ue8=,ta...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].recipient` | `age1sumyxgm2je4txw82k838698mmqmf40wsw6j8eu3jhf5v54g4sslqpchxuf` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].enc` | `-----BEGIN AGE ENCRYPTED FILE----- YWdlLWVuY3J5cHRpb24ub3JnL3YxCi0+IFgyNTUxOSBCQ1plbkRN...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.lastmodified` | `2026-02-17T11:15:04Z` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `sops.mac` | `ENC[AES256_GCM,data:3WR7aQ8eleIhtI0jgN8qneB4RPLvognuL8eVw0zPq19xy+iqUgyzkaf3X+MZQvExmJx...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.encrypted_regex` | `^(data|stringData)$` | Set intentionally to match this repository's desired-state for this component. |
| `sops.mac_only_encrypted` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `sops.version` | `3.11.0` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
