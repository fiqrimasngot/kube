# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `helmrelease.yaml`
- `kustomization.yaml`
- `secrets.sops.yaml`

## `helmrelease.yaml` values

### Document 1: `HelmRelease` `pgadmin`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `pgadmin` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `30m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.chartRef.kind` | `OCIRepository` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.chartRef.name` | `app-template` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.maxHistory` | `2` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.install.remediation.retries` | `3` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.upgrade.cleanupOnFail` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.upgrade.remediation.retries` | `3` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.uninstall.keepHistory` | `False` | Disabled intentionally to reduce risk, noise, or unnecessary overhead in this environment. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `database` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./secrets.sops.yaml', './helmrelease.yaml']` | Defines which child manifests are composed together as this deployment unit. |
| `configMapGenerator` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `configMapGenerator.[0].name` | `servers-json` | Set intentionally to match this repository's desired-state for this component. |
| `generatorOptions.disableNameSuffixHash` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `generatorOptions.annotations.kustomize.toolkit.fluxcd.io/substitute` | `disabled` | Adds controller-specific hints/behaviors needed by tooling in this cluster. |


## `secrets.sops.yaml` values

### Document 1: `Secret` `pgadmin`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Secret` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `pgadmin` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `stringData.PGADMIN_DEFAULT_EMAIL` | `ENC[AES256_GCM,data:1eK3TL2aEUnBD3MINIqq0blS,iv:kNbKio5adqWk49xwcEO27CdFuu2dTX/gMOcmCFm...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.PGADMIN_DEFAULT_PASSWORD` | `ENC[AES256_GCM,data:Tyz0CbmSJWNKt84=,iv:EM06rrpUbEWNZl8e/R1vIBNs9leXx/YOJMfAVRcOqbY=,ta...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].recipient` | `age1sumyxgm2je4txw82k838698mmqmf40wsw6j8eu3jhf5v54g4sslqpchxuf` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].enc` | `-----BEGIN AGE ENCRYPTED FILE----- YWdlLWVuY3J5cHRpb24ub3JnL3YxCi0+IFgyNTUxOSBsRTg5Vkdo...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.lastmodified` | `2026-02-17T11:15:04Z` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `sops.mac` | `ENC[AES256_GCM,data:9+U95+t83XmdeHKxUO9QOyVaLOqZtUOF8e8LiFPUgS91lHKiUT5zdNJ8YDVsViLEDyR...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.encrypted_regex` | `^(data|stringData)$` | Set intentionally to match this repository's desired-state for this component. |
| `sops.mac_only_encrypted` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `sops.version` | `3.11.0` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
