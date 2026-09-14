# Insecure Container Images

Outdated bases, unpinned tags, and look-alike names are supply-chain failures. The runtime never sees the difference.

## Attack scenario

CI builds `app:latest` from a public base that has not been scanned. A typosquat or stale package set ships to production.

## Noncompliant

```bash
docker build -t app:latest .
```

## Compliant

```bash
trivy image --exit-code 1 app@sha256:...
```

Use distroless/minimal bases, pin by digest, and fail the pipeline on severity thresholds.

## Remediation

- Pin by digest and provenance.
- Scan in CI and at deploy time.
- Trust only an allow-listed registry.
- Drop build tools from runtime images.

## Hands-on lab

1. List every image reference in `docker-compose.yml`.
2. Identify EOL or rolling tags (`php:7.4-apache`, `kalilinux/kali-rolling`).
3. Propose a pinned digest strategy for `postgres:13-alpine` and `registry:2`.
4. Keep the insecure baseline as a teaching target; do not "fix" it by deleting the findings.
