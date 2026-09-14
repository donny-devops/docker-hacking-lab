# Agents and Automation

## Concept

This lab may use “agents” (scripts, bots, or AI tools) to:

- Generate scenarios
- Analyze configurations
- Suggest mitigations
- Ground implementation in Granola meeting decisions (`granola-engineer`)

## Guidelines

- Agents must **never** commit secrets.
- Agents should follow repository policies:
  - Branch protection
  - Code review
  - Security checks
- Do not invent Granola meeting notes. If MCP returns no meetings, say so and use this file plus `CLAUDE.md`, `CONTRIBUTING.md`, and `SECURITY.md`.
- Never write exploits or PoCs. Detection helpers belong in `attacker-tools/` and `solutions/`.

## granola-engineer

In-repo Cursor plugin for decisions-aware work. Canonical files live in `.cursor/plugins/granola-engineer/`; workspace copies under `.cursor/agents`, `.cursor/rules`, `.cursor/skills`, `.cursor/commands`, and `.cursor/mcp.json` load when you open this repo.

**Enable**

1. Open this repository in Cursor.
2. First Granola MCP call signs in via the browser (no API keys in git).
3. Invoke `/granola-engineer`, or ask the agent to check Granola before implementing.

Optional local install: copy `.cursor/plugins/granola-engineer` to `~/.cursor/plugins/local/granola-engineer` and reload the window. See `.cursor/plugins/granola-engineer/README.md`.

**Use**

- `/granola-engineer` — implement against meeting decisions
- granola-context / granola-prep / granola-review skills — lookup, prep, and pre-submit review
- `/granola-pr` — PR text traced to meetings (or an explicit “no meetings in scope” note)

## Example Uses

- Automated generation of Dockerfiles with secure defaults.
- CI bots that comment on insecure patterns in PRs.
- Meeting-grounded lab docs and hardening changes (when Granola notes exist).
