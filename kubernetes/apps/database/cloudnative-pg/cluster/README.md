# cluster manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `cluster16.yaml`
- `cluster17-postgis.yaml`
- `kustomization.yaml`
- `scheduledbackup.yaml`

## `cluster16.yaml` values

### Document 1: `Cluster` `postgres`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `postgresql.cnpg.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Cluster` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `postgres` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.instances` | `1` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.imageName` | `ghcr.io/tensorchord/cloudnative-vectorchord:16-0.3.0` | Fixes the container image used at runtime so behavior is predictable across reconciliations. |
| `spec.primaryUpdateStrategy` | `unsupervised` | Set intentionally to match this repository's desired-state for this component. |
| `spec.storage.size` | `10Gi` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.storage.storageClass` | `ceph-block` | Targets the storage backend that matches persistence and performance expectations. |
| `spec.superuserSecret.name` | `cloudnative-pg` | Set intentionally to match this repository's desired-state for this component. |
| `spec.enableSuperuserAccess` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.postgresql.shared_preload_libraries` | `['vchord.so']` | Set intentionally to match this repository's desired-state for this component. |
| `spec.postgresql.parameters.max_connections` | `600` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.postgresql.parameters.max_slot_wal_keep_size` | `5GB` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.postgresql.parameters.shared_buffers` | `512MB` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.resources.requests.cpu` | `200m` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.resources.requests.memory` | `1Gi` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.resources.limits.memory` | `2Gi` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.monitoring.enablePodMonitor` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.monitoring.podMonitorMetricRelabelings` | `list[2]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.monitoring.podMonitorMetricRelabelings.[0].targetLabel` | `cnpg_cluster` | Set intentionally to match this repository's desired-state for this component. |
| `spec.monitoring.podMonitorMetricRelabelings.[0].action` | `replace` | Set intentionally to match this repository's desired-state for this component. |
| `spec.backup.retentionPolicy` | `7d` | Numeric value tuned for current workload size, reliability, and cluster capacity. |

### Document 2: `Service` `postgres-lb`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Service` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `postgres-lb` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `metadata.annotations.io.cilium/lb-ipam-ips` | `${SECRET_POSTGRES_SVC}` | Adds controller-specific hints/behaviors needed by tooling in this cluster. |
| `spec.type` | `LoadBalancer` | Set intentionally to match this repository's desired-state for this component. |
| `spec.externalTrafficPolicy` | `Cluster` | Set intentionally to match this repository's desired-state for this component. |
| `spec.ports` | `list[1]` | Uses the network port expected by clients, probes, or upstream services. |
| `spec.ports.[0].name` | `postgres` | Uses the network port expected by clients, probes, or upstream services. |
| `spec.ports.[0].port` | `5432` | Uses the network port expected by clients, probes, or upstream services. |
| `spec.ports.[0].protocol` | `TCP` | Uses the network port expected by clients, probes, or upstream services. |
| `spec.ports.[0].targetPort` | `5432` | Uses the network port expected by clients, probes, or upstream services. |
| `spec.selector.cnpg.io/cluster` | `postgres` | Set intentionally to match this repository's desired-state for this component. |
| `spec.selector.role` | `primary` | Set intentionally to match this repository's desired-state for this component. |


## `cluster17-postgis.yaml` values

### Document 1: `Cluster` `postgis`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `postgresql.cnpg.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Cluster` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `postgis` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.instances` | `1` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.imageName` | `ghcr.io/cloudnative-pg/postgis:17-3.4` | Fixes the container image used at runtime so behavior is predictable across reconciliations. |
| `spec.primaryUpdateStrategy` | `unsupervised` | Set intentionally to match this repository's desired-state for this component. |
| `spec.storage.size` | `10Gi` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.storage.storageClass` | `ceph-block` | Targets the storage backend that matches persistence and performance expectations. |
| `spec.superuserSecret.name` | `cloudnative-pg` | Set intentionally to match this repository's desired-state for this component. |
| `spec.enableSuperuserAccess` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.postgresql.parameters.max_connections` | `600` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.postgresql.parameters.max_slot_wal_keep_size` | `5GB` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.postgresql.parameters.shared_buffers` | `512MB` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.resources.requests.cpu` | `200m` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.resources.limits.memory` | `2Gi` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.monitoring.enablePodMonitor` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `spec.backup.retentionPolicy` | `7d` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.backup.barmanObjectStore.destinationPath` | `s3://cloudnative-pg/` | Set intentionally to match this repository's desired-state for this component. |
| `spec.backup.barmanObjectStore.endpointURL` | `http://minio.storage.svc.cluster.local:9000` | Set intentionally to match this repository's desired-state for this component. |
| `spec.backup.barmanObjectStore.serverName` | `postgis-v2` | Set intentionally to match this repository's desired-state for this component. |
| `spec.bootstrap.recovery.source` | `postgres` | Set intentionally to match this repository's desired-state for this component. |
| `spec.externalClusters` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |

### Document 2: `Service` `postgis-lb`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Service` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `postgis-lb` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `metadata.annotations.io.cilium/lb-ipam-ips` | `${SECRET_POSTGIS_SVC}` | Adds controller-specific hints/behaviors needed by tooling in this cluster. |
| `spec.type` | `LoadBalancer` | Set intentionally to match this repository's desired-state for this component. |
| `spec.externalTrafficPolicy` | `Cluster` | Set intentionally to match this repository's desired-state for this component. |
| `spec.ports` | `list[1]` | Uses the network port expected by clients, probes, or upstream services. |
| `spec.ports.[0].name` | `postgis` | Uses the network port expected by clients, probes, or upstream services. |
| `spec.ports.[0].port` | `5432` | Uses the network port expected by clients, probes, or upstream services. |
| `spec.ports.[0].protocol` | `TCP` | Uses the network port expected by clients, probes, or upstream services. |
| `spec.ports.[0].targetPort` | `5432` | Uses the network port expected by clients, probes, or upstream services. |
| `spec.selector.cnpg.io/cluster` | `postgresql` | Set intentionally to match this repository's desired-state for this component. |
| `spec.selector.role` | `primary` | Set intentionally to match this repository's desired-state for this component. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./cluster16.yaml', './scheduledbackup.yaml']` | Defines which child manifests are composed together as this deployment unit. |


## `scheduledbackup.yaml` values

### Document 1: `ScheduledBackup` `postgres`

- `metadata.namespace`: `database` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `postgresql.cnpg.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `ScheduledBackup` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `postgres` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.backupOwnerReference` | `self` | Set intentionally to match this repository's desired-state for this component. |
| `spec.schedule` | `@daily` | Set intentionally to match this repository's desired-state for this component. |
| `spec.cluster.name` | `postgres` | Set intentionally to match this repository's desired-state for this component. |
