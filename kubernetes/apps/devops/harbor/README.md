# Harbor deployment configuration

Target: the single-node Talos Kubernetes cluster (`k8s-0`, 10.32.1.51), managed by Flux.

Deployment method: Harbor Helm chart 1.19.4 (Harbor 2.15.4) from `https://helm.goharbor.io`, reconciled by Flux `HelmRelease` in namespace `devops`.

Endpoint and networking:

- Canonical hostname: `harbor.fiqriha.kim`.
- Harbor is exposed internally as ClusterIP service `devops/harbor:80`.
- Gateway API HTTPRoute attaches HTTPS on both `network/envoy-external` (10.32.1.13) and `network/envoy-internal` (10.32.1.12). TLS terminates at Envoy using the existing wildcard certificate for `*.fiqriha.kim`; Harbor's chart-side TLS is intentionally disabled.
- Docker clients use `https://harbor.fiqriha.kim`; the Gateway routes the complete Harbor API, including `/v2/`, to the chart's `harbor` service.

Persistence:

- All Harbor PVCs use the existing `ceph-block` StorageClass (Rook Ceph, RWO): registry 200Gi, database 20Gi, Redis 5Gi, job logs 5Gi, and Trivy 10Gi.
- The chart sets `resourcePolicy: keep`; backups/restore must still be added to the existing VolSync policy before production use.
- The cluster currently has a Ready node, the Ceph-backed StorageClass, both Envoy Gateways programmed, and a Ready `letsencrypt-production` ClusterIssuer.

Administrator credentials:

- The chart is configured with `existingSecretAdminPassword: harbor-admin` and key `HARBOR_ADMIN_PASSWORD`; no password is committed here.
- Before enabling the Kustomization, create `devops/harbor-admin` as a SOPS-encrypted Secret (or provision it through the cluster's approved secret-management path). Do not apply `secret-template.yaml`; it is documentation only and intentionally contains a sentinel value.
- The initial password should be randomly generated and changed from the Harbor portal after first login. Record it in the operator's password manager, not Git.

Prerequisites before deployment:

1. Provision the encrypted `harbor-admin` Secret in namespace `devops`.
2. Ensure DNS for `harbor.fiqriha.kim` resolves to the Envoy external/internal addresses as appropriate for the client network.
3. Confirm the wildcard certificate covers `harbor.fiqriha.kim`; otherwise add a cert-manager Certificate/ReferenceGrant for the Gateway TLS listener.
4. Add Harbor PVCs to the site's VolSync backup plan before storing important images.

The manifest is deliberately not deployed by this task; the dependent installation task should create the Secret, reconcile Flux, and verify the UI and registry API.
