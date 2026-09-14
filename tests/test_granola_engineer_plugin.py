"""Checks that the in-repo granola-engineer plugin is present and has no secrets."""
from __future__ import annotations

import json

from conftest import ROOT

PLUGIN = ROOT / ".cursor" / "plugins" / "granola-engineer"
WORKSPACE_CURSOR = ROOT / ".cursor"

SECRET_NEEDLES = (
    "GRANOLA_API_KEY",
    "GRANOLA_TOKEN",
    "sk-ant-",
    "sk-proj-",
    "xoxb-",
    "xoxp-",
    "BEGIN PRIVATE KEY",
    "AKIA",
)

MIRRORED_FILES = (
    ("mcp.json", "mcp.json"),
    ("agents/granola-engineer.md", "agents/granola-engineer.md"),
    ("rules/check-meeting-context.mdc", "rules/check-meeting-context.mdc"),
    ("skills/granola-engineer/SKILL.md", "skills/granola-engineer/SKILL.md"),
    ("skills/granola-context/SKILL.md", "skills/granola-context/SKILL.md"),
    ("skills/granola-prep/SKILL.md", "skills/granola-prep/SKILL.md"),
    ("skills/granola-review/SKILL.md", "skills/granola-review/SKILL.md"),
    ("commands/granola-pr.md", "commands/granola-pr.md"),
    ("commands/granola-plan.md", "commands/granola-plan.md"),
    ("commands/granola-spec.md", "commands/granola-spec.md"),
    ("commands/granola-brief.md", "commands/granola-brief.md"),
    ("commands/granola-bug-report.md", "commands/granola-bug-report.md"),
    ("commands/granola-gaps.md", "commands/granola-gaps.md"),
)


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_plugin_manifest_names_granola_engineer():
    manifest = json.loads(_read(PLUGIN / ".cursor-plugin" / "plugin.json"))
    assert manifest["name"] == "granola-engineer"
    assert "agents" in manifest
    assert "skills" in manifest
    assert "rules" in manifest
    mcp = json.loads(_read(PLUGIN / "mcp.json"))
    granola = mcp["mcpServers"]["granola"]
    assert granola["url"] == "https://mcp.granola.ai/mcp"
    assert "headers" not in granola
    assert "env" not in granola
    assert "apiKey" not in granola
    assert "Authorization" not in json.dumps(granola)


def test_plugin_ships_agent_skills_and_commands():
    assert (PLUGIN / "agents" / "granola-engineer.md").is_file()
    for skill in ("granola-engineer", "granola-context", "granola-prep", "granola-review"):
        assert (PLUGIN / "skills" / skill / "SKILL.md").is_file(), skill
    for command in (
        "granola-pr",
        "granola-plan",
        "granola-spec",
        "granola-brief",
        "granola-bug-report",
        "granola-gaps",
    ):
        assert (PLUGIN / "commands" / f"{command}.md").is_file(), command
    assert (PLUGIN / "rules" / "check-meeting-context.mdc").is_file()
    readme = _read(PLUGIN / "README.md")
    assert "Enable / use" in readme
    assert "~/.cursor/plugins/local" in readme


def test_granola_engineer_is_defensive_and_does_not_invent_meetings():
    agent = _read(PLUGIN / "agents" / "granola-engineer.md").lower()
    assert "query_granola_meetings" in agent
    assert "do not invent meeting" in agent
    assert "never write exploits" in agent
    assert "never commit secrets" in agent
    assert "docker-hacking-lab" in agent


def test_plugin_files_contain_no_secrets():
    for path in PLUGIN.rglob("*"):
        if not path.is_file() or path.suffix in {".svg", ".png"}:
            continue
        text = path.read_text(encoding="utf-8")
        lowered = text.lower()
        for needle in SECRET_NEEDLES:
            assert needle.lower() not in lowered, f"{path} contains {needle}"


def test_workspace_cursor_paths_mirror_plugin():
    for plugin_rel, workspace_rel in MIRRORED_FILES:
        plugin_text = _read(PLUGIN / plugin_rel)
        workspace_text = _read(WORKSPACE_CURSOR / workspace_rel)
        assert plugin_text == workspace_text, workspace_rel
