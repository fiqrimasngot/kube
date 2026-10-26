FROM debian:trixie-slim

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      cgit nginx fcgiwrap git git-lfs openssh-server \
      ca-certificates curl python3-pygments python3-markdown tini \
 && rm -rf /var/lib/apt/lists/* \
 && useradd --system --uid 1000 --create-home --shell /usr/bin/git-shell git \
 && mkdir -p /run/sshd /run/fcgiwrap /srv/git /etc/ssh/authorized_keys \
 && chown -R git:git /srv/git /home/git /etc/ssh/authorized_keys \
 && chmod 0755 /run/fcgiwrap

COPY cgitrc /etc/cgitrc
COPY nginx.conf /etc/nginx/nginx.conf
COPY entrypoint.sh /usr/local/bin/cgit-entrypoint
RUN chmod 0755 /usr/local/bin/cgit-entrypoint \
 && ssh-keygen -A \
 && printf '%s\n' 'PasswordAuthentication no' 'KbdInteractiveAuthentication no' 'PermitRootLogin no' 'UsePAM no' 'AllowUsers git' >> /etc/ssh/sshd_config

EXPOSE 8080 2222
ENTRYPOINT ["/usr/bin/tini", "--", "/usr/local/bin/cgit-entrypoint"]
