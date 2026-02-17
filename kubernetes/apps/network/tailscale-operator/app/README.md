# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `helmrelease.yaml`
- `kustomization.yaml`
- `secret.sops.yaml`

## `helmrelease.yaml` values

### Document 1: `HelmRepository` `tailscale`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `source.toolkit.fluxcd.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRepository` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `tailscale` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `2h` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.url` | `https://pkgs.tailscale.com/helmcharts` | Set intentionally to match this repository's desired-state for this component. |

### Document 2: `HelmRelease` `tailscale-operator`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `tailscale-operator` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `30m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.chart.spec.chart` | `tailscale-operator` | Selects the specific Helm chart that provides this workload. |
| `spec.chart.spec.version` | `1.94.2` | Pins the chart version for repeatable deployments and controlled upgrades. |
| `spec.chart.spec.interval` | `30m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.values.operatorConfig.hostname` | `tailscale-operator-k3s` | Routes traffic or integration calls to the intended DNS endpoint. |
| `spec.values.apiServerProxyConfig.mode` | `true` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.valuesFrom` | `list[2]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.valuesFrom.[0].kind` | `Secret` | Set intentionally to match this repository's desired-state for this component. |
| `spec.valuesFrom.[0].name` | `operator-oauth` | Set intentionally to match this repository's desired-state for this component. |
| `spec.valuesFrom.[0].valuesKey` | `client_id` | Set intentionally to match this repository's desired-state for this component. |
| `spec.valuesFrom.[0].targetPath` | `oauth.clientId` | Set intentionally to match this repository's desired-state for this component. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['secret.sops.yaml', 'helmrelease.yaml']` | Defines which child manifests are composed together as this deployment unit. |


## `secret.sops.yaml` values

### Document 1: `Secret` `operator-oauth`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Secret` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `operator-oauth` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `type` | `Opaque` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.client_id` | `ENC[AES256_GCM,data:Hmq/F4Ci9b/Kx+2zmd6kQ6A=,iv:sPP6Ytk9DbDhu18ADp4mTqRkYOnZaPCa7xJxvrf...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.client_secret` | `ENC[AES256_GCM,data:cNVh+UroYrl6w3B6Ca2V8SLUaylMoLBKq9XROjWEZJIYFszsFVgxZlf/KD+3osu62wr...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].recipient` | `age1sumyxgm2je4txw82k838698mmqmf40wsw6j8eu3jhf5v54g4sslqpchxuf` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].enc` | `-----BEGIN AGE ENCRYPTED FILE----- YWdlLWVuY3J5cHRpb24ub3JnL3YxCi0+IFgyNTUxOSBFcS9mdHgz...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.lastmodified` | `2026-02-17T11:15:05Z` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `sops.mac` | `ENC[AES256_GCM,data:i8hu/ZppHV97GYM21y2kkL7IzomUkWkgNk3hKpIdxYek23BFXtYnlTXcHMkQ2PienpD...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.encrypted_regex` | `^(data|stringData)$` | Set intentionally to match this repository's desired-state for this component. |
| `sops.mac_only_encrypted` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `sops.version` | `3.11.0` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
