# Insecure Container Orchestration
Covers K8s/Compose misconfigs, default SAs, broad RBAC, and exposed APIs.

## Attack scenario
Default SA has secret-read; app bug leaks cluster secrets.

## Noncompliant
serviceAccountName: default

## Compliant
serviceAccountName: app-sa
automountServiceAccountToken: false

## Remediation
- Dedicated SA per workload.
- Least-privilege RBAC.
- Scan configs with Polaris/Kubesec.

## Hands-on lab
1. Inspect current SA/roles.
2. Create restricted SA.
3. Update deployment and confirm denial.
