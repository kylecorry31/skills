---
name: simplify
description: Simplify code while preserving its behavior.
disable-model-invocation: true
argument-hint: "[uncommitted | since <ref> | <files or area>]"
---

Make the code smaller and simpler without changing what it does. Fewer concepts matter more than fewer characters; do not golf.

Scope is the named code, `since <ref>`, or by default the uncommitted changes. Read usages outside the scope to confirm a change is safe, but edit only inside it.

# Preserve behavior

- Run the relevant tests before and after. If the baseline is red, stop and tell the user. Without tests, make only changes provable by reading.
- Never change behavior, even to fix a bug. Report it instead.
- Accept a slowdown nobody would notice. Skip and report one on a hot path or large input.

# Keep the user in control

Apply without asking:

- Provably dead or redundant code, and unclear private or local names.
- Comments that restate the code or are stale. Keep comments that explain why.
- Unreferenced dependencies, config, and files in the diff's area.
- Unused public or exported code, unless the project is a library or API. Infer that from the manifest and docs, and ask if unclear. Never touch a library's public surface.

Ask first about:

- Anything that could be intentional: abstractions, wrappers, test seams, extension points.
- Restructuring, new dependencies, and anything with several valid designs.
- Unreferenced dependencies, config, and files outside the diff's area.
- Changes to what tests assert or cover.

Apply the clear cleanups first, then ask the rest in one batched question-tool call. For each, give the finding, the suggested change with its cost, any other design, and leaving it as is. Make no structural change until the user answers.

# Simplify

Prefer, in order: delete, reuse the standard library or existing code, merge duplicates, flatten, remove repeated work.

- Merge duplicates only at three or more occurrences that change for the same reason.
- Simplify tests like other code.
- Do not format code or run the formatter.

# Report

Net lines removed, test results before and after, anything unverified or skipped, and a "Noticed, not changed" list of bugs and other findings left alone. If the code is already simple, say so and change nothing.
