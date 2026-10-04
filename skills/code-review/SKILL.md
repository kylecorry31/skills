---
name: code-review
description: Review code and report only real bugs and serious problems.
disable-model-invocation: true
argument-hint: "[PR number | since <tag> | uncommitted | <area to review>] or findings to verify"
---

Review without changing code. Report only material problems with a concrete failing scenario or demonstrable cost. For diffs, report only problems introduced or worsened by the change.

Exclude polish, reasonable style or design choices, speculative future issues, and unnecessary generality, tests, or docs. Flag style or naming only when it violates a documented rule or actively misleads readers.

# Scope

- **Diff review**: use the user's fixed point or PR, or review the current branch/worktree when off `main`/`master` or when uncommitted changes exist.
- **Snapshot review**: review the code the user names (files, a package, or a feature) as it is now, not a diff. On clean `main`/`master` with nothing named, ask what to review.
- **Verify findings**: when given existing findings (pasted or in a file), do not run a new review. Check each against the current code, then keep, relabel, or drop it, and rewrite the kept ones in the report format below.

For a PR, check it out if it belongs to the current repo and the tree is clean; otherwise clone to a temporary directory.

Include uncommitted changes unless told otherwise. Ask if the review scope is unclear.

Clean up any temporary files and directories you created after you have finished the review.

# Review

Establish intent from the description, commits, comments, docs, or linked issue; ask if unclear. Look for:

- **Functionality**: broken intended behavior, practical edge cases, or unintended effects on existing code.
- **Concurrency, security, compatibility**: races, deadlocks, vulnerabilities, data loss, missing migrations, or broken callers/data.
- **Performance**: regressions at realistic scale, such as N+1 queries or unbounded growth.
- **Design**: misplaced logic, broken component interactions, or complexity likely to cause maintenance bugs.
- **Tests**: incorrect tests or tests that pass despite broken behavior; missing tests only for risky new behavior.
- **Rules and docs**: documented project rule violations or docs/comments made false by the change.

Delegate to subagents and use smaller, less capable models as needed.

# Report

Deduplicate findings. Drop findings without a concrete failure or cost, or excluded by the criteria above.

Order findings by severity:

- **Blocking**: breaks normal intended behavior, risks security/data loss, or causes a serious regression. Requires a fix or an explanation of why it is not a problem.
- **Consider**: a real but rare or limited problem, or a reasonable trade-off the author may accept.

Explain the trigger and impact. Describe the problem; suggest a fix only when it is not obvious. If no findings remain, output only `No issues found.` Otherwise use:

```
# Code Review Results

## 1. [<Blocking|Consider>] <one-line description> (`<file>:<line>`)

<Trigger and impact>
```

If asked to save a report without a filename, use `code-review-<timestamp>-<slugified-short-description>.md`.
