# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `helmrelease.yaml`
- `kustomization.yaml`
- `secrets.sops.yaml`

## `helmrelease.yaml` values

### Document 1: `HelmRelease` `obsidian-couchdb`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `obsidian-couchdb` | Keeps object identity stable so upgrades and references continue to work predictably. |
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
| `configMapGenerator` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `configMapGenerator.[0].name` | `obsidian-couchdb-configmap` | Set intentionally to match this repository's desired-state for this component. |
| `generatorOptions.disableNameSuffixHash` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `generatorOptions.annotations.kustomize.toolkit.fluxcd.io/substitute` | `disabled` | Adds controller-specific hints/behaviors needed by tooling in this cluster. |


## `secrets.sops.yaml` values

### Document 1: `Secret` `obsidian-couchdb-secret`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Secret` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `obsidian-couchdb-secret` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `type` | `Opaque` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.couchdb-user` | `ENC[AES256_GCM,data:1i1EKtVB,iv:frIe9ovdQdm0Pbhn/+BTKpbreDy2GNOx+dJMHz5jpJE=,tag:vOg85R...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.couchdb-password` | `ENC[AES256_GCM,data:dMQlAHdyQB1T5CDXXA4bI5/P+88=,iv:vjq3SUY76YD5UONwM/96XuF28jr5r9fbs9n...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].recipient` | `age1sumyxgm2je4txw82k838698mmqmf40wsw6j8eu3jhf5v54g4sslqpchxuf` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].enc` | `-----BEGIN AGE ENCRYPTED FILE----- YWdlLWVuY3J5cHRpb24ub3JnL3YxCi0+IFgyNTUxOSB3b3JwaHdh...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.lastmodified` | `2026-02-17T11:15:04Z` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `sops.mac` | `ENC[AES256_GCM,data:IhY3j6lzDhqWnpYP32eOERC3nV1PFF9zVNB76wmnGEEYYOPH61Ey2WiSs+2AaShPYEg...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.encrypted_regex` | `^(data|stringData)$` | Set intentionally to match this repository's desired-state for this component. |
| `sops.mac_only_encrypted` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `sops.version` | `3.11.0` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
