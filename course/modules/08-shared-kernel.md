# Shared Kernel Exploitation
Covers namespace mistakes, /proc exposure, pid=host, and cross-container access.

## Attack scenario
Host PID namespace exposes other containers'/host process data.

## Noncompliant
docker run --pid=host --cap-add SYS_ADMIN alpine

## Compliant
docker run --user nonroot --pid container --cap-drop ALL alpine

## Remediation
- Avoid --pid=host.
- Use container-scoped PID namespaces.
- Enable dmesg_restrict.

## Hands-on lab
1. Run two containers.
2. Inspect /proc with/without host PID.
3. Harden namespace usage.
