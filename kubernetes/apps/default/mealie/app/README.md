# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `helmrelease.yaml`
- `kustomization.yaml`
- `secrets.sops.yaml`

## `helmrelease.yaml` values

### Document 1: `HelmRelease` `mealie`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `mealie` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `30m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.chartRef.kind` | `OCIRepository` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.chartRef.name` | `app-template` | Binds this release to a known source object so artifact resolution is deterministic. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./helmrelease.yaml', './secrets.sops.yaml']` | Defines which child manifests are composed together as this deployment unit. |


## `secrets.sops.yaml` values

### Document 1: `Secret` `mealie`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `kind` | `Secret` | Declares which Kubernetes object/controller should process this manifest. |
| `apiVersion` | `v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `type` | `Opaque` | Set intentionally to match this repository's desired-state for this component. |
| `metadata.name` | `mealie` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `stringData.POSTGRES_USER` | `ENC[AES256_GCM,data:28E01d2crUA=,iv:0eKkwHKrTtUop96zXO2kIPqCb7BRuQ1SqIJWyhIOrLE=,tag:HH...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.POSTGRES_PASSWORD` | `ENC[AES256_GCM,data:QyZL5zZKIRLfjN4=,iv:K6RFOxt0csDQGtqMc4jM96p3SZtYn9GeiQC6rROMZR8=,ta...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.INIT_POSTGRES_SUPER_PASS` | `ENC[AES256_GCM,data:Q9fjiJFs72Xj6as=,iv:uw995Rl0aY5DwIW/hj5Nvh5PmIS7xDiXOhn+n09MCDk=,ta...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.OIDC_CLIENT_SECRET` | `ENC[AES256_GCM,data:cQnQtYjsW5ab0tW67gLTLaf6dFRKYS+tZuiYtgfwiE6V6trUufqZQM0cVpCD6aeixrk...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].recipient` | `age1sumyxgm2je4txw82k838698mmqmf40wsw6j8eu3jhf5v54g4sslqpchxuf` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].enc` | `-----BEGIN AGE ENCRYPTED FILE----- YWdlLWVuY3J5cHRpb24ub3JnL3YxCi0+IFgyNTUxOSAyai9WZzRP...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.lastmodified` | `2026-02-17T11:15:06Z` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `sops.mac` | `ENC[AES256_GCM,data:JRRIlCq0NTxqiaNYrilMOwyWkZs7+0+Vtr0Wzc3YWK25YGL9X4vgiXgm2hXFiX+eoQV...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.encrypted_regex` | `^(data|stringData)$` | Set intentionally to match this repository's desired-state for this component. |
| `sops.mac_only_encrypted` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `sops.version` | `3.11.0` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
