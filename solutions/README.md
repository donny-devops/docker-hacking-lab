# Instructor solutions (defensive)

These files show how to **detect and remove** the teaching misconfigurations. They do not include exploit payloads.

| File | Purpose |
|------|---------|
| `../docker-compose.hardened.yml` | Same topology with privileged mode, host-root mounts, Docker socket mounts, and published registry removed |
| `detect_misconfigurations.py` | Static analyzer for Compose files |
| `seccomp-restricted.json` | Example allow-list profile for a small userspace workload |

```bash
python3 solutions/detect_misconfigurations.py docker-compose.yml --expect-findings
python3 solutions/detect_misconfigurations.py docker-compose.hardened.yml
```

The insecure baseline is expected to report privileged mode, a Docker socket mount, and a host-root mount. The hardened file should report none of those.
