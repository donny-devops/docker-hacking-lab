# Insecure Container Images
Covers outdated bases, malware images, vulnerable packages, and registry hygiene.

## Attack scenario
Malicious image appears as trusted name; CI builds and deploys it.

## Noncompliant
docker build -t app:latest .

## Compliant
trivy image app@sha256:...

## Remediation
- Pin by digest/provenance.
- Scan in CI and deploy gate.
- Trust only approved registries.

## Hands-on lab
1. Build latest-tagged image.
2. Inspect layers/history.
3. Rebuild pinned and scan.
