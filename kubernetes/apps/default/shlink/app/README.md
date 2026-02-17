# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `helmrelease.yaml`
- `kustomization.yaml`
- `secrets.sops.yaml`

## `helmrelease.yaml` values

### Document 1: `HelmRelease` `shlink`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `shlink` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `30m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.chartRef.kind` | `OCIRepository` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.chartRef.name` | `app-template` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.maxHistory` | `2` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
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
| `resources` | `['./helmrelease.yaml', './secrets.sops.yaml']` | Defines which child manifests are composed together as this deployment unit. |


## `secrets.sops.yaml` values

### Document 1: `Secret` `shlink`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Secret` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `shlink` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `stringData.DB_NAME` | `ENC[AES256_GCM,data:1buw9j2J,iv:BZRcJ9i4rfGRBjkrc61fSMSm3vJuGqnfW6F+6dbxq1c=,tag:a2/Lfy...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.DB_HOST` | `ENC[AES256_GCM,data:mdRCXUG/GA3YN5cYpsSAOiB6IFpeS3Kh2Y4cgg4vakCuii0IFJk=,iv:l9Yb1+KYXMb...` | Routes traffic or integration calls to the intended DNS endpoint. |
| `stringData.DB_PORT` | `ENC[AES256_GCM,data:hyhf/Q==,iv:+T16qcospvKS2PKD1tBD4KHIo+UkYnGy7H/Jt2CJrLU=,tag:YtiAQb...` | Uses the network port expected by clients, probes, or upstream services. |
| `stringData.DB_USER` | `ENC[AES256_GCM,data:7cu4qskJulI=,iv:Euu94K/rqMAMvGMvxLRALpKaucC7CkP1FqcVXA9omGA=,tag:+N...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.DB_PASSWORD` | `ENC[AES256_GCM,data:u3lQRmAW0XwaKjI=,iv:jdIYj8BLBdhA+HzvLaGJ4G6XT3mbH6ybtaMItYgCZ4E=,ta...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.GEOLITE_LICENSE_KEY` | `` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.INIT_POSTGRES_DBNAME` | `ENC[AES256_GCM,data:IlQ/bNwk,iv:9mLPyEd7z+dOxOw2bnbbHcupWokNyklicHmbtpQ/380=,tag:QpU/Mc...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.INIT_POSTGRES_HOST` | `ENC[AES256_GCM,data:1qH/45wtCw1a+N6IYPnHOi7hhf5oTovYNkbeg3T6YyINhdAhxo0=,iv:XfBjg81xBtD...` | Routes traffic or integration calls to the intended DNS endpoint. |
| `stringData.INIT_POSTGRES_USER` | `ENC[AES256_GCM,data:6UJ4sAulABI=,iv:bmDJHEQW1yXx1LgL29HNr3a0FxfUgZZpZ83gX0YVJpI=,tag:kS...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.INIT_POSTGRES_PASS` | `ENC[AES256_GCM,data:x/b8+gV5vf1sZVA=,iv:ToACa7HYBetfkD+OquSnPAcKO1/FHf58Z6+h5PjuRPw=,ta...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.INIT_POSTGRES_PORT` | `ENC[AES256_GCM,data:xpBCFw==,iv:BfHGnFLSlwGnZX33n51UUCTRyy/NxLhLImqEOTkPGac=,tag:UvSBRU...` | Uses the network port expected by clients, probes, or upstream services. |
| `stringData.INIT_POSTGRES_SUPER_PASS` | `ENC[AES256_GCM,data:pdur0C4ffx8PPHM=,iv:Pb+kuH2u2SV1vqsASEnMuIi+G/L35nDzNT4xyb1cA7I=,ta...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].recipient` | `age1sumyxgm2je4txw82k838698mmqmf40wsw6j8eu3jhf5v54g4sslqpchxuf` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].enc` | `-----BEGIN AGE ENCRYPTED FILE----- YWdlLWVuY3J5cHRpb24ub3JnL3YxCi0+IFgyNTUxOSBhTHNsc3Fq...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.lastmodified` | `2026-02-17T11:15:05Z` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `sops.mac` | `ENC[AES256_GCM,data:b60C7S3bKUNqV9WtwwQcQgBSgha0EV0zEOmNoobfRZkgceC8INPnFDaYIBnKUJVwz1e...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.encrypted_regex` | `^(data|stringData)$` | Set intentionally to match this repository's desired-state for this component. |
| `sops.mac_only_encrypted` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
