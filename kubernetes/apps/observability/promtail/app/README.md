# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `helmrelease.yaml`
- `kustomization.yaml`

## `helmrelease.yaml` values

### Document 1: `HelmRelease` `promtail`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `promtail` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `5m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.chart.spec.chart` | `promtail` | Selects the specific Helm chart that provides this workload. |
| `spec.chart.spec.version` | `6.17.1` | Pins the chart version for repeatable deployments and controlled upgrades. |
| `spec.chart.spec.interval` | `30m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.postRenderers` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.daemonset.enabled` | `True` | Feature toggle chosen to match this environment's operational requirements. |
| `spec.values.image.repository` | `grafana/promtail` | Fixes the container image used at runtime so behavior is predictable across reconciliations. |
| `spec.values.image.tag` | `3.6.3@sha256:130b6dd63277d99ce87560c0266c0c30d07bc15ba0a8a590d42215465d4f5363` | Fixes the container image used at runtime so behavior is predictable across reconciliations. |
| `spec.values.serviceMonitor.enabled` | `True` | Feature toggle chosen to match this environment's operational requirements. |
| `spec.values.tolerations` | `list[2]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.tolerations.[0].effect` | `NoSchedule` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.tolerations.[0].operator` | `Exists` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.extraVolumes` | `list[2]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.extraVolumes.[0].name` | `var-journal` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.extraVolumeMounts` | `list[2]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.extraVolumeMounts.[0].name` | `var-journal` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.extraVolumeMounts.[0].mountPath` | `/var/log/journal` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.extraVolumeMounts.[0].readOnly` | `True` | Enabled because this behavior is required for reliable operation in this environment. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./helmrelease.yaml']` | Defines which child manifests are composed together as this deployment unit. |
