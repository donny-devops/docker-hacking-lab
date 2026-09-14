from pathlib import Path

import pytest

from conftest import (
    COURSE_MODULES,
    COURSE_QUIZZES,
    EXPECTED_MODULES,
    EXPECTED_QUIZ_STEMS,
    MODULE_SECTIONS,
)


@pytest.mark.catalog
def test_eleven_modules_exist():
    names = sorted(p.name for p in COURSE_MODULES.glob("*.md"))
    assert names == list(EXPECTED_MODULES)


@pytest.mark.catalog
def test_privileged_container_module_is_first():
    first = COURSE_MODULES / "01-privileged-containers.md"
    assert first.is_file()
    text = first.read_text(encoding="utf-8")
    assert "Privileged" in text
    assert "--privileged" in text


@pytest.mark.catalog
def test_module_sections_present():
    for name in EXPECTED_MODULES:
        text = (COURSE_MODULES / name).read_text(encoding="utf-8")
        for section in MODULE_SECTIONS:
            assert section in text, f"{name} missing {section}"


@pytest.mark.catalog
def test_twenty_two_assessments_exist():
    expected = []
    for stem in EXPECTED_QUIZ_STEMS:
        expected.extend([f"{stem}.md", f"{stem}-final.md"])
    names = sorted(p.name for p in COURSE_QUIZZES.glob("*.md"))
    assert names == sorted(expected)
    assert len(names) == 22


@pytest.mark.catalog
def test_quizzes_are_unique():
    bodies = {}
    for path in sorted(COURSE_QUIZZES.glob("*.md")):
        bodies[path.name] = path.read_text(encoding="utf-8").strip()
    inverse: dict[str, list[str]] = {}
    for name, body in bodies.items():
        inverse.setdefault(body, []).append(name)
    dupes = {k: v for k, v in inverse.items() if len(v) > 1}
    assert not dupes, f"duplicate quiz bodies: {dupes}"


@pytest.mark.catalog
def test_course_summary_lists_privileged_module():
    summary = Path(__file__).resolve().parents[1] / "COURSE_SUMMARY.md"
    text = summary.read_text(encoding="utf-8")
    assert "01 - Privileged Containers" in text
    assert "course/modules/" in text
