# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `helmrelease.yaml`
- `kustomization.yaml`
- `kustomizeconfig.yaml`
- `secret.sops.yaml`

## `helmrelease.yaml` values

### Document 1: `HelmRelease` `steam`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `steam` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `30m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.chartRef.kind` | `OCIRepository` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.chartRef.name` | `app-template` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.install.remediation.retries` | `3` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.upgrade.cleanupOnFail` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.upgrade.remediation.strategy` | `rollback` | Set intentionally to match this repository's desired-state for this component. |
| `spec.upgrade.remediation.retries` | `3` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.values.defaultPodOptions.runtimeClassName` | `nvidia` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.defaultPodOptions.hostNetwork` | `True` | Routes traffic or integration calls to the intended DNS endpoint. |
| `spec.values.defaultPodOptions.tolerations` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.defaultPodOptions.tolerations.[0].key` | `nvidia.com/gpu` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.defaultPodOptions.tolerations.[0].operator` | `Exists` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.defaultPodOptions.tolerations.[0].effect` | `NoSchedule` | Set intentionally to match this repository's desired-state for this component. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['secret.sops.yaml', 'helmrelease.yaml']` | Defines which child manifests are composed together as this deployment unit. |
| `configMapGenerator` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `configMapGenerator.[0].name` | `steam-init-scripts` | Set intentionally to match this repository's desired-state for this component. |
| `configurations` | `['kustomizeconfig.yaml']` | Set intentionally to match this repository's desired-state for this component. |


## `kustomizeconfig.yaml` values

### Document 1: `Unknown` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `nameReference` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `nameReference.[0].kind` | `ConfigMap` | Set intentionally to match this repository's desired-state for this component. |
| `nameReference.[0].version` | `v1` | Set intentionally to match this repository's desired-state for this component. |


## `secret.sops.yaml` values

### Document 1: `Secret` `steam`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Secret` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `steam` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `type` | `Opaque` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.USER_PASSWORD` | `ENC[AES256_GCM,data:Esah2L/J,iv:nysND843mpDHEQL6eA7+GpzFYZ3wLGhPKRZFNHPW0Jk=,tag:emQkw0...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.SUNSHINE_USER` | `ENC[AES256_GCM,data:WzUgaQ==,iv:/jpA6mWC+ihG9HAEhndSPcyLcY4HVNpS+RzJCmHfB78=,tag:LKnBWh...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.SUNSHINE_PASS` | `ENC[AES256_GCM,data:ItE3nA==,iv:IiCnxuyq8YPkgvgXMqgbVUc1kxtMziMqUBmrndxQKZk=,tag:Z29tkK...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].recipient` | `age1sumyxgm2je4txw82k838698mmqmf40wsw6j8eu3jhf5v54g4sslqpchxuf` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].enc` | `-----BEGIN AGE ENCRYPTED FILE----- YWdlLWVuY3J5cHRpb24ub3JnL3YxCi0+IFgyNTUxOSA4bVJvM0xs...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.lastmodified` | `2026-02-17T11:15:06Z` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `sops.mac` | `ENC[AES256_GCM,data:Oqeu1BETjYPNyj6k99Tx4XiewfF4p+TIZ153Fr1OTm0jzuH9tAwPW7Hb1N6uIQiSq0P...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.encrypted_regex` | `^(data|stringData)$` | Set intentionally to match this repository's desired-state for this component. |
| `sops.mac_only_encrypted` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `sops.version` | `3.11.0` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
