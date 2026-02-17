# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `certificate.yaml`
- `envoy.yaml`
- `helmrelease.yaml`
- `kustomization.yaml`
- `ocirepository.yaml`
- `podmonitor.yaml`

## `certificate.yaml` values

### Document 1: `Certificate` `${SECRET_DOMAIN/./-}-production`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `cert-manager.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Certificate` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `${SECRET_DOMAIN/./-}-production` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.secretName` | `${SECRET_DOMAIN/./-}-production-tls` | Set intentionally to match this repository's desired-state for this component. |
| `spec.issuerRef.name` | `letsencrypt-production` | Set intentionally to match this repository's desired-state for this component. |
| `spec.issuerRef.kind` | `ClusterIssuer` | Set intentionally to match this repository's desired-state for this component. |
| `spec.commonName` | `${SECRET_DOMAIN}` | Set intentionally to match this repository's desired-state for this component. |
| `spec.dnsNames` | `['${SECRET_DOMAIN}', '*.${SECRET_DOMAIN}']` | Set intentionally to match this repository's desired-state for this component. |


## `envoy.yaml` values

### Document 1: `EnvoyProxy` `envoy`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `gateway.envoyproxy.io/v1alpha1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `EnvoyProxy` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `envoy` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.logging.level.default` | `info` | Set intentionally to match this repository's desired-state for this component. |
| `spec.provider.type` | `Kubernetes` | Set intentionally to match this repository's desired-state for this component. |
| `spec.shutdown.drainTimeout` | `180s` | Bounds how long reconciliation may run before surfacing failure for faster troubleshooting. |

### Document 2: `GatewayClass` `envoy`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `gateway.networking.k8s.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `GatewayClass` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `envoy` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.controllerName` | `gateway.envoyproxy.io/gatewayclass-controller` | Set intentionally to match this repository's desired-state for this component. |
| `spec.parametersRef.group` | `gateway.envoyproxy.io` | Set intentionally to match this repository's desired-state for this component. |
| `spec.parametersRef.kind` | `EnvoyProxy` | Set intentionally to match this repository's desired-state for this component. |
| `spec.parametersRef.name` | `envoy` | Set intentionally to match this repository's desired-state for this component. |
| `spec.parametersRef.namespace` | `network` | Separates this component into the correct tenancy boundary and avoids cross-namespace sprawl. |

### Document 3: `Gateway` `envoy-external`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `gateway.networking.k8s.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Gateway` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `envoy-external` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `metadata.annotations.external-dns.alpha.kubernetes.io/target` | `external.${SECRET_DOMAIN}` | Adds controller-specific hints/behaviors needed by tooling in this cluster. |
| `spec.gatewayClassName` | `envoy` | Set intentionally to match this repository's desired-state for this component. |
| `spec.infrastructure.annotations.external-dns.alpha.kubernetes.io/hostname` | `external.${SECRET_DOMAIN}` | Routes traffic or integration calls to the intended DNS endpoint. |
| `spec.infrastructure.annotations.lbipam.cilium.io/ips` | `10.32.1.13` | Adds controller-specific hints/behaviors needed by tooling in this cluster. |
| `spec.listeners` | `list[2]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.listeners.[0].name` | `http` | Set intentionally to match this repository's desired-state for this component. |
| `spec.listeners.[0].protocol` | `HTTP` | Set intentionally to match this repository's desired-state for this component. |
| `spec.listeners.[0].port` | `80` | Uses the network port expected by clients, probes, or upstream services. |

### Document 4: `Gateway` `envoy-internal`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `gateway.networking.k8s.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Gateway` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `envoy-internal` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `metadata.annotations.external-dns.alpha.kubernetes.io/target` | `internal.${SECRET_DOMAIN}` | Adds controller-specific hints/behaviors needed by tooling in this cluster. |
| `spec.gatewayClassName` | `envoy` | Set intentionally to match this repository's desired-state for this component. |
| `spec.infrastructure.annotations.external-dns.alpha.kubernetes.io/hostname` | `internal.${SECRET_DOMAIN}` | Routes traffic or integration calls to the intended DNS endpoint. |
| `spec.infrastructure.annotations.lbipam.cilium.io/ips` | `10.32.1.12` | Adds controller-specific hints/behaviors needed by tooling in this cluster. |
| `spec.listeners` | `list[2]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.listeners.[0].name` | `http` | Set intentionally to match this repository's desired-state for this component. |
| `spec.listeners.[0].protocol` | `HTTP` | Set intentionally to match this repository's desired-state for this component. |
| `spec.listeners.[0].port` | `80` | Uses the network port expected by clients, probes, or upstream services. |

### Document 5: `BackendTrafficPolicy` `envoy`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `gateway.envoyproxy.io/v1alpha1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `BackendTrafficPolicy` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `envoy` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.compression` | `list[2]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.compression.[0].type` | `Brotli` | Set intentionally to match this repository's desired-state for this component. |
| `spec.connection.bufferLimit` | `8Mi` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.targetSelectors` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.targetSelectors.[0].group` | `gateway.networking.k8s.io` | Set intentionally to match this repository's desired-state for this component. |
| `spec.targetSelectors.[0].kind` | `Gateway` | Set intentionally to match this repository's desired-state for this component. |
| `spec.timeout.http.requestTimeout` | `0s` | Bounds how long reconciliation may run before surfacing failure for faster troubleshooting. |

### Document 6: `ClientTrafficPolicy` `envoy`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `gateway.envoyproxy.io/v1alpha1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `ClientTrafficPolicy` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `envoy` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.clientIPDetection.xForwardedFor.trustedCIDRs` | `['10.42.0.0/16']` | Set intentionally to match this repository's desired-state for this component. |
| `spec.connection.bufferLimit` | `4Mi` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.connection.maxAcceptPerSocketEvent` | `0` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.http2.initialStreamWindowSize` | `512Ki` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.http2.initialConnectionWindowSize` | `8Mi` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.http2.onInvalidMessage` | `TerminateStream` | Set intentionally to match this repository's desired-state for this component. |
| `spec.targetSelectors` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.targetSelectors.[0].group` | `gateway.networking.k8s.io` | Set intentionally to match this repository's desired-state for this component. |
| `spec.targetSelectors.[0].kind` | `Gateway` | Set intentionally to match this repository's desired-state for this component. |
| `spec.timeout.http.requestReceivedTimeout` | `0s` | Bounds how long reconciliation may run before surfacing failure for faster troubleshooting. |
| `spec.tls.minVersion` | `1.2` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.tls.alpnProtocols` | `['h2', 'http/1.1']` | Set intentionally to match this repository's desired-state for this component. |

### Document 7: `HTTPRoute` `https-redirect`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `gateway.networking.k8s.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HTTPRoute` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `https-redirect` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `metadata.annotations.external-dns.alpha.kubernetes.io/controller` | `none` | Adds controller-specific hints/behaviors needed by tooling in this cluster. |
| `spec.parentRefs` | `list[2]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.parentRefs.[0].name` | `envoy-external` | Set intentionally to match this repository's desired-state for this component. |
| `spec.parentRefs.[0].namespace` | `network` | Separates this component into the correct tenancy boundary and avoids cross-namespace sprawl. |
| `spec.parentRefs.[0].sectionName` | `http` | Set intentionally to match this repository's desired-state for this component. |
| `spec.rules` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |


## `helmrelease.yaml` values

### Document 1: `HelmRelease` `envoy-gateway`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `envoy-gateway` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.chartRef.kind` | `OCIRepository` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.chartRef.name` | `envoy-gateway` | Binds this release to a known source object so artifact resolution is deterministic. |
| `spec.interval` | `1h` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.values.global.imageRegistry` | `mirror.gcr.io` | Fixes the container image used at runtime so behavior is predictable across reconciliations. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./certificate.yaml', './envoy.yaml', './helmrelease.yaml', './ocirepository.yaml', '....` | Defines which child manifests are composed together as this deployment unit. |


## `ocirepository.yaml` values

### Document 1: `OCIRepository` `envoy-gateway`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `source.toolkit.fluxcd.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `OCIRepository` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `envoy-gateway` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `15m` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.layerSelector.mediaType` | `application/vnd.cncf.helm.chart.content.v1.tar+gzip` | Set intentionally to match this repository's desired-state for this component. |
| `spec.layerSelector.operation` | `copy` | Set intentionally to match this repository's desired-state for this component. |
| `spec.ref.tag` | `v1.6.1` | Locks the application version to avoid unexpected upstream changes. |
| `spec.url` | `oci://mirror.gcr.io/envoyproxy/gateway-helm` | Set intentionally to match this repository's desired-state for this component. |


## `podmonitor.yaml` values

### Document 1: `PodMonitor` `envoy-proxy`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `monitoring.coreos.com/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `PodMonitor` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `envoy-proxy` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.jobLabel` | `envoy-proxy` | Set intentionally to match this repository's desired-state for this component. |
| `spec.namespaceSelector.matchNames` | `['network']` | Set intentionally to match this repository's desired-state for this component. |
| `spec.podMetricsEndpoints` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.podMetricsEndpoints.[0].port` | `metrics` | Uses the network port expected by clients, probes, or upstream services. |
| `spec.podMetricsEndpoints.[0].path` | `/stats/prometheus` | Set intentionally to match this repository's desired-state for this component. |
| `spec.podMetricsEndpoints.[0].honorLabels` | `True` | Supports selectors, grouping, and operational discoverability. |
| `spec.selector.matchLabels.app.kubernetes.io/component` | `proxy` | Supports selectors, grouping, and operational discoverability. |
| `spec.selector.matchLabels.app.kubernetes.io/name` | `envoy` | Supports selectors, grouping, and operational discoverability. |
