---
name: add-multiformat-course-document
description: Workflow command scaffold for add-multiformat-course-document in docker-hacking-lab.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /add-multiformat-course-document

Use this workflow when working on **add-multiformat-course-document** in `docker-hacking-lab`.

## Goal

Adds or updates course-wide documents (outline, summary, metadata template) in multiple formats (md, docx, pdf, html).

## Common Files

- `container-security-course/course_outline.md`
- `container-security-course/course_outline.docx`
- `container-security-course/course_outline.pdf`
- `container-security-course/course_summary.html`
- `container-security-course/course_summary.pdf`
- `container-security-course/metadata_template.md`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Create or update the document in Markdown (.md).
- Convert or export the document to DOCX (.docx).
- Convert or export the document to PDF (.pdf).
- For summaries, optionally add HTML (.html) format.

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.