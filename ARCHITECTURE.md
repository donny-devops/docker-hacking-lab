# Architecture

## Overview

docker-hacking-lab is a **container-based security learning environment**:

- Each scenario is a Docker Compose service with `lab.role` and `lab.module` labels.
- Networks: `lab-external` (published to localhost) and `lab-internal` (`internal: true`).
- CI validates the course catalog, Compose contracts, and script syntax without starting containers.

## Components

- **Lab orchestrator**
  - `docker-compose.yml` — insecure teaching baseline
  - `docker-compose.hardened.yml` — defensive solution topology
- **Course catalog**
  - `course/modules/01-privileged-containers.md` … `11-lsm.md`
  - `course/quizzes/` — 11 module quizzes + 11 finals
- **Detection / solutions**
  - `attacker-tools/` — read-only inspection helpers
  - `solutions/detect_misconfigurations.py` — Compose static analysis
- **CI/CD**
  - `.github/workflows/ci.yml`
  - Dependabot for GitHub Actions, `lab/Dockerfile`, and pip
- **Agents**
  - `.cursor/plugins/granola-engineer/` — Cursor plugin (granola-engineer)
  - Workspace copies under `.cursor/` so the lab loads rules, skills, and MCP without extra install

## Security design

- Host publishes bind to `127.0.0.1` only.
- Insecure services stay labeled (`lab.role: insecure`) and documented.
- Secrets in Compose are official/example placeholders, never production credentials.
- Default lab traffic for `lab-internal` has no external gateway.

## Data and secrets

- Local overrides: `.env` (gitignored). Template: `.env.example`.
- CI uses GitHub encrypted secrets if/when runtime credentials are added.
- Do not commit real cloud keys. `AKIAIOSFODNN7EXAMPLE` is Amazon's documentation placeholder.
