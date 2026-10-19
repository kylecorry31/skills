---
name: streamline
description: Question requirements and suggest what to delete, default, or automate to reduce the complexity and the steps, decisions, and input a system asks of its users.
disable-model-invocation: true
argument-hint: "<code, feature, or workflow> [constraints]"
---

Review the target in five steps, in order. Eliminate before improving: do not suggest simplifying, speeding up, or automating anything an earlier step would delete. Measure cognitive load, number of actions, and moving parts, not code size or visual polish. Make no changes: deleting a requirement changes behavior, so the user decides what to adopt.

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

Simplify what remains: merge steps, flatten structure, and default or infer inputs from context instead of asking.

# 4. Speed up the cycle

Shorten the time between a user's action and the result they came for. Prefer skipping work over making it faster, and only target flows that survived steps 2 and 3. Look for blocking steps that could happen in the background, repeated waits for the same data, and round trips or screens between the user and the result.

# 5. Automate

Automate what the user still does by hand after the earlier steps. Look for values that can be detected, pre-filled, or synced instead of typed, recurring actions that can run on a schedule or trigger, and decisions the system can make from context. Do not automate anything destructive, irreversible, or visible to others unless it can be undone. Never bypass permission or consent prompts.

# Report

Lead with the recommended end state, the code, dependencies, concepts, and common-path actions it removes. Then list each suggestion with the requirement it challenges, its evidence, the current behavior, the proposed behavior, the tradeoff, and your recommendation, grouped by step and ordered by removal and interaction saved per risk. List anything you kept despite looking removable, with why, under `Kept`. List ideas that need new data, settings, or infrastructure separately under `Later`.
