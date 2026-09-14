#!/usr/bin/env bash
# MODULE 8: Supply-chain hygiene. Isolated lab only.
# Does not build or push backdoored images.
set -u

echo "[*] Compose image references (floating tags are a finding)"
if [[ -f docker-compose.yml ]]; then
  awk '/image:/{print}' docker-compose.yml
elif [[ -f /workspace/docker-compose.yml ]]; then
  awk '/image:/{print}' /workspace/docker-compose.yml
fi

if command -v docker >/dev/null 2>&1; then
  echo "[*] Local images missing a digest pin"
  docker images --format '{{.Repository}}:{{.Tag}} {{.Digest}}' | awk '
    $2 == "<none>" { print "[unpinned] " $1; next }
    { print "[pinned] " $1 " " $2 }
  '
fi

echo "[*] Remediation: pin by digest, sign with cosign, scan in CI, allow-list the registry."
echo "[*] Do not push typosquat tags into a shared registry."
