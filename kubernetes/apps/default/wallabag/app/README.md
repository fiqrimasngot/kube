# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `helmrelease.yaml`
- `kustomization.yaml`
- `secrets.sops.yaml`

## `helmrelease.yaml` values

### Document 1: `HelmRelease` `wallabag`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `wallabag` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `30m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.chartRef.kind` | `OCIRepository` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.chartRef.name` | `app-template` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.maxHistory` | `2` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.install.createNamespace` | `True` | Separates this component into the correct tenancy boundary and avoids cross-namespace sprawl. |
| `spec.install.remediation.retries` | `3` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.upgrade.cleanupOnFail` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.upgrade.remediation.strategy` | `rollback` | Set intentionally to match this repository's desired-state for this component. |
| `spec.upgrade.remediation.retries` | `3` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.uninstall.keepHistory` | `False` | Disabled intentionally to reduce risk, noise, or unnecessary overhead in this environment. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./helmrelease.yaml', './secrets.sops.yaml']` | Defines which child manifests are composed together as this deployment unit. |


## `secrets.sops.yaml` values

### Document 1: `Secret` `wallabag`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Secret` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `wallabag` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `stringData.INIT_POSTGRES_DBNAME` | `ENC[AES256_GCM,data:anZ9FAA0Qgo=,iv:w3E+VkO/VtHWxVVNWQD81ztzJtJH5nJlz/5WI4gmdXM=,tag:yM...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.INIT_POSTGRES_HOST` | `ENC[AES256_GCM,data:pKpkpNPqJ8otvIyS0lwyJ5cuhWEd0z5Fcsfv0oEEn4Id7E2rNNk=,iv:8prCcNv4IfA...` | Routes traffic or integration calls to the intended DNS endpoint. |
| `stringData.INIT_POSTGRES_USER` | `ENC[AES256_GCM,data:8LlI0Oeub70=,iv:OwZ5oYN0P8CU2boKuD/P3gKefWkinouqoewYou/LC70=,tag:iC...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.INIT_POSTGRES_PASS` | `ENC[AES256_GCM,data:pwGQHFwu8StfWoc=,iv:51vbufg3rFYs4D8KZh4S2fB9CT++hVoPvupXAVZzdWQ=,ta...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.INIT_POSTGRES_SUPER_PASS` | `ENC[AES256_GCM,data:KILiLKMduYHFLDw=,iv:nEH4hMtBM9G6eOvYNl1amHGIMhGVT3cOdz5xHkKOXo0=,ta...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.SYMFONY__ENV__DATABASE_DRIVER` | `ENC[AES256_GCM,data:1Wo3HBDJqUaP,iv:YHqsd29bGkeRmJVX/cR1M78c2AJvOzlUKqRxzkeleSw=,tag:Eh...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.SYMFONY__ENV__DATABASE_HOST` | `ENC[AES256_GCM,data:FWgwNMTFB2s7vgEYt8SmfpTWhliYDvcyw+RH55GgQGMtozU/icQ=,iv:Bf6ca6GQpVg...` | Routes traffic or integration calls to the intended DNS endpoint. |
| `stringData.SYMFONY__ENV__DATABASE_PORT` | `ENC[AES256_GCM,data:TjygZg==,iv:/3ew+thnbHKVj4XALiAvfK4idERzyk14KSQV/p1GErQ=,tag:jiTQl6...` | Uses the network port expected by clients, probes, or upstream services. |
| `stringData.SYMFONY__ENV__DATABASE_NAME` | `ENC[AES256_GCM,data:KFq/jHJ6lns=,iv:pIbWBs/YXlQCZ8tSfJ2HyDQTypspS4vGiAP3VoZp/qs=,tag:/8...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.SYMFONY__ENV__DATABASE_USER` | `ENC[AES256_GCM,data:MhZUi7xjvfc=,iv:4L9u0FxBsoqzilAV+mnfPGZIGo4SP3eIyCsYB8Wh3XY=,tag:ra...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.SYMFONY__ENV__DATABASE_PASSWORD` | `ENC[AES256_GCM,data:0KNirlV2L9jXWxI=,iv:Wjsn2dFhRL8POaobUHm0+E/6mV/RRJZzAH0BP0Wuy3w=,ta...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].recipient` | `age1sumyxgm2je4txw82k838698mmqmf40wsw6j8eu3jhf5v54g4sslqpchxuf` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].enc` | `-----BEGIN AGE ENCRYPTED FILE----- YWdlLWVuY3J5cHRpb24ub3JnL3YxCi0+IFgyNTUxOSBQaXhEY1F2...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.lastmodified` | `2026-02-17T11:15:05Z` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `sops.mac` | `ENC[AES256_GCM,data:aeZSjtuHpQBiwvfeJcTYmHNvIVvZ496+9APPHfLDXClToWTsb5+fT39w1jlhZZ/zyKl...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.encrypted_regex` | `^(data|stringData)$` | Set intentionally to match this repository's desired-state for this component. |
| `sops.mac_only_encrypted` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `sops.version` | `3.11.0` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
