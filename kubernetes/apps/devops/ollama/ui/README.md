# ui manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `helmrelease.yaml`
- `kustomization.yaml`
- `secrets.sops.yaml`

## `helmrelease.yaml` values

### Document 1: `HelmRelease` `open-webui`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `open-webui` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.chartRef.kind` | `OCIRepository` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.chartRef.name` | `app-template` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.interval` | `1h` | Uses a reconcile interval that balances configuration freshness with API/controller load. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./helmrelease.yaml', './secrets.sops.yaml']` | Defines which child manifests are composed together as this deployment unit. |


## `secrets.sops.yaml` values

### Document 1: `Secret` `open-webui`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Secret` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `open-webui` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `stringData.OAUTH_CLIENT_ID` | `ENC[AES256_GCM,data:rvVA+f7086NsO5fNsLsH/EsG+DMLagtu9t8rZFuV0UqmYnud8IV+KA==,iv:MVHRwVb...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.OAUTH_CLIENT_SECRET` | `ENC[AES256_GCM,data:6saqSCqhqyhqch7Gz3cQ5N3Oo/DIOAz7qG4nQyuooBrt/EyYQ64E24y9Iy5GR2/kxOk...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.OPENID_PROVIDER_URL` | `ENC[AES256_GCM,data:LTw8HNvFyh1p8OzgVyzl4eXck5UKMACHRj1X8d4hqdMVcOQch0nZUufe2xVuZKPkH8A...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.OPENID_REDIRECT_URI` | `ENC[AES256_GCM,data:utA/EIFiTJHOxXEtJLL2o0f+QDB/gND6fI4MeAxkWscHIqrxbdE52/tRG6o4UQCGUw=...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.DATABASE_HOST` | `ENC[AES256_GCM,data:t6M2j7JcNaokFkXGNC/SDU3iv7pypkZAb2gKaiSN+8dJ83NPAVA=,iv:Nrd6jkI9KRv...` | Routes traffic or integration calls to the intended DNS endpoint. |
| `stringData.DATABASE_NAME` | `ENC[AES256_GCM,data:W/21H7bitzcS7g==,iv:CQtbTOMjrXmIh4CTA4JuzNxYGso2Lk8f/jVQ9KUZDiI=,ta...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.DATABASE_PASSWORD` | `ENC[AES256_GCM,data:eXTaUpIBiwWvAw8=,iv:pc+P8yPyQLR/5gQp1DRhPD6F5fozAgGQlj8bv2YZ7Ho=,ta...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.DATABASE_USER` | `ENC[AES256_GCM,data:eH5H1IVQ8rQ=,iv:WzTgFnXC3njIoZ601PGsCBZIpj06p7QBkSEyaupX7mE=,tag:SU...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.WEBUI_SECRET_KEY` | `ENC[AES256_GCM,data:NRF+2LERWQ/RjhULAM345Uy7QI3dnKuv6D3nQ7RcTz3KyUp9fhO6wUlGRASt+l82Q6F...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.INIT_POSTGRES_DBNAME` | `ENC[AES256_GCM,data:jHEkas3lZ1fPmw==,iv:wj3rHeVHxsWqIZfRgmM4zmqOPPKdTwb01o8teXq0Jw4=,ta...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.INIT_POSTGRES_HOST` | `ENC[AES256_GCM,data:lAKRvAOZbISdRUhHQLVatdQDO2sMTETpesTb4kXboiZQgn/CKyA=,iv:bXTpQZLkgm9...` | Routes traffic or integration calls to the intended DNS endpoint. |
| `stringData.INIT_POSTGRES_USER` | `ENC[AES256_GCM,data:62LdMxa3/mQ=,iv:8sV24eqaWt8hkjniVE+dj2+5KLcLGNjFGZ1AVpUmBhI=,tag:6P...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.INIT_POSTGRES_PASS` | `ENC[AES256_GCM,data:UyLembtFqXMtXvc=,iv:2GxDhyccXC3ymxrws1/Rzsfw0XKEfr4EDPvMXJ039nw=,ta...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.INIT_POSTGRES_SUPER_PASS` | `ENC[AES256_GCM,data:riH1oebkkwUk0gg=,iv:vBou8A2O+ssl6svV2MkHlyz12k5c5o4RqnNGJQiqs1s=,ta...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.INIT_POSTGRES_SUPER_USER` | `ENC[AES256_GCM,data:ps6nNOz8I44=,iv:XYE9MgPuH792Uh2VYThTAXDlC7MGiDDJFvqyxuliqXU=,tag:76...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].recipient` | `age1sumyxgm2je4txw82k838698mmqmf40wsw6j8eu3jhf5v54g4sslqpchxuf` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].enc` | `-----BEGIN AGE ENCRYPTED FILE----- YWdlLWVuY3J5cHRpb24ub3JnL3YxCi0+IFgyNTUxOSBHQ3hFQldo...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.lastmodified` | `2026-02-17T11:15:04Z` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
