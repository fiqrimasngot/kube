# flux-system manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `kustomization.yaml`
- `namespace.yaml`

## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `namespace` | `flux-system` | Separates this component into the correct tenancy boundary and avoids cross-namespace sprawl. |
| `components` | `['../../components/sops']` | Applies shared Kustomize components used for cross-cutting concerns in this repo. |
| `resources` | `['./namespace.yaml', './flux-instance/ks.yaml', './flux-operator/ks.yaml']` | Defines which child manifests are composed together as this deployment unit. |


## `namespace.yaml` values

### Document 1: `Namespace` `flux-system`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Namespace` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `flux-system` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `metadata.annotations.kustomize.toolkit.fluxcd.io/prune` | `disabled` | Adds controller-specific hints/behaviors needed by tooling in this cluster. |
