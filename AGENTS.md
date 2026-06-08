# Agents and Automation

## Concept

This lab may use “agents” (scripts, bots, or AI tools) to:

- Generate scenarios
- Analyze configurations
- Suggest mitigations

## Guidelines

- Agents must **never** commit secrets.
- Agents should follow repository policies:
  - Branch protection
  - Code review
  - Security checks

## Example Uses

- Automated generation of Dockerfiles with secure defaults.
- CI bots that comment on insecure patterns in PRs.
