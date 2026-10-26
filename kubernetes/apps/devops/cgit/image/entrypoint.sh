#!/bin/sh
set -eu

install -d -o git -g git -m 0700 /home/git/.ssh
install -d -o git -g git -m 0700 /srv/git/.cgit-cache
printf '%s\n' "${CGIT_SSH_AUTHORIZED_KEYS:-}" > /home/git/.ssh/authorized_keys
chown git:git /home/git/.ssh/authorized_keys
chmod 0600 /home/git/.ssh/authorized_keys

# Generate host keys in the writable git home because the pod is non-root.
if [ ! -f /home/git/.ssh/ssh_host_ed25519_key ]; then
  ssh-keygen -q -t ed25519 -N '' -f /home/git/.ssh/ssh_host_ed25519_key
fi
chown git:git /home/git/.ssh/ssh_host_ed25519_key*
# Keep SSH on an unprivileged port; the Service exposes it as port 22.
/usr/sbin/sshd -D -e -p 2222 -h /home/git/.ssh/ssh_host_ed25519_key &
ssh_pid=$!

# fcgiwrap's socket is shared with nginx, both run as the git UID.
fcgiwrap -s unix:/run/fcgiwrap.socket &
fcgi_pid=$!
nginx -g 'daemon off;' &
nginx_pid=$!

trap 'kill "$ssh_pid" "$fcgi_pid" "$nginx_pid" 2>/dev/null || true' TERM INT
wait -n "$ssh_pid" "$fcgi_pid" "$nginx_pid"
exit $?
