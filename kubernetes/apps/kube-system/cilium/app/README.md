# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `helmrelease.yaml`
- `kustomization.yaml`
- `networks.yaml`
- `ocirepository.yaml`

## `helmrelease.yaml` values

### Document 1: `HelmRelease` `cilium`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `cilium` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.chartRef.kind` | `OCIRepository` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.chartRef.name` | `cilium` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.interval` | `1h` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.values.autoDirectNodeRoutes` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.values.bpf.masquerade` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.values.bpf.hostLegacyRouting` | `True` | Routes traffic or integration calls to the intended DNS endpoint. |
| `spec.values.cni.exclusive` | `False` | Disabled intentionally to reduce risk, noise, or unnecessary overhead in this environment. |
| `spec.values.cgroup.hostRoot` | `/sys/fs/cgroup` | Routes traffic or integration calls to the intended DNS endpoint. |
| `spec.values.dashboards.enabled` | `True` | Feature toggle chosen to match this environment's operational requirements. |
| `spec.values.endpointRoutes.enabled` | `True` | Feature toggle chosen to match this environment's operational requirements. |
| `spec.values.envoy.enabled` | `False` | Feature toggle chosen to match this environment's operational requirements. |
| `spec.values.gatewayAPI.enabled` | `False` | Feature toggle chosen to match this environment's operational requirements. |
| `spec.values.hubble.enabled` | `False` | Feature toggle chosen to match this environment's operational requirements. |
| `spec.values.ipam.mode` | `kubernetes` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.ipv4NativeRoutingCIDR` | `10.42.0.0/16` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.values.k8sServiceHost` | `127.0.0.1` | Routes traffic or integration calls to the intended DNS endpoint. |
| `spec.values.k8sServicePort` | `7445` | Uses the network port expected by clients, probes, or upstream services. |
| `spec.values.kubeProxyReplacement` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.values.kubeProxyReplacementHealthzBindAddr` | `0.0.0.0:10256` | Numeric value tuned for current workload size, reliability, and cluster capacity. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./helmrelease.yaml', './ocirepository.yaml', './networks.yaml']` | Defines which child manifests are composed together as this deployment unit. |


## `networks.yaml` values

### Document 1: `CiliumLoadBalancerIPPool` `pool`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `cilium.io/v2alpha1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `CiliumLoadBalancerIPPool` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `pool` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.allowFirstLastIPs` | `No` | Set intentionally to match this repository's desired-state for this component. |
| `spec.blocks` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.blocks.[0].cidr` | `10.32.1.0/24` | Numeric value tuned for current workload size, reliability, and cluster capacity. |

### Document 2: `CiliumL2AnnouncementPolicy` `l2-policy`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `cilium.io/v2alpha1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `CiliumL2AnnouncementPolicy` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `l2-policy` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.loadBalancerIPs` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.nodeSelector.matchLabels.kubernetes.io/os` | `linux` | Supports selectors, grouping, and operational discoverability. |


## `ocirepository.yaml` values

### Document 1: `OCIRepository` `cilium`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `source.toolkit.fluxcd.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `OCIRepository` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `cilium` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `15m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.layerSelector.mediaType` | `application/vnd.cncf.helm.chart.content.v1.tar+gzip` | Set intentionally to match this repository's desired-state for this component. |
| `spec.layerSelector.operation` | `copy` | Set intentionally to match this repository's desired-state for this component. |
| `spec.ref.tag` | `1.18.5` | Locks the application version to avoid unexpected upstream changes. |
| `spec.url` | `oci://ghcr.io/home-operations/charts-mirror/cilium` | Set intentionally to match this repository's desired-state for this component. |
