#!/usr/bin/env bash
# MODULE 10: Runtime Defense Verification
# Compare vuln-web vs defender-hardened

echo "[*] vuln-web security posture:"
docker inspect vuln-web | grep -E "Privileged|CapAdd|CapDrop|ReadonlyRootfs|SecurityOpt"

echo "[*] defender-hardened security posture:"
docker inspect defender-hardened | grep -E "Privileged|CapAdd|CapDrop|ReadonlyRootfs|SecurityOpt"

echo "[*] Testing read-only filesystem on defender-hardened..."
docker exec defender-hardened touch /test 2>&1

echo "[*] Checking non-root user..."
docker exec defender-hardened id 2>&1
