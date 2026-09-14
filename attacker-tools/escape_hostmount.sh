#!/usr/bin/env bash
# MODULE 4: Detect host-root bind mounts. Isolated lab only.
# Does not read host credential files or chroot.
set -u

HOST_ROOT="${HOST_MOUNT:-/host}"

echo "[*] Looking for a host-root mount at ${HOST_ROOT}"
if [[ -d "$HOST_ROOT/etc" && -d "$HOST_ROOT/proc" ]]; then
  echo "[!] FINDING: ${HOST_ROOT} looks like a host root filesystem mount."
  echo "[*] Directory names only:"
  ls "$HOST_ROOT" | head
  echo "[*] Remediation: remove the /:/host bind; mount a specific path read-only."
else
  echo "No host-root mount detected at ${HOST_ROOT}"
fi

if command -v docker >/dev/null 2>&1; then
  docker inspect escape-target-hostmount --format '{{json .Mounts}}' 2>/dev/null || true
fi
