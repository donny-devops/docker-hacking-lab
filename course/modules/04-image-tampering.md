# Container Image Tampering

Tags move. `app:latest` from an untrusted registry can be replaced. CI that deploys by tag will run whatever the tag points at.

## Attack scenario

A typosquat name (`ngiinx`) or a mutated tag is pushed to a registry the pipeline already trusts. The next deploy pulls the new manifest.

## Noncompliant

```bash
docker build -t app:latest .
docker push registry.example/app:latest
```

## Compliant

```bash
docker build -t app:1.0 .
docker push registry.example/app:1.0
DIGEST="$(docker image inspect registry.example/app:1.0 --format '{{index .RepoDigests 0}}')"
cosign sign --key cosign.key "$DIGEST"
```

Pin by digest in Compose/Kubernetes (`image: registry.example/app@sha256:...`). Verify signatures in CI before deploy.

## Remediation

- Pin images by digest, not floating tags.
- Sign with Sigstore/cosign and verify in the pipeline.
- Scan with Trivy/Grype and fail the build on relevant CVEs.
- Allow only an internal registry.

## Hands-on lab

1. Note that the lab registry has no authentication in the insecure baseline.
2. Inspect image names used in compose (no digest pins).
3. In the hardened file, confirm the registry is no longer published to the host. Peers on `lab-internal` can still reach it without auth.
4. Document a digest-pin policy for one service.
