# rules manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `barcode-reader-device.yaml`
- `google-coral-device.yaml`
- `kustomization.yaml`
- `nvidia-gpu.yaml`
- `zigbee-device.yaml`
- `zwave-device.yaml`

## `barcode-reader-device.yaml` values

### Document 1: `NodeFeatureRule` `barcode-reader-device`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `nfd.k8s-sigs.io/v1alpha1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `NodeFeatureRule` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `barcode-reader-device` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.rules` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.rules.[0].name` | `barcode.reader` | Set intentionally to match this repository's desired-state for this component. |


## `google-coral-device.yaml` values

### Document 1: `NodeFeatureRule` `google-coral-device`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `nfd.k8s-sigs.io/v1alpha1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `NodeFeatureRule` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `google-coral-device` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.rules` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.rules.[0].name` | `google.coral` | Set intentionally to match this repository's desired-state for this component. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./nvidia-gpu.yaml', './zwave-device.yaml', './zigbee-device.yaml', './google-coral-de...` | Defines which child manifests are composed together as this deployment unit. |


## `nvidia-gpu.yaml` values

### Document 1: `NodeFeatureRule` `nvidia-gpu-plugin`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `nfd.k8s-sigs.io/v1alpha1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `NodeFeatureRule` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `nvidia-gpu-plugin` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.rules` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.rules.[0].name` | `nvidia.gpu` | Set intentionally to match this repository's desired-state for this component. |


## `zigbee-device.yaml` values

### Document 1: `NodeFeatureRule` `sonoff-zigbee-device`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `nfd.k8s-sigs.io/v1alpha1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `NodeFeatureRule` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `sonoff-zigbee-device` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.rules` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.rules.[0].name` | `zigbee` | Set intentionally to match this repository's desired-state for this component. |


## `zwave-device.yaml` values

### Document 1: `NodeFeatureRule` `zwave-device`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `nfd.k8s-sigs.io/v1alpha1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `NodeFeatureRule` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `zwave-device` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.rules` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.rules.[0].name` | `aeotec.zwave` | Set intentionally to match this repository's desired-state for this component. |
