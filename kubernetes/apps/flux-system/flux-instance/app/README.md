# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `helmrelease.yaml`
- `httproute.yaml`
- `kustomization.yaml`
- `ocirepository.yaml`
- `receiver.yaml`
- `secret.sops.yaml`

## `helmrelease.yaml` values

### Document 1: `HelmRelease` `flux-instance`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `flux-instance` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.chartRef.kind` | `OCIRepository` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.chartRef.name` | `flux-instance` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.interval` | `1h` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.values.instance.components` | `['source-controller', 'kustomize-controller', 'helm-controller', 'notification-controll...` | Set intentionally to match this repository's desired-state for this component. |


## `httproute.yaml` values

### Document 1: `HTTPRoute` `github-webhook`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `gateway.networking.k8s.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HTTPRoute` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `github-webhook` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.hostnames` | `['flux-webhook.${SECRET_DOMAIN}']` | Routes traffic or integration calls to the intended DNS endpoint. |
| `spec.parentRefs` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.parentRefs.[0].name` | `envoy-external` | Set intentionally to match this repository's desired-state for this component. |
| `spec.parentRefs.[0].namespace` | `network` | Separates this component into the correct tenancy boundary and avoids cross-namespace sprawl. |
| `spec.parentRefs.[0].sectionName` | `https` | Set intentionally to match this repository's desired-state for this component. |
| `spec.rules` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./helmrelease.yaml', './ocirepository.yaml', './secret.sops.yaml', './httproute.yaml'...` | Defines which child manifests are composed together as this deployment unit. |


## `ocirepository.yaml` values

### Document 1: `OCIRepository` `flux-instance`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `source.toolkit.fluxcd.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `OCIRepository` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `flux-instance` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `15m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.layerSelector.mediaType` | `application/vnd.cncf.helm.chart.content.v1.tar+gzip` | Set intentionally to match this repository's desired-state for this component. |
| `spec.layerSelector.operation` | `copy` | Set intentionally to match this repository's desired-state for this component. |
| `spec.ref.tag` | `0.38.1` | Locks the application version to avoid unexpected upstream changes. |
| `spec.url` | `oci://ghcr.io/controlplaneio-fluxcd/charts/flux-instance` | Set intentionally to match this repository's desired-state for this component. |


## `receiver.yaml` values

### Document 1: `Receiver` `github-webhook`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `notification.toolkit.fluxcd.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Receiver` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `github-webhook` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.type` | `github` | Set intentionally to match this repository's desired-state for this component. |
| `spec.events` | `['ping', 'push']` | Set intentionally to match this repository's desired-state for this component. |
| `spec.secretRef.name` | `github-webhook-token-secret` | Set intentionally to match this repository's desired-state for this component. |
| `spec.resources` | `list[2]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.resources.[0].apiVersion` | `source.toolkit.fluxcd.io/v1` | Set intentionally to match this repository's desired-state for this component. |
| `spec.resources.[0].kind` | `GitRepository` | Set intentionally to match this repository's desired-state for this component. |
| `spec.resources.[0].name` | `flux-system` | Set intentionally to match this repository's desired-state for this component. |
| `spec.resources.[0].namespace` | `flux-system` | Separates this component into the correct tenancy boundary and avoids cross-namespace sprawl. |


## `secret.sops.yaml` values

### Document 1: `Secret` `github-webhook-token-secret`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Secret` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `github-webhook-token-secret` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `stringData.token` | `ENC[AES256_GCM,data:oZ4U+gWLbOfpjMBuWofCXtWrJ72sDqb06iMm/IWSzzI=,iv:3ytrATzii77GG0BiZ6n...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].recipient` | `age1sumyxgm2je4txw82k838698mmqmf40wsw6j8eu3jhf5v54g4sslqpchxuf` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].enc` | `-----BEGIN AGE ENCRYPTED FILE----- YWdlLWVuY3J5cHRpb24ub3JnL3YxCi0+IFgyNTUxOSBTbXBScmxl...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.lastmodified` | `2026-02-17T11:15:04Z` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `sops.mac` | `ENC[AES256_GCM,data:ej818G9VTxMTpU4phS5toCg89f3xLF8FKHZEXBEqgjRTMjbfh1olPuEoQDQQCnzJ5P1...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.encrypted_regex` | `^(data|stringData)$` | Set intentionally to match this repository's desired-state for this component. |
| `sops.mac_only_encrypted` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `sops.version` | `3.11.0` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
