# What Seccomp, AppArmor, and SELinux Actually Do
Covers LSM roles, Docker defaults, custom profiles, and operational pitfalls.

## Seccomp
Restricts syscalls. Docker default blocks ~44 dangerous syscalls.

## AppArmor
Path-based confinement. Uses docker-default on Debian/Ubuntu.

## SELinux
Label-based MAC. Stronger; enabled on RHEL/Fedora.

## Noncompliant
docker run --security-opt seccomp=unconfined ubuntu

## Compliant
docker run --security-opt seccomp=default --security-opt apparmor=docker-default ubuntu

## Remediation
- Keep defaults unless app breaks.
- Trace syscalls before narrowing.
- Combine seccomp + AppArmor/SELinux + capabilities.

## Hands-on lab
1. Inspect container security opts.
2. strace app process.
3. Build minimal custom seccomp JSON and test.
