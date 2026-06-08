# Contributing to docker-hacking-lab

Thanks for wanting to improve this lab. Let’s keep it safe, clear, and fun.

## Code of Conduct

By participating, you agree to follow the guidelines in `CODE_OF_CONDUCT.md`.

## How to Contribute

**1. Fork and branch**

- Fork the repo.
- Create a feature branch:
  - `feat/<short-description>`
  - `fix/<short-description>`
  - `docs/<short-description>`

**2. Development**

- Keep scenarios self‑contained and clearly documented.
- Add or update tests where applicable.
- Ensure `docker-compose` files are minimal and reproducible.

**3. Commit style**

- Use Conventional Commits:
  - `feat: add privilege escalation scenario`
  - `fix: correct network isolation`
  - `docs: explain lab topology`

**4. Pull requests**

- Target the `main` branch.
- Include:
  - Description of the scenario or fix
  - Security considerations
  - How to run and clean up

## Environment Requirements

- Recent Docker Engine and Docker Compose
- Linux or macOS recommended; Windows WSL2 supported
- No production secrets in your environment or commits

## Security Contributions

If your change touches security:

- Explain the threat model.
- Document risks and mitigations.
- Avoid shipping exploitable defaults without clear warnings.

## Self‑Hosted Runners (CI)

If you propose using self‑hosted runners:

- Never run untrusted code on shared runners.
- Restrict runners to private networks.
- Use locked‑down IAM and network policies.
