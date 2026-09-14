#!/usr/bin/env bash
# MODULE 5: Detect Docker socket exposure. Isolated lab only.
# Does not call mutating Engine API methods.
set -u

SOCK="${DOCKER_SOCKET:-/var/run/docker.sock}"

echo "[*] Checking for Engine Unix socket at ${SOCK}"
if [[ -S "$SOCK" ]]; then
  echo "[!] FINDING: socket exists. Mounting it is host-root equivalent."
  ls -l "$SOCK"
  echo "[*] Remediation: unmount the socket; use a least-privilege API proxy."
else
  echo "No Engine socket at ${SOCK}"
fi

if command -v docker >/dev/null 2>&1; then
  echo "[*] Host-side inspect of vuln-web mounts (if engine CLI is available)"
  docker inspect vuln-web --format '{{range .Mounts}}{{println .Source "->" .Destination}}{{end}}' 2>/dev/null || true
fi
