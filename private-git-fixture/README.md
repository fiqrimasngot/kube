# Private Git fixture: incomplete draft

This is an offline proof of the forced-command gate only. It is not a private
mirror deployment and must not receive real source or credentials. Nothing in
this directory is registered with Flux. No SSH server, key, PVC, Service or
network policy is provisioned here.

`upload-only.py` accepts exactly the SSH command Git uses for an upload-pack of
`/fixture.git`. It rejects shell commands, other paths, and receive-pack. The
repository path is hardcoded; using this gate for any other repository requires
a separate review. Run `python3 -m unittest discover -s private-git-fixture -v`
from the repository root. The clone test uses a synthetic repository and a fake
SSH transport, so it does not test SSH authentication or network isolation.

## Before this can serve real source

- Locate the actual `/pxe/bin/image_cluster` implementation and its callers;
  establish the exact input, output, ownership, mode and runtime dependencies.
- Choose a separate private Git service, not the existing cgit scan path. Give
  it a dedicated non-Ceph PVC and do not mount that volume in public cgit.
- Build and pin a reviewed SSH image. Restrict an independently provisioned
  reader public key with an SSH forced command and `restrict`; disable password,
  interactive shell, forwarding and environment injection. Persist and pin
  its host key. Mount the repository read-only for the serving process.
- Provision a separate authorized updater identity and isolated update path;
  a read-only server cannot synchronize itself. Protect data at rest and in
  backups, define key rotation, and ensure untrusted pull requests cannot use
  the reader credential or run on the privileged own runner.
- Use a ClusterIP service, default-deny ingress, and a narrowly selected runner
  workload. Confirm the actual Actions job pod labels and network policies, not
  just the controller or runner pod labels. Validate fresh unauthorized pods,
  push, path traversal, shell access, HTTP access, and host-key mismatch all
  fail. Test a real clone from the authorized job pod after the service exists.
- Test the exact non-Ceph storage class and PVC mount in this cluster and
  independently verify Nexus repository format, authorization, and access
  policy. No Nexus or cgit workload was present in this cluster at review time;
  the existing cgit Flux object reported missing `CGIT_IMAGE`.

The live `gha-kube` runner's `actions.github.com/repository=kube` and
`actions.github.com/scale-set-name=gha-kube` labels identify the runner pod,
but they do not establish which labels a hook-created job pod carries.
NetworkPolicy selectors alone are not a security boundary against users allowed
to create arbitrary pods with those labels. Verify namespace RBAC and the CNI's
actual enforcement as well as credential isolation.
