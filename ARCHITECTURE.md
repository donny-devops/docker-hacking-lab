# Architecture

## Overview

docker-hacking-lab is a **container‑based security learning environment**:

- Each scenario is a set of Docker services.
- Scenarios are isolated via networks and volumes.
- CI/CD and security tooling are demonstrated via GitHub workflows.

## Components

- **Lab Orchestrator**
  - `docker-compose.yml` files per scenario
  - Shared base images where appropriate

- **Scenarios**
  - Misconfigurations (privileged containers, weak isolation)
  - Network segmentation and firewall rules
  - Secrets handling and leakage examples

- **CI/CD**
  - GitHub Actions workflows in `.github/workflows/`
  - Optional self‑hosted runners for advanced users

## Security Design

- Default lab runs on a private network.
- No external exposure unless explicitly configured.
- Scenarios include:
  - “Secure” baseline
  - “Insecure” variant for learning

## Data and Secrets

- Secrets are stored in:
  - `.env` files (ignored by Git)
  - GitHub encrypted secrets for CI
- No real production credentials should ever be used.
