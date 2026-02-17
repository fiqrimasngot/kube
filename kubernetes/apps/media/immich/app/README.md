# app manifests

This README documents manifests deployed from this directory and explains the configured values at a practical level.

## Manifest files

- `configmap.yaml`
- `kustomization.yaml`
- `secrets.sops.yaml`

## `configmap.yaml` values

### Document 1: `ConfigMap` `immich-config`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `ConfigMap` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `immich-config` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `data.DB_PORT` | `5432` | Uses the network port expected by clients, probes, or upstream services. |
| `data.LOG_LEVEL` | `verbose` | Set intentionally to match this repository's desired-state for this component. |
| `data.REDIS_HOSTNAME` | `dragonfly.database.svc.cluster.local` | Routes traffic or integration calls to the intended DNS endpoint. |
| `data.REDIS_DBINDEX` | `1` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `data.REDIS_PORT` | `6379` | Uses the network port expected by clients, probes, or upstream services. |
| `data.DISABLE_REVERSE_GEOCODING` | `true` | Enabled because this behavior is required for reliable operation in this environment. |
| `data.ENABLE_MAPBOX` | `false` | Disabled intentionally to reduce risk, noise, or unnecessary overhead in this environment. |
| `data.NODE_ENV` | `production` | Set intentionally to match this repository's desired-state for this component. |
| `data.IMMICH_SERVER_URL` | `http://immich-server.media.svc.cluster.local:3001` | Set intentionally to match this repository's desired-state for this component. |
| `data.IMMICH_MACHINE_LEARNING_URL` | `http://immich-machine-learning.media.svc.cluster.local:3003` | Set intentionally to match this repository's desired-state for this component. |
| `data.TRANSFORMERS_CACHE` | `/usr/src/app/.transformers_cache` | Set intentionally to match this repository's desired-state for this component. |
| `data.TZ` | `${TIMEZONE}` | Set intentionally to match this repository's desired-state for this component. |
| `data.IMMICH_MEDIA_LOCATION` | `/usr/src/app/upload` | Set intentionally to match this repository's desired-state for this component. |


## `kustomization.yaml` values

### Document 1: `Kustomization` `(none)`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `kustomize.config.k8s.io/v1beta1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Kustomization` | Declares which Kubernetes object/controller should process this manifest. |
| `resources` | `['./configmap.yaml', './secrets.sops.yaml', './server', './machine-learning']` | Defines which child manifests are composed together as this deployment unit. |


## `secrets.sops.yaml` values

### Document 1: `Secret` `immich-secret`

- `metadata.namespace`: `cluster-scoped` — Namespace scope for this resource.

| Field | Value | Meaning |
|---|---|---|
| `apiVersion` | `v1` | Pins the manifest to the API version expected by this cluster and controller. |
| `kind` | `Secret` | Declares which Kubernetes object/controller should process this manifest. |
| `metadata.name` | `immich-secret` | Keeps object identity stable so upgrades and references continue to work predictably. |
| `stringData.DB_DATABASE_NAME` | `ENC[AES256_GCM,data:4nFOu9pb,iv:annqWL4iWAkxRbQW1+UxSHc3fo4Nb/6qP4qDjHvdMjE=,tag:8i4Dt/...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.DB_HOSTNAME` | `ENC[AES256_GCM,data:l56WsS7GHyjTmBZiJdYQN2HA2chYI/1BVPkU453BTyYFnc1ZlVY=,iv:EY7uDSwBj97...` | Routes traffic or integration calls to the intended DNS endpoint. |
| `stringData.DB_USERNAME` | `ENC[AES256_GCM,data:amMH+sD9Hdk=,iv:wiiZlWLxEv0E+1f4EAdc8tjP9U750kyC5+HL77ZgOzs=,tag:hW...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.DB_PASSWORD` | `ENC[AES256_GCM,data:ZY+ccn82zJUPLGc=,iv:HUvUxSzrxWVqM52ElHUKaQrHJA9NbceE10cqLhdnUuM=,ta...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.JWT_SECRET` | `ENC[AES256_GCM,data:YA8/l6lhfdCxAlcbkLjDkkHv3pVnXUi3bWhvbsjO7a8=,iv:A59VRLV4Lf5L0LMgDaJ...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.INIT_POSTGRES_DBNAME` | `ENC[AES256_GCM,data:ZGcNzD/1,iv:qiq6gZb6IWHMIuylTasq3E0tevp7ekvVpIH9y5V0RM0=,tag:K392B1...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.INIT_POSTGRES_HOST` | `ENC[AES256_GCM,data:utBMGODvEQmiKkkEpZKJH/yBe31BBFpmJUaXgNSEyP+s2SeiT/0=,iv:y5Jy9X1dxp7...` | Routes traffic or integration calls to the intended DNS endpoint. |
| `stringData.INIT_POSTGRES_USER` | `ENC[AES256_GCM,data:1JIUHXgGdRM=,iv:YE2/HkI/GbpddUMVwW7brQiJsH/T94XEC1Nrk7Vm7gA=,tag:MR...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.INIT_POSTGRES_PASS` | `ENC[AES256_GCM,data:8pMFcBO4jqX4gtk=,iv:DCS3viLok5MCAmXE5aPczrwlNahMWpNnT//wRNMDKNo=,ta...` | Set intentionally to match this repository's desired-state for this component. |
| `stringData.INIT_POSTGRES_SUPER_PASS` | `ENC[AES256_GCM,data:XcRGuX4M/OzI2qU=,iv:oTu3z+Q5z79mUlLlLLuOV3Pj/PyV88RZecXhfWSnQTw=,ta...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age` | `list[1]` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].recipient` | `age1sumyxgm2je4txw82k838698mmqmf40wsw6j8eu3jhf5v54g4sslqpchxuf` | Set intentionally to match this repository's desired-state for this component. |
| `sops.age.[0].enc` | `-----BEGIN AGE ENCRYPTED FILE----- YWdlLWVuY3J5cHRpb24ub3JnL3YxCi0+IFgyNTUxOSBNRm0wbXly...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.lastmodified` | `2026-02-17T11:15:06Z` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
| `sops.mac` | `ENC[AES256_GCM,data:SoqpXJwiwJYM4pAPaSlbtYwdAzF2OTWsgakxyxpMgAPWz92UYr1L6N4bmTQitJvm/ip...` | Set intentionally to match this repository's desired-state for this component. |
| `sops.encrypted_regex` | `^(data|stringData)$` | Set intentionally to match this repository's desired-state for this component. |
| `sops.mac_only_encrypted` | `True` | Enabled because this behavior is required for reliable operation in this environment. |
| `sops.version` | `3.11.0` | Numeric value tuned for current workload size, reliability, and cluster capacity. |
