---
name: simplify
description: Simplify code while preserving its behavior.
disable-model-invocation: true
argument-hint: The scope of the simplification request.
---

Refactor the requested code to be as simple and idiomatic as possible.

Scope (choose the first that applies):
1. User-requested scope
2. Uncommitted changes
3. Changes between the current branch and the base branch
4. Ask the user

**Do not**:
- Change behavior (including fixing bugs; report them to the user instead)
- Play code golf
- Change public APIs (only applies to libraries or API surfaces)
- Introduce new dependencies
- Expand the refactor beyond what was requested

**Ask the user**:
- Before making architectural changes
- Before removing abstractions that appear intentional
- If the simplification may cause a large performance impact

Report a brief summary of what was simplified and why.