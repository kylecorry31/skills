---
name: streamline
description: Question requirements and suggest what to delete, default, or automate to reduce the complexity and the steps, decisions, and input a system asks of its users.
disable-model-invocation: true
argument-hint: "<code, feature, or workflow> [constraints]"
---

Review the target in three steps, in order. Eliminate before improving: do not suggest simplifying anything an earlier step would delete. Measure cognitive load, number of actions, and moving parts, not code size or visual polish. Make no changes: deleting a requirement changes behavior, so the user decides what to adopt.

# 1. Question the requirements

Walk the real flow in the code, UI text, and docs, and read what each option does, not what its label says. Count the actions on the common path. Trace each element to the requirement that justifies it, using callers, config, tests, docs, and `git log`/`git blame`. Treat every input a person must supply as a requirement to challenge.

Ask the user about what the code, docs, and history cannot answer: the primary workflow and how users mainly use it, and any requirement whose origin or necessity you cannot determine. Ask before suggesting anything, with the harness's question tool, not in plain text. Put your recommended answer first in each question's options, and batch independent questions into one call.

# 2. Delete

For each element, ask what breaks if it is removed and whether it exists only to compensate for another element. Look for:
- Features, options, and flags with no users or only one value in practice
- Abstractions, layers, and services serving one caller or a hypothetical future need
- Dependencies, middleware, and wrappers covering a small or removable need
- Retries, fallbacks, caches, and defensive checks hiding a root cause that can be fixed
- Tests and code that exist only to support a complicated design
- Steps and prompts that could be dropped rather than automated

Keep what provides essential reliability, security, observability, or maintainability. The goal is minimum necessary complexity, not minimum code. Demote rather than remove a capability some users need.

# 3. Simplify

Simplify what remains, preferring skipping work over making it faster or automating it. Look for:
- Steps that can be merged and structure that can be flattened
- Inputs that can be defaulted, inferred from context, detected, pre-filled, or synced instead of asked for or typed
- Actions or decisions that can be automated without user intervention
- Speed ups on the common path, such as blocking steps that could happen in the background, repeated waits for the same data, and round trips or screens between the user and the result

Do not infer or automate anything destructive, irreversible, or visible to others unless it can be undone. Never bypass permission or consent prompts.

# Report

Use exactly these headings, in this order, with each suggestion as a numbered item restarting at 1 under its heading so the user can refer to it as, for example, "Delete 2" or "2.2":

- `# 1. Question the requirements`, `# 2. Delete`, `# 3. Simplify`: one numbered item per suggestion, ordered by removal and interaction saved per risk. Each item states the requirement it challenges, its evidence, the current behavior, the proposed behavior, what it removes (code, dependencies, concepts, common-path actions), the tradeoff, and your recommendation.
- `# Kept`: anything that looked removable but was kept, with why.
- `# Later`: ideas that need new data, settings, or infrastructure.

Omit no heading; write "None" under an empty one.
