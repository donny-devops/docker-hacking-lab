#!/usr/bin/env bash
# MODULE 7: Registry hygiene check. Isolated lab only.
set -u

REGISTRY="${REGISTRY:-registry:5000}"

echo "[*] Registry catalog (unauthenticated GET is a configuration check)"
if command -v curl >/dev/null 2>&1; then
  curl -sf "http://${REGISTRY}/v2/" >/dev/null && echo "v2 API reachable without auth at ${REGISTRY}" || echo "v2 API not reachable (good if intended)"
else
  echo "curl not installed"
fi

if command -v docker >/dev/null 2>&1; then
  echo "[*] Environment keys on running containers (names matching secret patterns)"
  docker ps -q | while read -r cid; do
    echo "--- ${cid} ---"
    docker inspect --format '{{range .Config.Env}}{{println .}}{{end}}' "$cid" \
      | awk -F= 'BEGIN{IGNORECASE=1} $1 ~ /PASSWORD|SECRET|KEY|TOKEN/ {print $1}'
  done
fi

echo "[*] Remediation: require registry auth, pin digests, and stop publishing the registry to the host."
