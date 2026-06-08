#!/usr/bin/env bash
# MODULE 2: Container Enumeration & Reconnaissance
# Run from attacker container

echo "============================================"
echo " DOCKER ENVIRONMENT ENUMERATION"
echo "============================================"

echo "[*] Hostname and identity..."
hostname && id && uname -a

echo "[*] Network interfaces and routes..."
ip addr show
ip route show

echo "[*] All hosts in /etc/hosts..."
cat /etc/hosts

echo "[*] Environment variables (looking for secrets)..."
env | grep -iE "key|pass|secret|token|api" || echo "None found"

echo "[*] Mounted filesystems..."
mount | grep -v "^cgroup\|^proc\|^sys\|^dev\|^tmpfs"

echo "[*] Running processes..."
ps aux 2>/dev/null || ps

echo "[*] Listening ports..."
netstat -tlnp 2>/dev/null || ss -tlnp

echo "[*] Checking for Docker socket..."
ls -la /var/run/docker.sock 2>/dev/null && echo "[!] Docker socket accessible — ESCAPE VECTOR" || echo "No socket found"

echo "[*] Checking capabilities..."
cat /proc/self/status | grep Cap
