# Security Policy

## Supported Versions

This project is experimental and **not** intended for production use.  
Security fixes are applied on a best‑effort basis to the `main` branch.

## Reporting a Vulnerability

If you discover a vulnerability:

- **Do not** open a public issue with exploit details.
- Email: donnydevops@outlook.com
- Include:
  - Steps to reproduce
  - Impact assessment
  - Suggested remediation (if any)

We aim to acknowledge reports within 72 hours and provide an initial assessment within 7 days.

## Scope

This repository is a **local lab** for learning:

- Container isolation and escape techniques
- Network segmentation and misconfiguration
- Secure CI/CD and supply‑chain practices

It must **never** be deployed to the public internet without additional hardening.

## Security Baselines

- Use the latest stable Docker and Compose.
- Run lab containers on an isolated network (e.g., `docker-hacking-lab` bridge).
- Disable privileged containers unless explicitly required for a scenario.
- Use read‑only root filesystems where possible.
- Use non‑root users inside containers whenever feasible.

## Advanced Security Measures

- Enable GitHub:
  - Dependabot alerts and security updates
  - Secret scanning and push protection
  - Code scanning (CodeQL or equivalent)
- Use signed commits and tags for releases.
- Require branch protection and code review for `main`.
- Store secrets only in:
  - GitHub Actions encrypted secrets
  - Local `.env` files excluded via `.gitignore`
  - External secret managers (e.g., HashiCorp Vault)

## Responsible Use

This lab is for **education and defense**:

- Do not use techniques from this repository against systems you do not own or have explicit permission to test.
- Follow all applicable laws and organizational policies.
