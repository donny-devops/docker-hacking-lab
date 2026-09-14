#!/usr/bin/env bash
# MODULE 2: Container enumeration (read-only). Isolated lab only.
set -u

echo "============================================"
echo " DOCKER ENVIRONMENT ENUMERATION (DETECT)"
echo "============================================"

echo "[*] Hostname and identity"
hostname 2>/dev/null || true
id 2>/dev/null || true
uname -a 2>/dev/null || true

echo "[*] Network interfaces and routes"
if command -v ip >/dev/null 2>&1; then
  ip addr show
  ip route show
else
  echo "iproute2 not installed"
fi

echo "[*] /etc/hosts"
cat /etc/hosts 2>/dev/null || true

echo "[*] Environment keys that look like secrets (names only)"
env | awk -F= 'BEGIN{IGNORECASE=1} $1 ~ /key|pass|secret|token|api/ {print $1}' || true

echo "[*] Mounted filesystems"
mount 2>/dev/null | grep -vE '^cgroup|^proc|^sys|^dev|^tmpfs' || true

echo "[*] Listening sockets"
if command -v ss >/dev/null 2>&1; then
  ss -tlnp 2>/dev/null || ss -tln
elif command -v netstat >/dev/null 2>&1; then
  netstat -tln 2>/dev/null || true
fi

echo "[*] Docker socket present?"
if [[ -S /var/run/docker.sock ]]; then
  echo "[!] FINDING: docker.sock is available in this namespace"
else
  echo "No docker.sock in this namespace"
fi

echo "[*] Capability bits"
grep -E '^Cap' /proc/self/status 2>/dev/null || true
