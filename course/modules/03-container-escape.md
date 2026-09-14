# Container Escape

Escape is usually a **misconfiguration chain**, not a novel exploit: privileged mode, host-path mounts, host PID/network namespaces, or Docker socket access.

## Attack scenario

A helper container receives `/var/run/docker.sock`. From there an operator (or later an attacker) can create a sibling container with host mounts. The original container did not need `--privileged`.

## Noncompliant

```bash
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock alpine
```

## Compliant

```bash
docker run --rm --user 1000:1000 --read-only --cap-drop ALL \
  --security-opt no-new-privileges:true alpine
```

## Remediation

- Drop capabilities; never set `--privileged` for app workloads.
- Avoid `--pid=host`, `--network=host`, and `/` host binds.
- Keep user namespaces and default seccomp/AppArmor.
- Use rootless Engine where possible.

## Hands-on lab

1. Compare labels `lab.finding` on insecure services.
2. Inspect `vuln-web`, `escape-target-privileged`, and `escape-target-hostmount`.
3. Apply the hardened compose file and re-inspect those three services.
4. Record which control closed each finding (socket, privileged, host mount).
