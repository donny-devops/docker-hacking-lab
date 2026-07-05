---
name: add-new-course-module
description: Workflow command scaffold for add-new-course-module in docker-hacking-lab.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /add-new-course-module

Use this workflow when working on **add-new-course-module** in `docker-hacking-lab`.

## Goal

Adds a new module to the container security course, including scripts, questions, metadata, and summary, in multiple formats.

## Common Files

- `container-security-course/module_XX_*/video_YY_script.md`
- `container-security-course/module_XX_*/video_YY_script.docx`
- `container-security-course/module_XX_*/video_YY_script.pdf`
- `container-security-course/module_XX_*/module_summary_script.md`
- `container-security-course/module_XX_*/module_summary_script.docx`
- `container-security-course/module_XX_*/module_summary_script.pdf`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Create a new module directory under container-security-course/ with a descriptive name (e.g., module_01_fundamentals).
- Add video scripts for each topic in the module in .md, .docx, and .pdf formats.
- Add a module summary script in .md, .docx, and .pdf formats.
- Add questions for the module in .md, .docx, and .pdf formats.
- Add metadata for the module in .md, .docx, and .pdf formats.

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.