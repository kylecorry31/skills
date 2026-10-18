---
name: code-review
description: Review code and report only real bugs and serious problems.
disable-model-invocation: true
argument-hint: "[PR number | since <tag> | uncommitted | <area to review>] or findings to verify"
---

Review without changing code.

Scope (choose the first that applies):
1. User-requested scope
2. Uncommitted changes
3. Changes between the current branch and the base branch
4. Ask the user

When given existing findings, do not run a new review. Check each against the current code, then keep, relabel, or drop it, and rewrite the kept ones in the report format below.

Establish intent from the description, commits, docs, or linked issue; ask if unclear. Report only material problems with a concrete failing scenario or demonstrable cost. For diffs, report only problems introduced or worsened by the change. Exclude polish, reasonable style or design choices, speculative future issues, nitpicks, and unnecessary generality, tests, or docs. Flag style or naming only when it violates a documented rule or actively misleads readers.

Deduplicate findings and order them by severity:

- **Blocking**: breaks normal intended behavior, risks security/data loss, or causes a serious regression. Requires a fix or an explanation of why it is not a problem.
- **Consider**: a real but rare or limited problem, or a reasonable trade-off the author may accept.

Explain the trigger and impact. Suggest a fix only when it is not obvious. If you reviewed only part of the scope, or an area needs expertise you could not apply, say so at the end. If no findings remain, output only `No issues found.` Otherwise use:

```
# Code Review Results

## 1. [<Blocking|Consider>] <one-line description> (`<file>:<line>`)

<Trigger and impact>
```

If asked to save a report without a filename, use `code-review-<timestamp>-<slugified-short-description>.md`.
