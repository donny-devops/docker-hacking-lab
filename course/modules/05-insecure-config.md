# Insecure Container Configuration

Writable root filesystems, extra capabilities, and root users turn a simple RCE into persistence (cron, binaries, modules).

## Attack scenario

A container runs as root with `CAP_SYS_ADMIN` and a writable rootfs. A compromised process can change its own mounts and drop files that survive restarts if volumes persist.

## Noncompliant

```bash
docker run --cap-add SYS_ADMIN --read-only=false ubuntu
```

## Compliant

```bash
docker run --user 65532:65532 --read-only --tmpfs /tmp --cap-drop ALL ubuntu
```

## Remediation

- Run as a non-root user.
- `--read-only` plus tmpfs for required scratch paths.
- Drop all capabilities, then add back only what the app needs.
- `no-new-privileges:true`.

## Hands-on lab

1. `docker inspect` `defender-hardened` and list ReadonlyRootfs, CapDrop, User, SecurityOpt.
2. Contrast with `escape-target-privileged` on the insecure baseline.
3. Confirm the hardened compose file applies `cap_drop: [ALL]` to former escape targets.
4. Attempt a write to `/` inside `defender-hardened` and record the denial.
