# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `helmrelease.yaml`
- `kustomization.yaml`
- `secrets.sops.yaml`

## `helmrelease.yaml` values

### Document 1: `HelmRelease` `kube-prometheus-stack`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `kube-prometheus-stack` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `30m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.chart.spec.chart` | `kube-prometheus-stack` | Selects the specific Helm chart that provides this workload. |
| `spec.chart.spec.version` | `80.14.4` | Pins the chart version for repeatable deployments and controlled upgrades. |
| `spec.install.createNamespace` | `True` | Separates this component into the correct tenancy boundary and avoids cross-namespace sprawl. |
| `spec.install.remediation.retries` | `3` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.upgrade.remediation.retries` | `3` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.values.kubeEtcd.endpoints` | `['10.32.1.51']` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.kubeProxy.enabled` | `False` | Feature toggle chosen to match this environment's operational requirements. |
| `spec.values.kubeStateMetrics.enabled` | `True` | Feature toggle chosen to match this environment's operational requirements. |
| `spec.values.kube-state-metrics.fullnameOverride` | `kube-state-metrics` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.kube-state-metrics.metricLabelsAllowlist` | `['pods=[*]', 'deployments=[*]', 'persistentvolumeclaims=[*]']` | Supports selectors, grouping, and operational discoverability. |
| `spec.values.grafana.assertNoLeakedSecrets` | `False` | Disabled intentionally to reduce risk, noise, or unnecessary overhead in this environment. |
| `spec.values.grafana.envFromSecret` | `grafana-admin-secret` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.grafana.defaultDashboardsTimezone` | `browser` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.grafana.plugins` | `['grafana-piechart-panel', 'grafana-clock-panel', 'grafana-piechart-panel', 'grafana-wo...` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.prometheusOperator.configReloaderCpu` | `0` | Numeric value tuned for current workload size, reliability, and cluster capacity. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./helmrelease.yaml', './secrets.sops.yaml', './grafana-dashboard']` | Defines which child manifests are composed together as this deployment unit. |


## `secrets.sops.yaml` values

### Document 1: `Secret` `grafana-admin-secret`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Secret` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `grafana-admin-secret` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `stringData.openid-config-client-id` | `ENC[AES256_GCM,data:mLBWIbrtOJp7WttmQBE/XMFtT0ioYUnYfWPZdr443z1J7DgZcKF/tA==,iv:mS/hlG8...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.openid-config-client-secret` | `ENC[AES256_GCM,data:+bcygJFmh5C/jD377RGgqwa4yhvttXD1ZICAxLEKrHmCTlf0H3W4Y9F0aWgac/DM+W2...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].recipient` | `age1sumyxgm2je4txw82k838698mmqmf40wsw6j8eu3jhf5v54g4sslqpchxuf` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].enc` | `-----BEGIN AGE ENCRYPTED FILE----- YWdlLWVuY3J5cHRpb24ub3JnL3YxCi0+IFgyNTUxOSBBSWFvcmUr...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.lastmodified` | `2026-02-17T11:15:06Z` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `sops.mac` | `ENC[AES256_GCM,data:wHzB2D8Sq5t5KOKUQ0XJgKSIIJvHdTKSVEw0fQ7/hSB9hnmHQDG/OjHJjXT5Uxqza+X...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.encrypted_regex` | `^(data|stringData)$` | Set intentionally to match this repository's desired-state for this component. |
| `sops.mac_only_encrypted` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `sops.version` | `3.11.0` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
