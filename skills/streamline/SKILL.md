---
name: streamline
description: Suggest ways to reduce the steps, decisions, and input a workflow asks of its user.
disable-model-invocation: true
argument-hint: "<workflow, feature, or process> [constraints]"
---

Review a workflow and suggest changes that ask less of its user. Measure cognitive load and number of actions, not code size or visual polish. Make no changes: the user decides what to adopt.

Walk the real flow in the code, UI text, and docs, and read what each option does, not what its label says. Count the actions on the common path. If you cannot tell what the primary workflow is or how users mainly use it, ask the user with the harness's question tool, not in plain text, before suggesting anything. Do not ask about anything else.

Prefer, in order: remove, merge, default from context, automate, demote to a secondary menu, rename by outcome. Do not automate anything destructive, irreversible, or visible to others unless it can be undone. Demote rather than remove a capability some users need. Never bypass permission or consent prompts.

# Report

Lead with the recommended end state for the common path and the actions it saves. Then list each suggestion with the current behavior, the proposed behavior, the tradeoff, and your recommendation, ordered by interaction saved per risk. List ideas that need new data, settings, or infrastructure separately under `Later`.
