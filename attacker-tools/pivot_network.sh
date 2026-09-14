#!/usr/bin/env bash
# MODULE 9: Network position mapping. Isolated lab only.
# Does not send SSRF payloads against application endpoints.
set -u

echo "[*] Attacker network position"
if command -v ip >/dev/null 2>&1; then
  ip addr show
  ip route
fi

echo "[*] Compose networks: lab-external 172.20.0.0/24, lab-internal 172.22.0.0/24 (internal)"
echo "[*] internal-db should not have a host-published port."

if command -v docker >/dev/null 2>&1; then
  docker inspect internal-db --format 'ports={{json .NetworkSettings.Ports}} networks={{json .NetworkSettings.Networks}}' 2>/dev/null || true
fi

echo "[*] Remediation: keep databases on internal networks; block host publishes; disable ICC if east-west is not required."
