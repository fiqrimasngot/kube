# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `certificate.yaml`
- `helmrelease.yaml`
- `kustomization.yaml`
- `secret.sops.yaml`

## `certificate.yaml` values

### Document 1: `Certificate` `smtp-relay`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `cert-manager.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Certificate` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `smtp-relay` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.secretName` | `tls.smtp-relay` | Set intentionally to match this repository's desired-state for this component. |
| `spec.issuerRef.name` | `letsencrypt-production` | Set intentionally to match this repository's desired-state for this component. |
| `spec.issuerRef.kind` | `ClusterIssuer` | Set intentionally to match this repository's desired-state for this component. |
| `spec.commonName` | `smtp.${SECRET_DOMAIN}` | Set intentionally to match this repository's desired-state for this component. |
| `spec.dnsNames` | `['smtp.${SECRET_DOMAIN}']` | Set intentionally to match this repository's desired-state for this component. |
| `spec.privateKey.rotationPolicy` | `Always` | Set intentionally to match this repository's desired-state for this component. |


## `helmrelease.yaml` values

### Document 1: `HelmRelease` `smtp-relay`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `smtp-relay` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `1h` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.chartRef.kind` | `OCIRepository` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.chartRef.name` | `app-template` | Binds this release to a known source object so artifact resolution is deterministic. |
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
| `resources` | `['./helmrelease.yaml', './certificate.yaml', './secret.sops.yaml']` | Defines which child manifests are composed together as this deployment unit. |
| `configMapGenerator` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `configMapGenerator.[0].name` | `smtp-relay-configmap` | Set intentionally to match this repository's desired-state for this component. |
| `generatorOptions.disableNameSuffixHash` | `True` | Enabled because this behavior is required for reliable operation in this environment. |


## `secret.sops.yaml` values

### Document 1: `Secret` `smtp-relay-secret`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Secret` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `smtp-relay-secret` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `type` | `Opaque` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.SMTP_RELAY_USERNAME` | `ENC[AES256_GCM,data:5SNhKT6PwS+5hsxBL6tRMZXRoRY20Q==,iv:G7RFJhX8U4kIgYsxbo35+6qAFbchnbE...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.SMTP_RELAY_PASSWORD` | `ENC[AES256_GCM,data:O7Q1snnVlJ/WK8CoAM/avHCE3vmC+kHtJsz0t98ACo+tRENz5dvJdqitV6XzS8/hBWw...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].recipient` | `age1sumyxgm2je4txw82k838698mmqmf40wsw6j8eu3jhf5v54g4sslqpchxuf` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].enc` | `-----BEGIN AGE ENCRYPTED FILE----- YWdlLWVuY3J5cHRpb24ub3JnL3YxCi0+IFgyNTUxOSAvTkE3Q1ow...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.lastmodified` | `2026-02-17T11:15:05Z` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `sops.mac` | `ENC[AES256_GCM,data:acsarT2dPO95q2/NG6Nnk8vDDDFNdBb9iqL4u8NXKgCjQq3uIn9XyNshfyXScISB0hQ...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.encrypted_regex` | `^(data|stringData)$` | Set intentionally to match this repository's desired-state for this component. |
| `sops.mac_only_encrypted` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `sops.version` | `3.11.0` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
