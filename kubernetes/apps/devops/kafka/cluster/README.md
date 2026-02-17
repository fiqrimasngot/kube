# cluster manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `kafka-cluster.yaml`
- `kafka-topics.yaml`
- `kafka-users.yaml`
- `kustomization.yaml`

## `kafka-cluster.yaml` values

### Document 1: `KafkaNodePool` `kafka`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kafka.strimzi.io/v1beta2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `KafkaNodePool` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `kafka` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `metadata.labels.strimzi.io/cluster` | `kafka-at-home` | Supports selectors, grouping, and operational discoverability. |
| `spec.replicas` | `3` | Sets desired availability versus resource cost for this service. |
| `spec.roles` | `['broker', 'controller']` | Set intentionally to match this repository's desired-state for this component. |
| `spec.storage.type` | `persistent-claim` | Set intentionally to match this repository's desired-state for this component. |
| `spec.storage.class` | `ceph-block` | Set intentionally to match this repository's desired-state for this component. |
| `spec.storage.size` | `5Gi` | Numeric value tuned for current workload size, reliability, and cluster capacity. |

### Document 2: `Kafka` `kafka-at-home`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kafka.strimzi.io/v1beta2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kafka` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `kafka-at-home` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `metadata.annotations.strimzi.io/node-pools` | `enabled` | Adds controller-specific hints/behaviors needed by tooling in this cluster. |
| `metadata.annotations.strimzi.io/kraft` | `enabled` | Adds controller-specific hints/behaviors needed by tooling in this cluster. |
| `spec.kafka.version` | `3.8.0` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.kafka.metadataVersion` | `3.8-IV0` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.kafka.replicas` | `3` | Sets desired availability versus resource cost for this service. |
| `spec.kafka.listeners` | `list[3]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.kafka.listeners.[0].name` | `plain` | Set intentionally to match this repository's desired-state for this component. |
| `spec.kafka.listeners.[0].port` | `9092` | Uses the network port expected by clients, probes, or upstream services. |
| `spec.kafka.listeners.[0].type` | `internal` | Set intentionally to match this repository's desired-state for this component. |
| `spec.kafka.listeners.[0].tls` | `False` | Disabled intentionally to reduce risk, noise, or unnecessary overhead in this environment. |
| `spec.kafka.config.offsets.topic.replication.factor` | `3` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.kafka.config.transaction.state.log.replication.factor` | `3` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.kafka.config.transaction.state.log.min.isr` | `2` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.kafka.config.default.replication.factor` | `3` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.kafka.config.min.insync.replicas` | `2` | Sets desired availability versus resource cost for this service. |
| `spec.kafka.storage.type` | `persistent-claim` | Set intentionally to match this repository's desired-state for this component. |
| `spec.kafka.storage.class` | `ceph-block` | Set intentionally to match this repository's desired-state for this component. |
| `spec.kafka.storage.size` | `5Gi` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.zookeeper.replicas` | `3` | Sets desired availability versus resource cost for this service. |


## `kafka-topics.yaml` values

### Document 1: `KafkaTopic` `test-topic`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kafka.strimzi.io/v1beta2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `KafkaTopic` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `test-topic` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `metadata.labels.strimzi.io/cluster` | `kafka-at-home` | Supports selectors, grouping, and operational discoverability. |
| `spec.partitions` | `1` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `spec.replicas` | `3` | Sets desired availability versus resource cost for this service. |
| `spec.config.retention.ms` | `7200000` | Numeric value tuned for current workload size, reliability, and cluster capacity. |


## `kafka-users.yaml` values

- No YAML documents found.

## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./kafka-users.yaml', './kafka-cluster.yaml', './kafka-topics.yaml']` | Defines which child manifests are composed together as this deployment unit. |
