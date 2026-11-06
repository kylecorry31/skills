---
name: bug-investigation
description: Use when asked to identify the root cause of a bug or write a bug report. Do not use if the bug is already known or trivial.
argument-hint: "<bug report, issue URL, stack trace, logs, or suspected finding>"
---

Reproduce a bug report and identify the root cause. Don't rely solely on code inspection unless it is very obvious from the code.

Once you are finished with your investigation, write a detailed report in the format below. The report must be self-contained, since it may be pasted into an issue tracker without the code. The tests are only a means of confirmation, so don't reference them or their file paths in the report. Write the reproduction steps so that someone can follow them by hand or turn them into a regression test later.

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

If asked to save a report without a filename, use `.scratch/bug-investigation-<slugified-short-description>.md`.
