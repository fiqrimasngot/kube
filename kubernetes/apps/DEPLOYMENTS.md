# Kubernetes Deployments Reference

This document explains every deployment currently defined under `kubernetes/apps`.  
Each entry includes:
- **Purpose**: what the deployment is used for.
- **Key manifests**: where to start when you need to configure or troubleshoot it.

## cert-manager

| Deployment | Purpose | Key manifests |
|---|---|---|
| `cert-manager/cert-manager` | Automates certificate issuance/renewal for in-cluster TLS. | `kubernetes/apps/cert-manager/cert-manager/ks.yaml`, `.../app/helmrelease.yaml` |

## database

| Deployment | Purpose | Key manifests |
|---|---|---|
| `database/cloudnative-pg` | PostgreSQL operator for managing PostgreSQL clusters. | `kubernetes/apps/database/cloudnative-pg/ks.yaml`, `.../app/helmrelease.yaml` |
| `database/dragonfly` | In-memory data store compatible with Redis use-cases. | `kubernetes/apps/database/dragonfly/ks.yaml`, `.../app/helmrelease.yaml` |
| `database/obsidian-couchdb` | CouchDB backend for Obsidian sync/workflow data. | `kubernetes/apps/database/obsidian-couchdb/ks.yaml`, `.../app/helmrelease.yaml` |
| `database/pgadmin` | Web UI for administering PostgreSQL databases. | `kubernetes/apps/database/pgadmin/ks.yaml`, `.../app/helmrelease.yaml` |

## default

| Deployment | Purpose | Key manifests |
|---|---|---|
| `default/actual` | Actual Budget personal finance application. | `kubernetes/apps/default/actual/ks.yaml`, `.../app/helmrelease.yaml` |
| `default/bytestash` | Self-hosted file/link stash and quick sharing utility. | `kubernetes/apps/default/bytestash/ks.yaml`, `.../app/helmrelease.yaml` |
| `default/cyberchef` | Browser-based data transformation and encoding toolkit. | `kubernetes/apps/default/cyberchef/ks.yaml`, `.../app/helmrelease.yaml` |
| `default/home-assistant` | Home automation platform for smart devices and integrations. | `kubernetes/apps/default/home-assistant/ks.yaml`, `.../app/helmrelease.yaml` |
| `default/homebox` | Home inventory and asset tracking application. | `kubernetes/apps/default/homebox/ks.yaml`, `.../app/helmrelease.yaml` |
| `default/homepage` | Dashboard/start page for services and links. | `kubernetes/apps/default/homepage/ks.yaml`, `.../app/helmrelease.yaml` |
| `default/kiwix` | Offline Wikipedia/knowledge base reader service. | `kubernetes/apps/default/kiwix/ks.yaml`, `.../app/helmrelease.yaml` |
| `default/mealie` | Recipe manager and meal-planning app. | `kubernetes/apps/default/mealie/ks.yaml`, `.../app/helmrelease.yaml` |
| `default/n8n` | Workflow automation and integration engine. | `kubernetes/apps/default/n8n/ks.yaml`, `.../app/helmrelease.yaml` |
| `default/nextcloud` | Self-hosted collaboration, storage, and sync platform. | `kubernetes/apps/default/nextcloud/ks.yaml`, `.../app/helmrelease.yaml` |
| `default/paperless` | Document ingestion and OCR-based archive system. | `kubernetes/apps/default/paperless/ks.yaml`, `.../app/helmrelease.yaml` |
| `default/searxng` | Privacy-focused metasearch engine instance. | `kubernetes/apps/default/searxng/ks.yaml`, `.../app/helmrelease.yaml` |
| `default/shlink` | URL shortener and link analytics service. | `kubernetes/apps/default/shlink/ks.yaml`, `.../app/helmrelease.yaml` |
| `default/wallabag` | Read-it-later and article archiving service. | `kubernetes/apps/default/wallabag/ks.yaml`, `.../app/helmrelease.yaml` |
| `default/web-app` | Example/sample web application deployment. | `kubernetes/apps/default/web-app/ks.yaml`, `.../app/helmrelease.yaml` |

## devops

| Deployment | Purpose | Key manifests |
|---|---|---|
| `devops/gha-runner-scale-set` | GitHub Actions runner scale set for job execution. | `kubernetes/apps/devops/gha-runner-scale-set/ks.yaml`, `.../app/helmrelease.yaml` |
| `devops/gha-runner-scale-set-controller` | Controller/operator for managing GitHub runner scale sets. | `kubernetes/apps/devops/gha-runner-scale-set-controller/ks.yaml`, `.../app/helmrelease.yaml` |
| `devops/kafka` | Apache Kafka event streaming platform deployment. | `kubernetes/apps/devops/kafka/ks.yaml`, `.../app/helmrelease.yaml`, `.../cluster/kafka-cluster.yaml` |
| `devops/ollama` | Local LLM serving stack (backend + UI). | `kubernetes/apps/devops/ollama/ks.yaml`, `.../backend/helmrelease.yaml`, `.../ui/helmrelease.yaml` |
| `devops/openclawd` | OpenClawd AI/chat tooling deployment. | `kubernetes/apps/devops/openclawd/ks.yaml`, `.../app/helmrelease.yaml` |

## flux-system

| Deployment | Purpose | Key manifests |
|---|---|---|
| `flux-system/flux-instance` | Main Flux instance reconciling cluster state from Git/OCI sources. | `kubernetes/apps/flux-system/flux-instance/ks.yaml`, `.../app/helmrelease.yaml` |
| `flux-system/flux-operator` | Flux operator lifecycle management. | `kubernetes/apps/flux-system/flux-operator/ks.yaml`, `.../app/helmrelease.yaml` |

## kube-system

| Deployment | Purpose | Key manifests |
|---|---|---|
| `kube-system/cilium` | CNI and network policy dataplane for Kubernetes networking. | `kubernetes/apps/kube-system/cilium/ks.yaml`, `.../app/helmrelease.yaml` |
| `kube-system/coredns` | Cluster DNS service for internal name resolution. | `kubernetes/apps/kube-system/coredns/ks.yaml`, `.../app/helmrelease.yaml` |
| `kube-system/metrics-server` | Resource metrics API for HPA and `kubectl top`. | `kubernetes/apps/kube-system/metrics-server/ks.yaml`, `.../app/helmrelease.yaml` |
| `kube-system/node-feature-discovery` | Labels nodes based on detected hardware/software features. | `kubernetes/apps/kube-system/node-feature-discovery/ks.yaml`, `.../app/helmrelease.yaml` |
| `kube-system/nvidia-plugin` | NVIDIA device plugin enabling GPU scheduling on nodes. | `kubernetes/apps/kube-system/nvidia-plugin/ks.yaml`, `.../app/helmrelease.yaml` |
| `kube-system/reloader` | Triggers workload restarts on ConfigMap/Secret changes. | `kubernetes/apps/kube-system/reloader/ks.yaml`, `.../app/helmrelease.yaml` |

## media

| Deployment | Purpose | Key manifests |
|---|---|---|
| `media/bazarr` | Subtitle management for media libraries. | `kubernetes/apps/media/bazarr/ks.yaml`, `.../app/helmrelease.yaml` |
| `media/blender` | Blender service workload for rendering/interactive use. | `kubernetes/apps/media/blender/ks.yaml`, `.../app/helmrelease.yaml` |
| `media/flaresolverr` | Anti-bot challenge solver used by indexer apps. | `kubernetes/apps/media/flaresolverr/ks.yaml`, `.../app/helmrelease.yaml` |
| `media/freshrss` | RSS feed aggregation and reader platform. | `kubernetes/apps/media/freshrss/ks.yaml`, `.../app/helmrelease.yaml` |
| `media/ghost` | Ghost publishing/blog platform. | `kubernetes/apps/media/ghost/ks.yaml`, `.../app/helmrelease.yaml` |
| `media/i2pd` | I2P router service for anonymized network access. | `kubernetes/apps/media/i2pd/ks.yaml`, `.../app/helmrelease.yaml` |
| `media/immich` | Self-hosted photo/video backup and management platform. | `kubernetes/apps/media/immich/ks.yaml`, `.../app/helmrelease.yaml` |
| `media/jellyfin` | Media streaming server. | `kubernetes/apps/media/jellyfin/ks.yaml`, `.../app/helmrelease.yaml` |
| `media/jellyseerr` | Media request management front-end for Jellyfin ecosystem. | `kubernetes/apps/media/jellyseerr/ks.yaml`, `.../app/helmrelease.yaml` |
| `media/lidarr` | Music library acquisition/management automation. | `kubernetes/apps/media/lidarr/ks.yaml`, `.../app/helmrelease.yaml` |
| `media/prowlarr` | Indexer aggregator for *arr applications. | `kubernetes/apps/media/prowlarr/ks.yaml`, `.../app/helmrelease.yaml` |
| `media/radarr` | Movie acquisition and library automation. | `kubernetes/apps/media/radarr/ks.yaml`, `.../app/helmrelease.yaml` |
| `media/sabnzbd` | Usenet downloader backend. | `kubernetes/apps/media/sabnzbd/ks.yaml`, `.../app/helmrelease.yaml` |
| `media/sonarr` | TV series acquisition and library automation. | `kubernetes/apps/media/sonarr/ks.yaml`, `.../app/helmrelease.yaml` |
| `media/steam` | Steam-related workload (game/service support). | `kubernetes/apps/media/steam/ks.yaml`, `.../app/helmrelease.yaml` |
| `media/tdarr` | Distributed transcoding/health-check automation for media files. | `kubernetes/apps/media/tdarr/ks.yaml`, `.../app/helmrelease.yaml` |

## network

| Deployment | Purpose | Key manifests |
|---|---|---|
| `network/cloudflare-dns` | External DNS updates against Cloudflare zones. | `kubernetes/apps/network/cloudflare-dns/ks.yaml`, `.../app/helmrelease.yaml` |
| `network/cloudflare-tunnel` | Cloudflare Tunnel connector for exposing services externally. | `kubernetes/apps/network/cloudflare-tunnel/ks.yaml`, `.../app/helmrelease.yaml` |
| `network/envoy-gateway` | Gateway API dataplane/control-plane based on Envoy. | `kubernetes/apps/network/envoy-gateway/ks.yaml`, `.../app/helmrelease.yaml` |
| `network/k8s-gateway` | Internal DNS gateway/rewriter services for local domains. | `kubernetes/apps/network/k8s-gateway/ks.yaml`, `.../app/helmrelease.yaml` |
| `network/pihole` | DNS sinkhole and ad-blocking resolver. | `kubernetes/apps/network/pihole/ks.yaml`, `.../app/helmrelease.yaml` |
| `network/smtp-relay` | SMTP relay for outbound mail from cluster workloads. | `kubernetes/apps/network/smtp-relay/ks.yaml`, `.../app/helmrelease.yaml` |
| `network/tailscale-operator` | Tailscale operator and connectors for secure network access. | `kubernetes/apps/network/tailscale-operator/ks.yaml`, `.../app/helmrelease.yaml`, `.../connectors/` |

## observability

| Deployment | Purpose | Key manifests |
|---|---|---|
| `observability/blackbox-exporter` | Probes endpoint availability from Prometheus. | `kubernetes/apps/observability/blackbox-exporter/ks.yaml`, `.../app/helmrelease.yaml` |
| `observability/dcgm-exporter` | Exposes NVIDIA GPU metrics for monitoring. | `kubernetes/apps/observability/dcgm-exporter/ks.yaml`, `.../app/helmrelease.yaml` |
| `observability/goldilocks` | Rightsizing recommendations for workload resources. | `kubernetes/apps/observability/goldilocks/ks.yaml`, `.../app/helmrelease.yaml` |
| `observability/kube-prometheus-stack` | Core monitoring stack (Prometheus, Alertmanager, Grafana, exporters). | `kubernetes/apps/observability/kube-prometheus-stack/ks.yaml`, `.../app/helmrelease.yaml` |
| `observability/loki` | Log aggregation backend. | `kubernetes/apps/observability/loki/ks.yaml`, `.../app/helmrelease.yaml` |
| `observability/promtail` | Log shipping agent for Loki. | `kubernetes/apps/observability/promtail/ks.yaml`, `.../app/helmrelease.yaml` |
| `observability/smartctl-exporter` | Disk SMART metric exporter. | `kubernetes/apps/observability/smartctl-exporter/ks.yaml`, `.../app/helmrelease.yaml` |
| `observability/speedtest-exporter` | Network speed test metrics exporter. | `kubernetes/apps/observability/speedtest-exporter/ks.yaml`, `.../app/helmrelease.yaml` |
| `observability/uptime-kuma` | Service uptime status monitoring dashboard. | `kubernetes/apps/observability/uptime-kuma/ks.yaml`, `.../app/helmrelease.yaml` |

## openebs-system

| Deployment | Purpose | Key manifests |
|---|---|---|
| `openebs-system/openebs` | OpenEBS local storage components and CSI support. | `kubernetes/apps/openebs-system/openebs/ks.yaml`, `.../app/helmrelease.yaml` |

## rook-ceph

| Deployment | Purpose | Key manifests |
|---|---|---|
| `rook-ceph/rook-ceph` | Ceph storage operator and cluster resources for distributed storage. | `kubernetes/apps/rook-ceph/rook-ceph/ks.yaml`, `.../app/helmrelease.yaml`, `.../cluster/helmrelease.yaml` |

## security

| Deployment | Purpose | Key manifests |
|---|---|---|
| `security/authentik` | Identity provider and SSO platform for applications. | `kubernetes/apps/security/authentik/ks.yaml`, `.../app/helmrelease.yaml` |

## storage

| Deployment | Purpose | Key manifests |
|---|---|---|
| `storage/csi-driver-nfs` | NFS CSI driver for dynamic or static NFS-backed PVCs. | `kubernetes/apps/storage/csi-driver-nfs/ks.yaml`, `.../app/helmrelease.yaml` |
| `storage/minio` | S3-compatible object storage service. | `kubernetes/apps/storage/minio/ks.yaml`, `.../app/helmrelease.yaml` |
| `storage/nfs-server` | NFS server deployment to provide shared volumes. | `kubernetes/apps/storage/nfs-server/ks.yaml`, `.../app/helmrelease.yaml` |
| `storage/samba` | SMB/CIFS file sharing service. | `kubernetes/apps/storage/samba/ks.yaml`, `.../app/helmrelease.yaml` |
| `storage/scrutiny` | Disk health monitoring and reporting service. | `kubernetes/apps/storage/scrutiny/ks.yaml`, `.../app/helmrelease.yaml` |

## volsync-system

| Deployment | Purpose | Key manifests |
|---|---|---|
| `volsync-system/snapshot-controller` | CSI snapshot CRDs/controller for volume snapshots. | `kubernetes/apps/volsync-system/snapshot-controller/ks.yaml`, `.../app/helmrelease.yaml` |
| `volsync-system/volsync` | Volume replication and backup orchestration. | `kubernetes/apps/volsync-system/volsync/ks.yaml`, `.../app/helmrelease.yaml` |

## Notes

- The `ks.yaml` files describe Flux `Kustomization` ordering/dependencies.
- The `app/helmrelease.yaml` files usually hold the main runtime configuration.
- Some deployments include additional folders like `cluster/`, `connectors/`, or `resources/` for extra objects required by that deployment.
