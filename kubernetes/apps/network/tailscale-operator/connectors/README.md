# connectors manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `dns.yaml`
- `kustomization.yaml`
- `machines.yaml`
- `nfs.yaml`

## `dns.yaml` values

### Document 1: `Connector` `ts-dns-cidrs`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `tailscale.com/v1alpha1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Connector` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `ts-dns-cidrs` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.hostname` | `ts-dns-cidrs` | Routes traffic or integration calls to the intended DNS endpoint. |
| `spec.exitNode` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.subnetRouter.advertiseRoutes` | `['${SECRET_PIHOLE_SVC}/32']` | Set intentionally to match this repository's desired-state for this component. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['machines.yaml', 'dns.yaml', 'nfs.yaml']` | Defines which child manifests are composed together as this deployment unit. |


## `machines.yaml` values

### Document 1: `Connector` `ts-pod-cidrs`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `tailscale.com/v1alpha1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Connector` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `ts-pod-cidrs` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.hostname` | `ts-pod-cidrs` | Routes traffic or integration calls to the intended DNS endpoint. |
| `spec.exitNode` | `False` | Disabled intentionally to reduce risk, noise, or unnecessary overhead in this environment. |
| `spec.subnetRouter.advertiseRoutes` | `['10.32.0.0/16']` | Set intentionally to match this repository's desired-state for this component. |


## `nfs.yaml` values

### Document 1: `Connector` `ts-nfs-svc`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `tailscale.com/v1alpha1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Connector` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `ts-nfs-svc` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.hostname` | `ts-nfs-svc` | Routes traffic or integration calls to the intended DNS endpoint. |
| `spec.exitNode` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.subnetRouter.advertiseRoutes` | `['${SECRET_NFS_SVC}/32']` | Set intentionally to match this repository's desired-state for this component. |
