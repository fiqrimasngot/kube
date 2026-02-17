# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `helmrelease.yaml`
- `kustomization.yaml`
- `secrets.sops.yaml`

## `helmrelease.yaml` values

### Document 1: `HelmRelease` `paperless`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `paperless` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `15m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.chartRef.kind` | `OCIRepository` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.chartRef.name` | `app-template` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.install.remediation.retries` | `3` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.upgrade.cleanupOnFail` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
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

### Document 1: `Secret` `paperless`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Secret` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `paperless` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `stringData.INIT_POSTGRES_DBNAME` | `ENC[AES256_GCM,data:xPbhXkOxqgop,iv:q3K+cMPXmHdbQYc+YxlzCJLcZTpD75wSTuWNm4qqHLo=,tag:zC...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.INIT_POSTGRES_HOST` | `ENC[AES256_GCM,data:wd61hLLauqjnF2mEFHmW/3BQb3oqyThmKovO6ki0ZD5YA05MAe4=,iv:SkcpxqvSxwI...` | Routes traffic or integration calls to the intended DNS endpoint. |
| `stringData.INIT_POSTGRES_USER` | `ENC[AES256_GCM,data:f4fsTfy3xIQ=,iv:xeuZdT7fZnFNjRYJfKW+YQMoez1d6Jl2rUKgrhkao30=,tag:zE...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.INIT_POSTGRES_PASS` | `ENC[AES256_GCM,data:NpjJPbGhf8gBKMw=,iv:4LpGC4oI2O083FhroHlrcjibIGzT7Gnp0ogeelIe7y8=,ta...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.INIT_POSTGRES_SUPER_PASS` | `ENC[AES256_GCM,data:RmxGGMQYm3cwNAE=,iv:H67pskz0nZRBOEB9PsfFQ4KwWvBvoxKaziTPAnkpCBo=,ta...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.PAPERLESS_DBPASS` | `ENC[AES256_GCM,data:YyD8grTwOZxoOqI=,iv:IGOIp24Wg4PJ9O7oRD9XZpzXfnUqj84nag7yHeHGoBM=,ta...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.PAPERLESS_DBUSER` | `ENC[AES256_GCM,data:62jGF4fK7lQ=,iv:kUV5HtXMgrRHp9PDc1m5WmvubPLNLo9k6m4egUTmJVY=,tag:XO...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.PAPERLESS_DBNAME` | `ENC[AES256_GCM,data:/U3anGu0HEJn,iv:NfBx4NOCSXgIX0Ba5JyX14gn7iEJWP5GS9Ez0KDi9xg=,tag:Bd...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.PAPERLESS_ADMIN_USER` | `ENC[AES256_GCM,data:JQi8FIIz,iv:u1NL6ACmADo8H4MybSmA42ziGjPLoJexmPjGSJZIJAk=,tag:i9SRVF...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.PAPERLESS_ADMIN_PASSWORD` | `ENC[AES256_GCM,data:hP3xlA==,iv:5saVBVusUREPQXbJqXi9tB7vpMLk6ALxMz/bcVsSRfg=,tag:sdr2dh...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.PAPERLESS_SECRET_KEY` | `ENC[AES256_GCM,data:3gydmD5nXAeRKb6HjQvEllL04TD5S6+/JMhKh6ZbWMM=,iv:eUdCMceUlZfpsoLEnXs...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.PAPERLESS_SOCIALACCOUNT_PROVIDERS` | `ENC[AES256_GCM,data:+H1bASe8/+v4wiRWU4CZo83+xjoWZcUUjOQIiGXAHMGjCWFPL+0GfnQmfBYx4IY90Cn...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].recipient` | `age1sumyxgm2je4txw82k838698mmqmf40wsw6j8eu3jhf5v54g4sslqpchxuf` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].enc` | `-----BEGIN AGE ENCRYPTED FILE----- YWdlLWVuY3J5cHRpb24ub3JnL3YxCi0+IFgyNTUxOSBXNnN0VnFk...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.lastmodified` | `2026-02-17T11:15:05Z` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `sops.mac` | `ENC[AES256_GCM,data:rFc0MLzXHHnsT0vkOVA7gECfVIai3PAeqUbN7Bx2pM+u+bnwyU0QMKvTxxhKb1UwmzG...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.encrypted_regex` | `^(data|stringData)$` | Set intentionally to match this repository's desired-state for this component. |
| `sops.mac_only_encrypted` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
