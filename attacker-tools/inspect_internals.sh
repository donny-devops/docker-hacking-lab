#!/usr/bin/env bash
# MODULE 1: Kernel primitive inspection (read-only). Isolated lab only.
set -u

echo "============================================"
echo " LINUX KERNEL PRIMITIVES — CONTAINER VIEW"
echo "============================================"

echo "[*] Namespaces"
ls -la /proc/self/ns/ 2>/dev/null || true
if command -v lsns >/dev/null 2>&1; then
  lsns -p $$ 2>/dev/null || lsns 2>/dev/null || true
fi

echo "[*] Capability masks"
grep -E '^Cap' /proc/self/status 2>/dev/null || true

echo "[*] capsh decode (if installed)"
if command -v capsh >/dev/null 2>&1; then
  capsh --print 2>/dev/null || true
fi

echo "[*] Cgroup membership"
cat /proc/self/cgroup 2>/dev/null || true

echo "[*] Seccomp"
grep -i Seccomp /proc/self/status 2>/dev/null || true

echo "[*] AppArmor/SELinux current context"
if [[ -r /proc/self/attr/current ]]; then
  cat /proc/self/attr/current
else
  echo "No /proc/self/attr/current"
fi
