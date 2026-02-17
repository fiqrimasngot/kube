# k8s-events-exporter deployment manifests

This directory deploys [`kubernetes-event-exporter`](https://github.com/resmoio/kubernetes-event-exporter) into the `observability` namespace and routes Kubernetes events to Loki.

## Files in this directory

- `kustomization.yaml`: entrypoint manifest that applies all resources in this folder.
- `roles.yaml`: service account + RBAC permissions used by the exporter.
- `deployment.yaml`: workload definition for the exporter pod.
- `configmap.yaml`: exporter runtime configuration (`config.yaml`) mounted into the pod.

## `deployment.yaml` field reference

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `apps/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Deployment` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `event-exporter` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `metadata.namespace` | `observability` | Scopes the resource into the namespace where this component is intentionally operated. |
| `spec.replicas` | `1` | Sets desired availability versus resource cost for this service. |
| `spec.selector.matchLabels` | `app=event-exporter`, `version=v1` | Label selector used by the Deployment to identify pods it owns. Must match template labels. |
| `spec.template.metadata.labels.app` | `event-exporter` | Supports selectors, grouping, and operational discoverability. |
| `spec.template.metadata.labels.version` | `v1` | Supports selectors, grouping, and operational discoverability. |
| `spec.template.metadata.annotations.prometheus.io/scrape` | `'true'` | Adds controller-specific hints/behaviors needed by tooling in this cluster. |
| `spec.template.metadata.annotations.prometheus.io/port` | `'2112'` | Uses the network port expected by clients, probes, or upstream services. |
| `spec.template.metadata.annotations.prometheus.io/path` | `'/metrics'` | Adds controller-specific hints/behaviors needed by tooling in this cluster. |
| `spec.template.spec.serviceAccountName` | `event-exporter` | Set intentionally to match this repository's desired-state for this component. |
| `spec.template.spec.securityContext.runAsNonRoot` | `true` | Applies runtime hardening to reduce privilege and container escape risk. |
| `spec.template.spec.securityContext.seccompProfile.type` | `RuntimeDefault` | Applies runtime hardening to reduce privilege and container escape risk. |
| `spec.template.spec.containers[0].name` | `event-exporter` | Set intentionally to match this repository's desired-state for this component. |
| `spec.template.spec.containers[0].image` | `ghcr.io/resmoio/kubernetes-event-exporter:v1.7@sha256:...` | Fixes the container image used at runtime so behavior is predictable across reconciliations. |
| `spec.template.spec.containers[0].imagePullPolicy` | `IfNotPresent` | Fixes the container image used at runtime so behavior is predictable across reconciliations. |
| `spec.template.spec.containers[0].args[0]` | `-conf=/data/config.yaml` | Set intentionally to match this repository's desired-state for this component. |
| `spec.template.spec.containers[0].volumeMounts[0].mountPath` | `/data` | Set intentionally to match this repository's desired-state for this component. |
| `spec.template.spec.containers[0].volumeMounts[0].name` | `cfg` | Set intentionally to match this repository's desired-state for this component. |
| `spec.template.spec.containers[0].securityContext.allowPrivilegeEscalation` | `false` | Applies runtime hardening to reduce privilege and container escape risk. |
| `spec.template.spec.containers[0].securityContext.capabilities.drop` | `[ALL]` | Applies runtime hardening to reduce privilege and container escape risk. |
| `spec.template.spec.volumes[0].name` | `cfg` | Set intentionally to match this repository's desired-state for this component. |
| `spec.template.spec.volumes[0].configMap.name` | `event-exporter-cfg` | Set intentionally to match this repository's desired-state for this component. |

## `configmap.yaml` values explained

The `ConfigMap` stores exporter runtime configuration under `data.config.yaml`.

- `logLevel: debug`: verbose logging for troubleshooting.
- `logFormat: json`: structured logs.
- `route.routes`: ordered routing rules.
  - Rule 1 sends matching events to both `dump` and `loki` receivers.
  - Rule 2 drops events from namespace `observability` to reduce noise/feedback loops.
- `receivers.dump.stdout: {}`: writes events to container stdout.
- `receivers.loki.webhook.endpoint`: Loki push API endpoint.
- `headers`: static HTTP headers for Loki requests.
- `layout.streams.stream`: labels attached to each Loki stream (`severity`, `reason`, `namespace`, etc.).
- `layout.streams.values`: log entry payload and timestamp expression.

## `roles.yaml` values explained

- `ServiceAccount event-exporter`: identity used by the pod.
- `ClusterRole event-exporter`:
  - `apiGroups: ["*"]`, `resources: ["*"]`, `verbs: ["get", "watch", "list"]`: read-only access to all resource types so events can be enriched.
  - `coordination.k8s.io/leases` with `verbs: ["*"]`: full lease access (used by leader election patterns when needed).
- `ClusterRoleBinding event-exporter`: binds service account to cluster role.

## `kustomization.yaml` values explained

- `apiVersion: kustomize.config.k8s.io/v1beta1`: Kustomize API version.
- `kind: Kustomization`: declares Kustomize configuration.
- `resources`: ordered list of manifests to apply (`roles.yaml`, `deployment.yaml`, `configmap.yaml`).
