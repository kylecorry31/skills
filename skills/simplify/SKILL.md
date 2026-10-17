---
name: simplify
description: Simplify code while preserving its behavior.
disable-model-invocation: true
argument-hint: "[uncommitted | since <ref> | <files or area>]"
---

Make the code smaller and simpler without changing what it does. Less code is easier to read, test, and maintain, so prefer deleting over rewriting, and rewriting over adding. Fewer concepts matter more than fewer characters, so do not golf.

Scope is the user's fixed point or named code. Default to the uncommitted changes plus the branch's diff against `main`/`master`, and leave unrelated code alone.

# Preserve behavior

- Run the relevant tests before and after. Without tests, make only changes provable by reading, and say what is unverified.
- Keep public APIs, persisted formats, and error and logging semantics.
- Do not apply a change that alters behavior, even to fix a bug. Report it instead.

# Keep the user in control

Apply unambiguous cleanups yourself, such as dead code, unused imports and parameters, and redundant checks. Ask first about anything that could be intentional (an abstraction, a test seam, an extension point), anything that restructures the code (module boundaries, layering, patterns, new dependencies), and anything with several valid designs.

After applying the clear cleanups, ask the remaining questions with the harness's question tool, not in plain text. Batch them into one call. For each, state the finding and offer options: the suggested simplification with its cost, any other valid design, and leaving it as is. Make no architectural change until the user answers.

# Simplify

Use the first option that works: delete, reuse the standard library or existing code, merge duplicates that change for the same reason, flatten, then remove repeated work. Fix the underlying mechanism rather than layering a special case onto shared code.

# Report

Summarize the net lines removed, the test results, anything skipped, and the open questions. If the code is already simple, say so and change nothing.
