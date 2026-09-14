# Kernel Vulnerabilities

Containers share the host kernel. Image rebuilds do not patch kernel CVEs. Host (and runtime) patching is the control.

## Attack scenario

A public kernel CVE is exploitable from an unprivileged process, sometimes via user namespaces. Every container on that host is in scope.

## Noncompliant

```bash
uname -r   # leftover, unpatched kernel
```

## Compliant

Keep Engine, runc/containerd, and the host kernel on a documented SLA. Confirm:

```bash
runc --version
containerd --version
uname -r
```

## Remediation

- Patch host and runtime on an SLA; reboot or live-patch as required.
- Minimize host kernel modules.
- Evaluate gVisor/Kata when the threat model needs a different isolation boundary.
- Disable unprivileged user namespaces when they are not required.

## Hands-on lab

1. Record kernel and runtime versions on the lab host.
2. Map one historical container-escape CVE (for example CVE-2019-5736) to the layer it affected (runc, containerd, kernel).
3. Write a one-page patch response: detect, drain, patch, verify.
4. Explain why rebuilding `php:7.4-apache` does not fix a host kernel CVE.
