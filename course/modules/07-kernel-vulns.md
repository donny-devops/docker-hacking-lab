# Kernel Vulnerabilities
Covers host/runtime CVEs, patching cadence, and isolation limitations.

## Attack scenario
Unpatched kernel enables container-to-host privilege escalation.

## Noncompliant
uname -r  # old unpatched kernel

## Compliant
sudo apt install linux-generic-hwe-22.04

## Remediation
- Patch host/runtime on SLA.
- Minimize host kernel modules.
- Evaluate gVisor/Kata for stronger isolation.

## Hands-on lab
1. Check kernel against CVE advisories.
2. Review runtime changelog.
3. Document upgrade plan.
