#!/usr/bin/env bash
# MODULE 10: Runtime defense comparison. Isolated lab only.
set -u

inspect_fields() {
  local name="$1"
  if ! command -v docker >/dev/null 2>&1; then
    echo "docker CLI not available"
    return
  fi
  docker inspect "$name" --format \
    'Privileged={{.HostConfig.Privileged}} CapAdd={{json .HostConfig.CapAdd}} CapDrop={{json .HostConfig.CapDrop}} ReadonlyRootfs={{.HostConfig.ReadonlyRootfs}} SecurityOpt={{json .HostConfig.SecurityOpt}} User={{.Config.User}}' \
    2>/dev/null || echo "(container ${name} not running)"
}

echo "[*] vuln-web security posture"
inspect_fields vuln-web

echo "[*] defender-hardened security posture"
inspect_fields defender-hardened

if command -v docker >/dev/null 2>&1; then
  echo "[*] User inside defender-hardened (inspect only; no writes)"
  docker exec defender-hardened id 2>&1 || true
fi

echo "[*] Compare with docker-compose.hardened.yml and solutions/detect_misconfigurations.py"
echo "[*] ReadonlyRootfs=true is the write-denial signal; this helper does not create files."
