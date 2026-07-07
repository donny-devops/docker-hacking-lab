# Container Image Tampering
Covers supply-chain attacks, tag mutation, untrusted registries, and image signing.

## Attack scenario
Attacker pushes backdoored tag to public registry; CI auto-deploys it.

## Noncompliant
docker build -t app:latest .

## Compliant
cosign sign --key cosign.key app@sha256:...

## Remediation
- Pin images by digest.
- Sign images with cosign/Sigstore.
- Scan in CI with Trivy/Grype.

## Hands-on lab
1. Inspect image history/layers.
2. Re-pin by digest.
3. Verify provenance/signature.
