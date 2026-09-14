# What Seccomp, AppArmor, and SELinux Actually Do

Linux security modules filter syscalls (seccomp) or enforce MAC on paths/labels (AppArmor, SELinux). They complement capabilities; they do not replace patching.

## Attack scenario

An operator launches a workload with `seccomp=unconfined` (or `--privileged`) so a one-off binary can call unusual syscalls. The extra kernel attack surface stays on for the rest of the container's life.

## Seccomp

Restricts syscalls. Docker's default profile blocks a set of dangerous calls. `--security-opt seccomp=unconfined` turns that off.

## AppArmor

Path-based confinement on Debian/Ubuntu. Docker applies `docker-default` unless disabled.

## SELinux

Label-based MAC, common on RHEL/Fedora. Stronger default labeling for volume mounts.

## Noncompliant

```bash
docker run --security-opt seccomp=unconfined ubuntu
```

`--privileged` also disables seccomp and MAC.

## Compliant

```bash
docker run --security-opt seccomp=default --security-opt apparmor=docker-default ubuntu
```

A tighter starting point is `solutions/seccomp-restricted.json` after tracing the app.

## Remediation

- Keep runtime defaults unless a traced syscall list proves a need.
- Combine seccomp + AppArmor/SELinux + dropped capabilities + non-root.
- Use `SCMP_ACT_LOG` only in a lab to discover syscalls, not in production as the only action.

## Hands-on lab

1. Read `Seccomp:` from `/proc/self/status` via `inspect_internals.sh`.
2. Compare that output conceptually with `defender-hardened` (`no-new-privileges`).
3. Review `solutions/seccomp-restricted.json` and note it is an allow-list.
4. Do not deploy an untested custom profile onto the teaching services.
