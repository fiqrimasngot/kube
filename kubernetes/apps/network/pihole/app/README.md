# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `helmrelease.yaml`
- `kustomization.yaml`
- `secret.sops.yaml`

## `helmrelease.yaml` values

### Document 1: `HelmRepository` `pihole`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `source.toolkit.fluxcd.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRepository` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `pihole` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `2h` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.timeout` | `3m` | Bounds how long reconciliation may run before surfacing failure for faster troubleshooting. |
| `spec.url` | `https://mojo2600.github.io/pihole-kubernetes/` | Set intentionally to match this repository's desired-state for this component. |

### Document 2: `HelmRelease` `pihole`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `pihole` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `15m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.chart.spec.chart` | `pihole` | Selects the specific Helm chart that provides this workload. |
| `spec.chart.spec.version` | `2.35.0` | Pins the chart version for repeatable deployments and controlled upgrades. |
| `spec.maxHistory` | `3` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.install.createNamespace` | `True` | Separates this component into the correct tenancy boundary and avoids cross-namespace sprawl. |
| `spec.install.remediation.retries` | `3` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.upgrade.cleanupOnFail` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.upgrade.remediation.retries` | `3` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.uninstall.keepHistory` | `False` | Disabled intentionally to reduce risk, noise, or unnecessary overhead in this environment. |
| `spec.values.DNS1` | `10.32.1.1` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.values.adlists` | `['https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts', 'https://s3.amazon...` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.doh.enabled` | `True` | Feature toggle chosen to match this environment's operational requirements. |
| `spec.values.doh.name` | `cloudflared` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.doh.repository` | `crazymax/cloudflared` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.doh.tag` | `latest@sha256:7e94afadbc1fca729d4187e566697319a8752e471085f4d86396300e21039508` | Locks the application version to avoid unexpected upstream changes. |
| `spec.values.doh.pullPolicy` | `IfNotPresent` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.admin.existingSecret` | `pihole-dashboard` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.admin.passwordKey` | `password` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.antiaff.avoidRelease` | `pihole1` | Set intentionally to match this repository's desired-state for this component. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./secret.sops.yaml', './helmrelease.yaml']` | Defines which child manifests are composed together as this deployment unit. |


## `secret.sops.yaml` values

### Document 1: `Secret` `pihole-dashboard`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Secret` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `pihole-dashboard` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `stringData.password` | `ENC[AES256_GCM,data:smXH+bEb3lZWMOTS5QZ23Z3J8Iei1O3Of1sG11fDyFw=,iv:6Iu1Kf9LX9329poW3zb...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].recipient` | `age1sumyxgm2je4txw82k838698mmqmf40wsw6j8eu3jhf5v54g4sslqpchxuf` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].enc` | `-----BEGIN AGE ENCRYPTED FILE----- YWdlLWVuY3J5cHRpb24ub3JnL3YxCi0+IFgyNTUxOSBXdlRHd21P...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.lastmodified` | `2026-02-17T11:15:05Z` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `sops.mac` | `ENC[AES256_GCM,data:ji8diDSAJoX3IO+XtdwB29QElHFIEKuTspCU+IM0GG7ju/laIforz4yNUwbs+cc59ia...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.encrypted_regex` | `^(data|stringData)$` | Set intentionally to match this repository's desired-state for this component. |
| `sops.mac_only_encrypted` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `sops.version` | `3.11.0` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
