# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `helmrelease.yaml`
- `kustomization.yaml`

## `helmrelease.yaml` values

### Document 1: `HelmRepository` `prometheus-community`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `source.toolkit.fluxcd.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRepository` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `prometheus-community` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.type` | `oci` | Set intentionally to match this repository's desired-state for this component. |
| `spec.interval` | `5m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.url` | `oci://ghcr.io/prometheus-community/charts` | Set intentionally to match this repository's desired-state for this component. |

### Document 2: `HelmRelease` `blackbox-exporter`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `blackbox-exporter` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `30m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.chart.spec.chart` | `prometheus-blackbox-exporter` | Selects the specific Helm chart that provides this workload. |
| `spec.chart.spec.version` | `11.6.1` | Pins the chart version for repeatable deployments and controlled upgrades. |
| `spec.values.fullnameOverride` | `blackbox-exporter` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.ingress.enabled` | `True` | Feature toggle chosen to match this environment's operational requirements. |
| `spec.values.ingress.className` | `internal` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.ingress.hosts` | `list[1]` | Routes traffic or integration calls to the intended DNS endpoint. |
| `spec.values.ingress.hosts.[0].host` | `blackbox.${SECRET_DOMAIN}` | Routes traffic or integration calls to the intended DNS endpoint. |
| `spec.values.allowIcmp` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.values.pspEnabled` | `False` | Feature toggle chosen to match this environment's operational requirements. |
| `spec.values.podSecurityContext.sysctls` | `list[1]` | Applies runtime hardening to reduce privilege and container escape risk. |
| `spec.values.podSecurityContext.sysctls.[0].name` | `net.ipv4.ping_group_range` | Applies runtime hardening to reduce privilege and container escape risk. |
| `spec.values.podSecurityContext.sysctls.[0].value` | `1000 1000` | Applies runtime hardening to reduce privilege and container escape risk. |
| `spec.values.securityContext.runAsUser` | `1000` | Applies runtime hardening to reduce privilege and container escape risk. |
| `spec.values.securityContext.runAsGroup` | `1000` | Applies runtime hardening to reduce privilege and container escape risk. |
| `spec.values.securityContext.readOnlyRootFilesystem` | `True` | Applies runtime hardening to reduce privilege and container escape risk. |
| `spec.values.securityContext.runAsNonRoot` | `True` | Applies runtime hardening to reduce privilege and container escape risk. |
| `spec.values.securityContext.allowPrivilegeEscalation` | `False` | Applies runtime hardening to reduce privilege and container escape risk. |
| `spec.values.serviceMonitor.enabled` | `True` | Feature toggle chosen to match this environment's operational requirements. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./helmrelease.yaml']` | Defines which child manifests are composed together as this deployment unit. |
