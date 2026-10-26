# cgit deployment

This app deploys the Debian trixie cgit/nginx/fcgiwrap image described in `image/`.
The image must be built and published before Flux reconciliation, then `CGIT_IMAGE`
must be added to the cluster-secrets substitution source. The image intentionally
runs as UID 1000 and serves HTTP on 8080 and SSH on 2222; the Services expose
HTTP on 8080 and SSH on port 22.

Required secret (SOPS-managed, never commit plaintext keys):

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: cgit-ssh-authorized-keys
stringData:
  authorized_keys: |
    restrict,no-port-forwarding,no-agent-forwarding,no-X11-forwarding,no-pty ssh-ed25519 ...
```

Repositories are bare Git repositories under `/srv/git`. The nginx configuration
routes Git smart HTTP requests to `git-http-backend` and all browser requests to
cgit CGI. The Gateway's internal HTTPS listener and existing HTTP redirect provide
TLS; no public listener or host firewall/SELinux changes are used.

## Import an SRPM

`cgit/srpm-import` stores one package per repository. It calls the backend's
idempotent `newrepo` helper, unpacks the SRPM, commits the spec and patches at the
repository root, and tags the import as `<version>-<release>`. Source archives
are kept outside Git under `/srv/git/lookaside/<package>/`; the committed
`sources` file contains SHA-256 checksums. Raw `.src.rpm` files are not committed.

Run it from the cgit/SSH pod (where `newrepo`, `/srv/git`, and the lookaside
volume are available), or point it at a client-side Git remote and provide an
appropriate repository-creation wrapper:

```sh
cgit/srpm-import --repo hello hello-1.0-1.src.rpm
cgit/srpm-import directory-containing-srpms/
```

For a client-side checkout, set `SRPM_GIT_REMOTE` (a base URL or a `%s` template)
and `SRPM_LOOKASIDE`, and use `--newrepo`/`--ssh-host` for the server's
repository-creation mechanism. Re-running an import whose exact tag already
exists is a no-op. The script deliberately uses the lookaside strategy from
`DEPLOYMENT_PLAN.md`: cgit can browse Git trees but does not render Git LFS
objects, and this deployment does not provide an LFS server.

To rebuild an SRPM, clone the package repo, copy each archive named in `sources`
from `/srv/git/lookaside/<package>/` into the rpmbuild `SOURCES` directory (and
verify its checksum), then run `rpmbuild -bs <package>.spec`. Patches and other
small inputs are in the repository root; use the spec's referenced filenames.

## URLs and Git access

The internal browser URL is https://cgit.kube.dug.com/ (reachable through the
LAN/VPN and trusted internal CA). HTTPS clone URLs are shown by cgit. SSH uses
`ssh://git@cgit.kube.dug.com:22/<repo>.git`; port 22 is a ClusterIP service and
is not publicly exposed. Add a public key to the SOPS-managed
`cgit-ssh-authorized-keys` Secret; private keys never belong in this repository.

## Data protection scope

This deployment deliberately does not create, restore, or configure backups,
snapshots, VolSync resources, or backup credentials. The repository PVC is the
live storage only; arrange any external data-protection policy independently
without adding it to this application.

## Maintenance and upgrades

The cgit image creates `/srv/git/.cgit-cache` with mode 0700 at startup; this
keeps generated cgit cache data on the same durable PVC as the repositories.
Run `git gc` during a maintenance window (on a quiesced writer) before large
imports. Upgrade by publishing a new immutable image tag, updating `CGIT_IMAGE`
in the SOPS-managed cluster substitution, reconciling the Flux Kustomization,
and checking the HTTPS readiness probe, SSH clone, HTTP clone, and cgit snapshot
download.

## Current operational gate

The manifests and render checks are committed with the app, but live end-to-end
checks require the operator to provision `CGIT_IMAGE` and the
`cgit-ssh-authorized-keys` Secret. Until those inputs exist, the cgit Deployment
cannot start.

