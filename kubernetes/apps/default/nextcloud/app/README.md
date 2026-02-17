# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `helmrelease.yaml`
- `kustomization.yaml`
- `secrets.sops.yaml`

## `helmrelease.yaml` values

### Document 1: `HelmRepository` `nextcloud`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `source.toolkit.fluxcd.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRepository` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `nextcloud` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.interval` | `1h` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.url` | `https://nextcloud.github.io/helm/` | Set intentionally to match this repository's desired-state for this component. |

### Document 2: `HelmRelease` `nextcloud`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `helm.toolkit.fluxcd.io/v2` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HelmRelease` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `nextcloud` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.chart.spec.chart` | `nextcloud` | Selects the specific Helm chart that provides this workload. |
| `spec.chart.spec.version` | `8.7.0` | Pins the chart version for repeatable deployments and controlled upgrades. |
| `spec.interval` | `2h` | Uses a reconcile interval that balances configuration freshness with API/controller load. |
| `spec.install.timeout` | `60m` | Bounds how long reconciliation may run before surfacing failure for faster troubleshooting. |
| `spec.upgrade.timeout` | `60m` | Bounds how long reconciliation may run before surfacing failure for faster troubleshooting. |
| `spec.values.deploymentAnnotations.secret.reloader.stakater.com/reload` | `nextcloud-secret` | Adds controller-specific hints/behaviors needed by tooling in this cluster. |
| `spec.values.phpClientHttpsFix.enabled` | `True` | Feature toggle chosen to match this environment's operational requirements. |
| `spec.values.nextcloud.host` | `cloud.${SECRET_DOMAIN}` | Routes traffic or integration calls to the intended DNS endpoint. |
| `spec.values.nextcloud.extraInitContainers` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.nextcloud.extraInitContainers.[0].name` | `init-db` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.nextcloud.extraInitContainers.[0].image` | `ghcr.io/onedr0p/postgres-init:17.4@sha256:43dd04e91e861cf912378bad987afa168fa4f13d05528...` | Fixes the container image used at runtime so behavior is predictable across reconciliations. |
| `spec.values.nextcloud.extraVolumes` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.nextcloud.extraVolumes.[0].name` | `nfs-home` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.nextcloud.extraVolumeMounts` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.nextcloud.extraVolumeMounts.[0].name` | `nfs-home` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.nextcloud.extraVolumeMounts.[0].mountPath` | `/mnt/data/home` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.nextcloud.extraEnv` | `list[5]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.nextcloud.extraEnv.[0].name` | `REDIS_HOST` | Set intentionally to match this repository's desired-state for this component. |
| `spec.values.nextcloud.extraEnv.[0].value` | `dragonfly.database.svc.cluster.local` | Set intentionally to match this repository's desired-state for this component. |

### Document 3: `HTTPRoute` `nextcloud`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `gateway.networking.k8s.io/v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `HTTPRoute` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `nextcloud` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `spec.hostnames` | `['cloud.${SECRET_DOMAIN}']` | Routes traffic or integration calls to the intended DNS endpoint. |
| `spec.parentRefs` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `spec.parentRefs.[0].name` | `envoy-external` | Set intentionally to match this repository's desired-state for this component. |
| `spec.parentRefs.[0].namespace` | `network` | Separates this component into the correct tenancy boundary and avoids cross-namespace sprawl. |
| `spec.rules` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./helmrelease.yaml', './secrets.sops.yaml']` | Defines which child manifests are composed together as this deployment unit. |


## `secrets.sops.yaml` values

### Document 1: `Secret` `nextcloud-secret`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Secret` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `nextcloud-secret` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `stringData.ADMIN_USER` | `ENC[AES256_GCM,data:mVCwtVztSp1mPJCE,iv:uUu+V7eriuMSBloMLaw+OLgIe8gzMBu9jTncHhKdNco=,ta...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.ADMIN_PASS` | `ENC[AES256_GCM,data:i+JWUBlBro6coXN3S+UjGaCP7/MFQMaTUYUCknujkLQ=,iv:NOHl8tvL/epkPCKjSGl...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.REDIS_PASSWORD` | `ENC[AES256_GCM,data:frtlGOk7ZbTm+vfkq46XJW1oJ9qWjSG5i9fycERJ8N4=,iv:zD/pz4yD0SvpWJ39ylX...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.S3_ACCESS_KEY` | `ENC[AES256_GCM,data:9n8AbXyr3FhWd+4CjFe8V/HBayg=,iv:5CeqKkJLiq54fMjmNsniHdXMbw/WXJH1n9z...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.S3_SECRET_KEY` | `ENC[AES256_GCM,data:UGQimNy23mRfmE0pWyGDO9slK3wjxMVUQ1y8uyqwMmvYroJUcY6P7g==,iv:LskWkk0...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.SMTP_USERNAME` | `ENC[AES256_GCM,data:vE0FTTC9ak5m/IPmNVX7hd5xb8+4Ww==,iv:l+EdtxtMG5Z+ya1NjvxwsFz/qknm6wT...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.SMTP_PASSWORD` | `ENC[AES256_GCM,data:l2jdbRxMPdVoTXekcSzosohX+5hjhdOFiZ2kuVyQfOW00y4CTbQ3bOXqymN2zsV+CDk...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.TOKEN` | `` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.SMTP_HOST` | `ENC[AES256_GCM,data:UbASw68odmx3axK///xQ/lwMT3py2l/mXJlz3UkvZiCfnR0s,iv:U2ddGyY7g6gCylg...` | Routes traffic or integration calls to the intended DNS endpoint. |
| `stringData.OIDC_CLIENT_ID` | `` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.OIDC_CLIENT_SECRET` | `` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.INIT_POSTGRES_DBNAME` | `ENC[AES256_GCM,data:s7WBvvNp9nd/,iv:I4ucVrPiCydm+vfVrwg5eTxIuQgMB8VYiPzNOYeckZg=,tag:cD...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.INIT_POSTGRES_HOST` | `ENC[AES256_GCM,data:h0FsHcrlkkc5S07sPWn3/bNdN/rP7zu/XUeyOAzK3UhOnVuU7yk=,iv:jaUJ7anf0e7...` | Routes traffic or integration calls to the intended DNS endpoint. |
| `stringData.INIT_POSTGRES_USER` | `ENC[AES256_GCM,data:pqDNgX8RnhA6,iv:mgUEWLoGs6r/Y0oYb6Kr19OwKuPLYYcZfjP2l5Ii01Q=,tag:mr...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.INIT_POSTGRES_PASS` | `ENC[AES256_GCM,data:ZYd4uQlGpNdkK/uCbEOD7lq5Snw=,iv:LfV+90Fsk/QLtg5oJbrhEksBwSJ5Andv5nC...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.INIT_POSTGRES_SUPER_PASS` | `ENC[AES256_GCM,data:14twojwwPOey2MI=,iv:VnF0UfbEfi8pcJXUjcnWXpdSavXUk77kReIS+ZbrwyM=,ta...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].recipient` | `age1sumyxgm2je4txw82k838698mmqmf40wsw6j8eu3jhf5v54g4sslqpchxuf` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].enc` | `-----BEGIN AGE ENCRYPTED FILE----- YWdlLWVuY3J5cHRpb24ub3JnL3YxCi0+IFgyNTUxOSArTHMwd1Fr...` | Set intentionally to match this repository's desired-state for this component. |
