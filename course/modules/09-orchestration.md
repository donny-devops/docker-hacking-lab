# Insecure Container Orchestration

Orchestrators multiply a single bad default: the default ServiceAccount, cluster-admin bindings, or an exposed API server.

## Attack scenario

A pod uses the default ServiceAccount with a mounted token. An app bug lets an attacker read in-cluster secrets.

## Noncompliant

```yaml
serviceAccountName: default
```

## Compliant

```yaml
serviceAccountName: app-sa
automountServiceAccountToken: false
```

## Remediation

- Dedicated ServiceAccount per workload; no token unless the API is required.
- Least-privilege RBAC; no cluster-admin for apps.
- Pod Security Admission / Gatekeeper / Kyverno to block privileged, hostPath, and hostPID.
- Scan manifests (Polaris, Kubesec).

## Hands-on lab

1. This Compose lab is not Kubernetes; map each Compose finding to a PSA equivalent (`privileged`, `hostPath`, `hostPorts`).
2. Write a restricted PodSecurity `restricted` policy checklist for the three insecure services.
3. Confirm `defender-hardened` already matches several restricted-profile controls.
4. Document why `internal-db` has no published host port.
