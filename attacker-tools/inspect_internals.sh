#!/usr/bin/env bash
# MODULE 1: Docker Internals — Kernel Primitive Inspection
# Run from any container to understand isolation boundaries

echo "============================================"
echo " LINUX KERNEL PRIMITIVES — CONTAINER VIEW"
echo "============================================"

echo "[*] Namespaces this container is in..."
ls -la /proc/self/ns/
lsns -p UTF8 2>/dev/null

echo "[*] Linux capabilities (raw hex)..."
cat /proc/self/status | grep -E "^Cap"

echo "[*] Decoded capabilities..."
capsh --decode= 2>/dev/null

echo "[*] Cgroup memberships..."
cat /proc/self/cgroup

echo "[*] Seccomp status..."
cat /proc/self/status | grep Seccomp

echo "[*] AppArmor profile..."
cat /proc/self/attr/current 2>/dev/null || echo "AppArmor not enforced"
