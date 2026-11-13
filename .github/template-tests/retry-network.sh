#!/usr/bin/env bash
# Retry only the observed transient HTTPS transport error. Never turn a failed
# validation into success: every attempt runs the original command in full.
set -uo pipefail

if (( $# == 0 )); then
    printf 'Usage: retry-network.sh COMMAND [ARG...]\n' >&2
    exit 2
fi

log=$(mktemp) || exit 1
trap 'rm -f "$log"' EXIT

for attempt in 1 2 3; do
    "$@" 2>&1 | tee "$log"
    status=${PIPESTATUS[0]}
    if (( status == 0 )); then
        exit 0
    fi
    if (( attempt == 3 )) || ! grep -Fq 'tls: first record does not look like a TLS handshake' "$log"; then
        exit "$status"
    fi
    printf '::warning::Transient TLS download failure; retrying (%s/3).\n' "$((attempt + 1))"
    sleep "${NETWORK_RETRY_DELAY:-10}"
done
