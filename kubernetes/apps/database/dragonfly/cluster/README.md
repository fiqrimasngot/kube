# cluster manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `cluster.yaml`
- `kustomization.yaml`
- `podmonitor.yaml`

## `cluster.yaml` values

### Document 1: `Dragonfly` `dragonfly`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `dragonflydb.io/v1alpha1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Dragonfly` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `dragonfly` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.image` | `ghcr.io/dragonflydb/dragonfly:v1.35.1` | Fixes the container image used at runtime so behavior is predictable across reconciliations. |
| `spec.replicas` | `1` | Sets desired availability versus resource cost for this service. |
| `spec.env` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.env.[0].name` | `MAX_MEMORY` | Set intentionally to match this repository's desired-state for this component. |
| `spec.args` | `['--maxmemory=$(MAX_MEMORY)Mi', '--proactor_threads=2', '--cluster_mode=emulated', '--d...` | Set intentionally to match this repository's desired-state for this component. |
| `spec.resources.requests.cpu` | `100m` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.resources.limits.memory` | `512Mi` | Numeric value tuned for current workload size, reliability, and cluster capacity. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./cluster.yaml', './podmonitor.yaml']` | Defines which child manifests are composed together as this deployment unit. |


## `podmonitor.yaml` values

### Document 1: `PodMonitor` `dragonfly`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `monitoring.coreos.com/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `PodMonitor` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `dragonfly` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.selector.matchLabels.app` | `dragonfly` | Supports selectors, grouping, and operational discoverability. |
| `spec.podTargetLabels` | `['app']` | Supports selectors, grouping, and operational discoverability. |
| `spec.podMetricsEndpoints` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.podMetricsEndpoints.[0].port` | `admin` | Uses the network port expected by clients, probes, or upstream services. |
