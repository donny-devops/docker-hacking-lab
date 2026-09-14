---
name: granola-pr
description: Write a PR description grounded in meeting decisions and discussions.
---

# granola-pr

Someone is ready to open a pull request and wants the description to reflect not just what changed, but why — traced back to the meetings where the work was discussed.

Look at the current branch: the diff against the base branch, the commit history, and what files were touched. From that, identify the feature or topic being worked on.

Use `query_granola_meetings` to find meetings where this work was discussed. Use `get_meetings` to pull detailed content — decisions, requirements, constraints that were agreed on. If the branch name or commits reference a specific project or feature, search for that directly.

Write a PR description that includes:

- A summary of what the PR does, grounded in what was discussed ("implements the caching approach agreed in the March 15 planning session")
- Which meetings informed the work, with titles and dates
- Any decisions from meetings that this PR implements
- Anything the PR does that wasn't explicitly discussed — not as a problem, just flagged for reviewers ("the meeting didn't cover error handling for this case, so I went with X")

If Granola returns no meetings, say that in the description rather than inventing citations. Fall back to repository docs and the PR template in `.github/PULL_REQUEST_TEMPLATE.md`.

The tone should be a normal PR description, not a meeting report. Follow docker-hacking-lab rules: no exploits or PoCs, no secrets, keep `lab-validate` green.
