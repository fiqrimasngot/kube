# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `helmrelease.yaml`
- `kustomization.yaml`

## `helmrelease.yaml` values

### Document 1: `HelmRepository` `authentik`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `source.toolkit.fluxcd.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRepository` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `authentik` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `1h` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.url` | `https://charts.goauthentik.io` | Set intentionally to match this repository's desired-state for this component. |

### Document 2: `HelmRelease` `authentik`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `authentik` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `5m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.install.timeout` | `25m` | Bounds how long reconciliation may run before surfacing failure for faster troubleshooting. |
| `spec.install.remediation.retries` | `5` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.upgrade.timeout` | `25m` | Bounds how long reconciliation may run before surfacing failure for faster troubleshooting. |
| `spec.upgrade.remediation.retries` | `5` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.upgrade.remediation.remediateLastFailure` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.upgrade.cleanupOnFail` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.chart.spec.chart` | `authentik` | Selects the specific Helm chart that provides this workload. |
| `spec.chart.spec.version` | `2025.10.3` | Pins the chart version for repeatable deployments and controlled upgrades. |
| `spec.values.kubernetesIntegration` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.values.postgresql.enabled` | `True` | Feature toggle chosen to match this environment's operational requirements. |
| `spec.values.redis.enabled` | `False` | Feature toggle chosen to match this environment's operational requirements. |
| `spec.values.authentik.secret_key` | `${SECRET_AUTHENTIK_SECRET_KEY}` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.global.addPrometheusAnnotations` | `True` | Adds controller-specific hints/behaviors needed by tooling in this cluster. |
| `spec.values.backup.bucket` | `authentik-db` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.backup.host` | `http://minio.storage.svc.cluster.local:9000` | Routes traffic or integration calls to the intended DNS endpoint. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./helmrelease.yaml']` | Defines which child manifests are composed together as this deployment unit. |
