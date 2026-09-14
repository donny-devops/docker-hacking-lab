# Instructor solutions (defensive)

These files show how to **detect and remove** the teaching misconfigurations. They do not include exploit payloads.

| File | Purpose |
|------|---------|
| `../docker-compose.hardened.yml` | Standalone topology: privileged mode, host-root mounts, and Docker socket mounts removed. Registry is unpublished on the host but still unauthenticated on `lab-internal`. |
| `detect_misconfigurations.py` | Static analyzer for Compose files |
| `seccomp-restricted.json` | Example allow-list profile for a small userspace workload |

```bash
python3 solutions/detect_misconfigurations.py docker-compose.yml --expect-findings
python3 solutions/detect_misconfigurations.py docker-compose.hardened.yml
```

The insecure baseline is expected to report privileged mode, a Docker socket mount, and a host-root mount. The hardened file should report none of those.

Do not merge the two Compose files. Compose list/scalar merge would keep the insecure privileged, socket, and host-root keys.
