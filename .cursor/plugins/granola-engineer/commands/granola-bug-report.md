---
name: granola-bug-report
description: Turn a bug walkthrough call into a structured bug report.
---

# granola-bug-report

Someone just got off a call where a user or teammate walked them through a bug. The conversation is in Granola — now they need a structured write-up they can hand to the engineering team or drop into a ticket.

Ask which meeting, or use `query_granola_meetings` to find the most recent one that sounds like a bug walkthrough. Use `list_meetings` to scan recent meetings if the search needs narrowing. Once you have the meeting ID, use `get_meetings` for the summary and `get_meeting_transcript` for exact quotes.

From the conversation, extract:

- What the person reported happening, in their own words
- Steps to reproduce, pieced together from the walkthrough ("they clicked X, then Y, then it broke")
- Expected behaviour vs what actually happened
- Any environment details mentioned — browser, OS, account type, plan tier, specific page or feature
- Who reported it and when

Use direct quotes from the transcript for anything ambiguous or subjective — "it just spins forever after I click save" is more useful than a paraphrase.

If Granola has no matching meeting, say so and help structure a report from what the user describes. Do not invent a walkthrough. Follow `.github/ISSUE_TEMPLATE/bug_report.md` when filing against this repo.

The output should be structured enough to paste straight into Linear, GitHub Issues, or whatever the team uses. For docker-hacking-lab, keep reproduction steps defensive (compose, validate, detector) — no exploit payloads.
