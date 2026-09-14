# Skills and Learning Objectives

## Core Skills

- Understand Docker container isolation and its limits.
- Identify common misconfigurations in an isolated lab (privileged mode, socket mounts, host-root binds).
- Apply secure defaults and compare them with `docker-compose.hardened.yml`.

## Advanced Skills

- Analyze CI/CD pipelines for security weaknesses.
- Use GitHub security features:
  - Secret scanning
  - Code scanning
  - Dependabot
- Write Compose static checks (`solutions/detect_misconfigurations.py`).

## Recommended Path

1. Run `make test`, then the insecure Compose baseline.
2. Inspect labels and findings with `attacker-tools/` helpers.
3. Apply the hardened topology and re-run the detector.
4. Keep the `lab-validate` GitHub Actions check green.

Cursor agents: the granola-engineer plugin (rules, skills, `/granola-engineer`) is documented in `AGENTS.md` and `.cursor/plugins/granola-engineer/README.md`.
