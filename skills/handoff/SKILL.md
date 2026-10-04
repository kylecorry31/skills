---
name: handoff
description: Use when asked for a handoff document, or a brief another agent or developer can implement from.
argument-hint: "<what to hand off> [output path]"
---

Write a handoff document that another agent or developer can implement from without the conversation. The reader has none of your context and may be working in a different repo, so state what they need and no more.

Include only settled decisions. List open questions as `Unresolved:` bullets, and do not invent requirements.

## Contents
Use these sections, dropping any that do not apply:

- **Goal**: one or two sentences on the outcome. For a bug, the problem and its impact.
- **Behavior**: what the finished work does. Include triggers, flows, success, failure, and cancellation behavior, defaults, arguments, config keys, and exact labels or strings.
- **Suggested approach**: for a bug or a change in a library, the fix or API the consumer needs, with a short code sample when it is clearer than prose.
- **Tests**: the cases to cover, including the one that reproduces a bug.
- **Code references**: the few paths most likely to shorten implementation, including an existing analogous implementation. Search the repo for these before writing. Name the repo and version when the reader works elsewhere.
- **Notes**: constraints and follow-ups, kept apart from the agreed behavior.

Write in direct engineering language with short bullets. Use `code` formatting for symbols, paths, commands, and literal values. Leave out conversation history and rationale.

Save it to the requested path. Without one, use `.scratch/handoff-<short-kebab-name>.md` if the repo has a `.scratch` folder, otherwise the repo root. Finish by confirming the file exists and gives the goal, the main flow, and the defaults.
