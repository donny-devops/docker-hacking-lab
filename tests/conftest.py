#!/usr/bin/env python3
"""Shared paths and compose loaders for lab tests."""
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
COMPOSE_INSECURE = ROOT / "docker-compose.yml"
COMPOSE_HARDENED = ROOT / "docker-compose.hardened.yml"
COURSE_MODULES = ROOT / "course" / "modules"
COURSE_QUIZZES = ROOT / "course" / "quizzes"
ATTACKER_TOOLS = ROOT / "attacker-tools"
SOLUTIONS = ROOT / "solutions"

EXPECTED_MODULES = (
    "01-privileged-containers.md",
    "02-exposed-apis.md",
    "03-container-escape.md",
    "04-image-tampering.md",
    "05-insecure-config.md",
    "06-dos.md",
    "07-kernel-vulns.md",
    "08-shared-kernel.md",
    "09-orchestration.md",
    "10-insecure-images.md",
    "11-lsm.md",
)

EXPECTED_QUIZ_STEMS = (
    "privileged-containers",
    "exposed-apis",
    "container-escape",
    "image-tampering",
    "insecure-config",
    "dos",
    "kernel-vulns",
    "shared-kernel",
    "orchestration",
    "insecure-images",
    "lsm",
)

MODULE_SECTIONS = (
    "## Attack scenario",
    "## Noncompliant",
    "## Compliant",
    "## Remediation",
    "## Hands-on lab",
)


def load_yaml(path: Path) -> dict:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert isinstance(data, dict), f"{path} must parse to a mapping"
    return data
