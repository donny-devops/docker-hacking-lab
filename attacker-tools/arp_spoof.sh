#!/usr/bin/env bash
# MODULE 9: Network isolation check. Isolated lab only.
# Does not perform spoofing or packet injection.
set -u

echo "[*] Interface and forwarding state"
if command -v ip >/dev/null 2>&1; then
  ip -br addr
  ip route
fi
if [[ -r /proc/sys/net/ipv4/ip_forward ]]; then
  echo "ip_forward=$(cat /proc/sys/net/ipv4/ip_forward)"
fi

echo "[*] Reachability of documented lab nets (ICMP only, one ping each)"
for host in 172.20.0.1 172.22.0.1; do
  if ping -c1 -W1 "$host" >/dev/null 2>&1; then
    echo "[+] ${host} responded"
  else
    echo "[*] ${host} did not respond (may be expected)"
  fi
done

echo "[*] Remediation: keep lab-internal internal=true; do not bridge attacker tools into production VLANs."
