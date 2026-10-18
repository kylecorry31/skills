---
name: bug-investigation
description: Investigate a bug to identify the root cause and reproduction steps.
disable-model-invocation: true
argument-hint: "<bug report, issue URL, stack trace, logs, or suspected finding>"
---

Reproduce a bug report and identify the root cause.

1. Form hypotheses: list the candidate minimal reproduction steps (inputs, state, and actions that would trigger the bug), most likely first. Use code inspection only to generate and rank hypotheses, never as confirmation.
2. Confirm each hypothesis with an automated test that fails because of the bug, starting with the cheapest level that can exercise it:
   1. Unit test
   2. Integration or end-to-end test
3. Treat a hypothesis as confirmed only when its test fails for the reported reason. If it passes or fails for a different reason, rule the hypothesis out and move to the next.
4. Trace the failing test to the root cause.

The report must be self-contained, since it may be pasted into an issue tracker without the code. The tests are only a means of confirmation: don't reference them or their file paths in the report. Write the reproduction steps so that someone can follow them by hand or turn them into a regression test later.

Output a report with this format:

```markdown
A brief description of the bug.

## Actual Behavior
...

## Expected Behavior
...

## Root Cause
...

## Introduced
The commit or release that introduced the bug (if easy to find or the user explicitly asked for it).

## Ruled Out
If you were unable to reproduce the bug or identify its root cause, explain what you tried and why it didn't work.

## Reproduction Steps
1. ...

## Stack Trace
If applicable.

## Suggested Fix
A description of the proposed solution to fix the bug, if applicable.
```

If asked to save a report without a filename, use `bug-investigation-<timestamp>-<slugified-short-description>.md`.
