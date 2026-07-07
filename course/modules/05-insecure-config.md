# Insecure Container Configuration
Covers excessive permissions, writable rootfs, dangerous sysctls, and insecure defaults.

## Attack scenario
Root-owned writable rootfs enables cron/kmodule persistence.

## Noncompliant
docker run --cap-add SYS_ADMIN --read-only=false ubuntu

## Compliant
docker run --user 65532:65532 --read-only --tmpfs /tmp ubuntu

## Remediation
- Run as nonroot.
- Use --read-only with tmpfs.
- Drop capabilities by default.

## Hands-on lab
1. Inspect docker inspect config.
2. Harden runtime flags.
3. Verify no root writable paths.
