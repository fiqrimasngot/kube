# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `helmrelease.yaml`
- `kustomization.yaml`
- `secrets.sops.yaml`

## `helmrelease.yaml` values

### Document 1: `HelmRepository` `grafana`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `source.toolkit.fluxcd.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRepository` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `grafana` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `2h` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.url` | `https://grafana.github.io/helm-charts` | Set intentionally to match this repository's desired-state for this component. |

### Document 2: `HelmRelease` `loki`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `loki` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `30m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.timeout` | `15m` | Bounds how long reconciliation may run before surfacing failure for faster troubleshooting. |
| `spec.chart.spec.chart` | `loki` | Selects the specific Helm chart that provides this workload. |
| `spec.chart.spec.version` | `6.49.0` | Pins the chart version for repeatable deployments and controlled upgrades. |
| `spec.maxHistory` | `2` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.install.remediation.retries` | `3` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.upgrade.cleanupOnFail` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.upgrade.remediation.retries` | `3` | Allows automatic recovery from transient pull/network/startup failures. |
| `spec.uninstall.keepHistory` | `False` | Disabled intentionally to reduce risk, noise, or unnecessary overhead in this environment. |
| `spec.values.deploymentMode` | `SimpleScalable` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.loki.auth_enabled` | `False` | Feature toggle chosen to match this environment's operational requirements. |
| `spec.values.gateway.replicas` | `1` | Sets desired availability versus resource cost for this service. |
| `spec.values.gateway.enabled` | `True` | Feature toggle chosen to match this environment's operational requirements. |
| `spec.values.read.replicas` | `1` | Sets desired availability versus resource cost for this service. |
| `spec.values.write.replicas` | `1` | Sets desired availability versus resource cost for this service. |
| `spec.values.backend.replicas` | `1` | Sets desired availability versus resource cost for this service. |
| `spec.values.lokiCanary.enabled` | `False` | Feature toggle chosen to match this environment's operational requirements. |
| `spec.values.test.enabled` | `False` | Feature toggle chosen to match this environment's operational requirements. |
| `spec.valuesFrom` | `list[4]` | Set intentionally to match this repository's desired-state for this component. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./helmrelease.yaml', './secrets.sops.yaml']` | Defines which child manifests are composed together as this deployment unit. |
| `configMapGenerator` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `configMapGenerator.[0].name` | `loki-rules` | Set intentionally to match this repository's desired-state for this component. |
| `configMapGenerator.[0].namespace` | `observability` | Separates this component into the correct tenancy boundary and avoids cross-namespace sprawl. |
| `generatorOptions.disableNameSuffixHash` | `True` | Enabled because this behavior is required for reliable operation in this environment. |


## `secrets.sops.yaml` values

### Document 1: `Secret` `loki`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Secret` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `loki` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `stringData.BUCKET_NAME` | `ENC[AES256_GCM,data:q6Wecw==,iv:IBsooVAcVrtW17dDnJ7WW01jgO2o8GVFwbYbrZXG1x0=,tag:ZHeGtV...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.BUCKET_HOST` | `ENC[AES256_GCM,data:R2GSmyf9enDV326VvuSOiY7kgK97msks8/3Br6li6nLQZyLSNthWcyMIzg==,iv:TAm...` | Routes traffic or integration calls to the intended DNS endpoint. |
| `stringData.AWS_ACCESS_KEY_ID` | `ENC[AES256_GCM,data:z7Vs1nB/5PTAUJx9MEq45tzUEcA=,iv:Yn2gV9b+solX9yG3rhvDGMS9phDS5KCLVMQ...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.AWS_SECRET_ACCESS_KEY` | `ENC[AES256_GCM,data:7AQQWXD31OvegJOpZM+5wGFNYUVwCJT8k0tbHATc7vRNKuP7RLM4iw==,iv:AqTX7wY...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].recipient` | `age1sumyxgm2je4txw82k838698mmqmf40wsw6j8eu3jhf5v54g4sslqpchxuf` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].enc` | `-----BEGIN AGE ENCRYPTED FILE----- YWdlLWVuY3J5cHRpb24ub3JnL3YxCi0+IFgyNTUxOSBTUFJDR1JD...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.lastmodified` | `2026-02-17T11:15:06Z` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `sops.mac` | `ENC[AES256_GCM,data:W/RL7lmCn7O5YJtyFftfaFKgEgprkjpczwi+gwWifqaUwZ8oO+1D6q6Zkd9h3w4HIhe...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.encrypted_regex` | `^(data|stringData)$` | Set intentionally to match this repository's desired-state for this component. |
| `sops.mac_only_encrypted` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `sops.version` | `3.11.0` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
