# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `configmap.yaml`
- `helmrelease.yaml`
- `kustomization.yaml`
- `priorityclass.yaml`

## `configmap.yaml` values

### Document 1: `ConfigMap` `tdarr-config`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `ConfigMap` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `tdarr-config` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `data.FFMPEG_PATH` | `/usr/local/bin/ffmpeg` | Set intentionally to match this repository's desired-state for this component. |
| `data.HANDBRAKE_PATH` | `/usr/local/bin/HandBrakeCLI` | Set intentionally to match this repository's desired-state for this component. |
| `data.NODE_WORKER_LIMIT` | `2` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `data.NODE_CONCURRENT_LIMIT` | `1` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `data.SKIP_TRANSCODE_AFTER_ATTEMPTS` | `3` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `data.FILE_SIZE_LIMIT_GB` | `100` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `data.DEFAULT_QUALITY_CRF` | `22` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `data.DEFAULT_PRESET` | `medium` | Set intentionally to match this repository's desired-state for this component. |
| `data.PREFERRED_AUDIO_LANG` | `eng` | Set intentionally to match this repository's desired-state for this component. |
| `data.PREFERRED_SUB_LANG` | `eng` | Set intentionally to match this repository's desired-state for this component. |
| `data.PREFERRED_CONTAINER` | `mkv` | Set intentionally to match this repository's desired-state for this component. |
| `data.GPU_TRANSCODE_WORKERS` | `1` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `data.GPU_HEALTHCHECK_WORKERS` | `1` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `data.GPU_CPU_TRANSCODE_WORKERS` | `0` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `data.GPU_CPU_HEALTHCHECK_WORKERS` | `0` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `data.CPU_TRANSCODE_WORKERS` | `2` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `data.CPU_HEALTHCHECK_WORKERS` | `1` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `data.NODE_POLL_INTERVAL` | `2000` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `data.NODE_START_PAUSED` | `false` | Disabled intentionally to reduce risk, noise, or unnecessary overhead in this environment. |


## `helmrelease.yaml` values

### Document 1: `HelmRelease` `tdarr`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `tdarr` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `30m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
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
| `resources` | `['helmrelease.yaml', 'priorityclass.yaml', 'configmap.yaml']` | Defines which child manifests are composed together as this deployment unit. |


## `priorityclass.yaml` values

### Document 1: `PriorityClass` `tdarr-priority`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `scheduling.k8s.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `PriorityClass` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `tdarr-priority` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `value` | `100` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `globalDefault` | `False` | Disabled intentionally to reduce risk, noise, or unnecessary overhead in this environment. |
| `description` | `Priority class for Tdarr media processing workloads` | Set intentionally to match this repository's desired-state for this component. |
