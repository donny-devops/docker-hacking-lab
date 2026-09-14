# granola-engineer (docker-hacking-lab)

In-repo Cursor plugin that grounds agent work in Granola meeting decisions. Adapted from the official Granola Cursor plugin for this educational Docker lab.

This plugin does **not** store API keys. Granola authenticates in the browser on first MCP use.

## What is included

| Kind | Name | Role |
|------|------|------|
| Agent | `/granola-engineer` | Anchor implementation to meeting decisions |
| Skill | `granola-engineer` | When to use the agent |
| Skill | `granola-context` | Look up a past decision |
| Skill | `granola-prep` | Prep for an upcoming call |
| Skill | `granola-review` | Diff work vs meeting decisions |
| Rule | `check-meeting-context` | Always-on nudge to query Granola |
| Commands | `/granola-plan`, `/granola-spec`, `/granola-brief`, `/granola-bug-report`, `/granola-pr`, `/granola-gaps` | Manual document workflows |
| MCP | `granola` | `https://mcp.granola.ai/mcp` (no secrets in git) |

## Enable / use

**This repo (recommended).** Open `docker-hacking-lab` in Cursor. Workspace copies under `.cursor/agents/`, `.cursor/rules/`, `.cursor/skills/`, `.cursor/commands/`, and `.cursor/mcp.json` load automatically. Ask the agent to work as granola-engineer, or invoke `/granola-engineer`.

**Local plugin install (optional).** Copy this directory to Cursor's local plugin folder and reload:

```bash
mkdir -p ~/.cursor/plugins/local
cp -R .cursor/plugins/granola-engineer ~/.cursor/plugins/local/granola-engineer
```

Then run **Developer: Reload Window**. First Granola tool call prompts browser sign-in. You need a [Granola](https://granola.ai) account. Empty results are expected when the connected plan has no in-scope notes — do not invent meetings.

**Marketplace.** You can also install [Granola](https://cursor.com/marketplace/granola) from the Cursor Marketplace. This in-repo copy adds lab guardrails (no exploits, no secrets) and does not require the marketplace plugin.

## Lab constraints

- Isolated educational lab only. Never write exploits or PoCs.
- Never commit Granola tokens, cloud keys, or `.env` files.
- If meetings defer work to Slack or other tools, say so and offer to check them.
- Keep `make test` / `lab/validate.sh` green when changing CI or tests.

## Layout

```
.cursor/plugins/granola-engineer/
  .cursor-plugin/plugin.json
  mcp.json
  agents/granola-engineer.md
  rules/check-meeting-context.mdc
  skills/granola-engineer/SKILL.md
  skills/granola-context/SKILL.md
  skills/granola-prep/SKILL.md
  skills/granola-review/SKILL.md
  commands/*.md
```

Workspace discovery paths (kept in sync by `tests/test_granola_engineer_plugin.py`) live under `.cursor/agents`, `.cursor/rules`, `.cursor/skills`, `.cursor/commands`, and `.cursor/mcp.json`.
