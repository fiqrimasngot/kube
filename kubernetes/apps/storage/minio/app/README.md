# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `helmrelease.yaml`
- `kustomization.yaml`
- `secret.sops.yaml`

## `helmrelease.yaml` values

### Document 1: `HelmRelease` `minio`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `minio` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `30m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.chartRef.kind` | `OCIRepository` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.chartRef.name` | `app-template` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.install.remediation.retries` | `3` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.upgrade.cleanupOnFail` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.upgrade.remediation.strategy` | `rollback` | Set intentionally to match this repository's desired-state for this component. |
| `spec.upgrade.remediation.retries` | `3` | Allows automatic recovery from transient pull/network/startup failures. |

### Document 2: `PersistentVolumeClaim` `backups`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `PersistentVolumeClaim` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `backups` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.storageClassName` | `zfs-k8s-0-library` | Targets the storage backend that matches persistence and performance expectations. |
| `spec.accessModes` | `['ReadWriteOnce']` | Matches how many pods/nodes are expected to mount this volume safely. |
| `spec.resources.requests.storage` | `2Ti` | Reserves enough storage for expected data growth and retention. |

### Document 3: `PersistentVolume` `backups-pv`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `PersistentVolume` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `backups-pv` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.accessModes` | `['ReadWriteOnce']` | Matches how many pods/nodes are expected to mount this volume safely. |
| `spec.capacity.storage` | `2199023255552` | Reserves enough storage for expected data growth and retention. |
| `spec.claimRef.apiVersion` | `v1` | Set intentionally to match this repository's desired-state for this component. |
| `spec.claimRef.kind` | `PersistentVolumeClaim` | Set intentionally to match this repository's desired-state for this component. |
| `spec.claimRef.name` | `backups` | Set intentionally to match this repository's desired-state for this component. |
| `spec.claimRef.namespace` | `storage` | Separates this component into the correct tenancy boundary and avoids cross-namespace sprawl. |
| `spec.csi.driver` | `zfs.csi.openebs.io` | Set intentionally to match this repository's desired-state for this component. |
| `spec.csi.fsType` | `zfs` | Set intentionally to match this repository's desired-state for this component. |
| `spec.csi.volumeAttributes.openebs.io/poolname` | `k8s-0-library` | Set intentionally to match this repository's desired-state for this component. |
| `spec.csi.volumeHandle` | `backups` | Set intentionally to match this repository's desired-state for this component. |
| `spec.nodeAffinity.required.nodeSelectorTerms` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.persistentVolumeReclaimPolicy` | `Retain` | Set intentionally to match this repository's desired-state for this component. |
| `spec.storageClassName` | `zfs-k8s-0-library` | Targets the storage backend that matches persistence and performance expectations. |
| `spec.volumeMode` | `Filesystem` | Set intentionally to match this repository's desired-state for this component. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./helmrelease.yaml', './secret.sops.yaml']` | Defines which child manifests are composed together as this deployment unit. |


## `secret.sops.yaml` values

### Document 1: `Secret` `minio-secret`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Secret` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `minio-secret` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `stringData.MINIO_ROOT_USER` | `ENC[AES256_GCM,data:6ifdAJiM,iv:YBRuP1YU5mCqekH6qP8XeQ9MYQny26SWCDiPSIKgWg4=,tag:W6t8ST...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.MINIO_ROOT_PASSWORD` | `ENC[AES256_GCM,data:Lk2b4PnE7G4z64nd7RxSbTkN3DpPfvc0TvchP3RAKM4=,iv:kfCtyu59wJ/tNVdPJTg...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.openid-config-url` | `ENC[AES256_GCM,data:gIs61P7Rxrrw9vo5l4GlMnTedv5GaHfGhrioV8uDcTWtCW5Bf2+lys7oKoKodCQgRhL...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.openid-config-client-id` | `ENC[AES256_GCM,data:wypGq+yoZFCNU844utn+4Bu0T9S1/2zXDSpMINlGAG2+1UBYsQwf1w==,iv:ZpmoTBY...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.openid-config-client-secret` | `ENC[AES256_GCM,data:0dZrDAXtsufik4bv01yxXEfvgWZm31jZkMaM+i9/WtqKH1tSM9H0RYEUT8b4BHYL+e/...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.openid-config-scopes` | `ENC[AES256_GCM,data:K9d6n1e0NKxUKWcseXVlVglm9ZOGITzCZeo=,iv:z26KNHt14BvlZV/G5wci48/2/J8...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.openid-config-callback-uri` | `` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].recipient` | `age1sumyxgm2je4txw82k838698mmqmf40wsw6j8eu3jhf5v54g4sslqpchxuf` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].enc` | `-----BEGIN AGE ENCRYPTED FILE----- YWdlLWVuY3J5cHRpb24ub3JnL3YxCi0+IFgyNTUxOSArWVc5Vy9x...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.lastmodified` | `2026-02-17T11:15:06Z` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `sops.mac` | `ENC[AES256_GCM,data:7II1oKsiTjSyp6162gEtGjmscgTtUFD3mzzhr7H4NrwbWiKe5p6u7ugLeUMBgG1Tz4P...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.encrypted_regex` | `^(data|stringData)$` | Set intentionally to match this repository's desired-state for this component. |
| `sops.mac_only_encrypted` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `sops.version` | `3.11.0` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
