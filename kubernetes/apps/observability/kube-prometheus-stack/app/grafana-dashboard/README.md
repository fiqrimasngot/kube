# grafana-dashboard manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `kustomization.yaml`

## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `configMapGenerator` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `configMapGenerator.[0].name` | `grafana-dashboard-nodes` | Set intentionally to match this repository's desired-state for this component. |
| `generatorOptions.disableNameSuffixHash` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `generatorOptions.labels.grafana-dashboard` | `true` | Supports selectors, grouping, and operational discoverability. |
| `generatorOptions.annotations.k8s-sidecar-target-directory` | `/tmp/dashboards/Cluster` | Adds controller-specific hints/behaviors needed by tooling in this cluster. |
