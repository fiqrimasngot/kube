# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `helmrelease.yaml`
- `kustomization.yaml`
- `secrets.sops.yaml`

## `helmrelease.yaml` values

### Document 1: `OCIRepository` `openclaw`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `source.toolkit.fluxcd.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `OCIRepository` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `openclaw` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `15m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.layerSelector.mediaType` | `application/vnd.cncf.helm.chart.content.v1.tar+gzip` | Set intentionally to match this repository's desired-state for this component. |
| `spec.layerSelector.operation` | `copy` | Set intentionally to match this repository's desired-state for this component. |
| `spec.ref.tag` | `4.6.2` | Locks the application version to avoid unexpected upstream changes. |
| `spec.url` | `oci://ghcr.io/bjw-s-labs/helm/app-template` | Set intentionally to match this repository's desired-state for this component. |

### Document 2: `HelmRelease` `openclaw`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `openclaw` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.chartRef.kind` | `OCIRepository` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.chartRef.name` | `openclaw` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.interval` | `1h` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.install.remediation.retries` | `-1` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.upgrade.cleanupOnFail` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.upgrade.remediation.retries` | `3` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.values.defaultPodOptions.shareProcessNamespace` | `True` | Separates this component into the correct tenancy boundary and avoids cross-namespace sprawl. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./helmrelease.yaml', './secrets.sops.yaml']` | Defines which child manifests are composed together as this deployment unit. |


## `secrets.sops.yaml` values

### Document 1: `Secret` `openclaw`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Secret` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `openclaw` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `stringData.OPENCLAW_GATEWAY_TOKEN` | `ENC[AES256_GCM,data:0q40heJkpavVCAEsWbP+5sqR5OD1qSjfEZCD+BPpM5g5cpJSMJrxwQ==,iv:gm2v4/j...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.DISCORD_BOT_TOKEN` | `ENC[AES256_GCM,data:HBsRB2tiZgH1rTKi8cIWHzC9b+Vd1+DdguDvMYaB63aDi2p/Fp4E++B7voXQmYBsfcy...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.ANTHROPIC_API_KEY` | `ENC[AES256_GCM,data:sTA72luSwaMs/4jNxkskcb/O0o7a6O0hSni9BI3rEIqN8zCbozh4MbWeIvfUxpLmZh8...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.GH_TOKEN` | `ENC[AES256_GCM,data:LZTeh+l67CcdbE1GT7tRW6ZSo/CRldOxEGn9Iowudv1+UDqEZ/vkpmbWpxbRURn5fQ=...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.openclaw.json` | `ENC[AES256_GCM,data:aYnB3uIkFyQ3PXojUgN2afUUDFTrKNcSkuMf6M/J8A8QwIC74dei8vWChn8zVtGGBMU...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].recipient` | `age1sumyxgm2je4txw82k838698mmqmf40wsw6j8eu3jhf5v54g4sslqpchxuf` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].enc` | `-----BEGIN AGE ENCRYPTED FILE----- YWdlLWVuY3J5cHRpb24ub3JnL3YxCi0+IFgyNTUxOSBsWHVvSXdB...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.lastmodified` | `2026-02-17T11:15:04Z` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `sops.mac` | `ENC[AES256_GCM,data:YlvDcVoJAMoGp+TUJ6+eFpcvV7TzWiP4RV2DYaYPwq8DGEUqQVjyUccCqs6WO5YjBzZ...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.encrypted_regex` | `^(data|stringData)$` | Set intentionally to match this repository's desired-state for this component. |
| `sops.mac_only_encrypted` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `sops.version` | `3.11.0` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
