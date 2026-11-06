---
name: handoff
description: Use when asked for a handoff document, or a brief another agent or developer can implement from.
argument-hint: "<what to hand off> [output path]"
---

Write a handoff document that another agent or developer can implement from without the conversation. The reader has none of your context and may be working in a different repo, so state what they need and no more.

Write to `.scratch/handoff-<short-name>.md` if a path is not provided.
