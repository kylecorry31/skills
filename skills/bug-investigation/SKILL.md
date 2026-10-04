---
name: bug-investigation
description: Investigate a bug to identify the root cause and reproduction steps.
disable-model-invocation: true
argument-hint: "<bug report, issue URL, stack trace, logs, or suspected finding>"
---

Given a bug report (description, issue, log, stack trace, or a suspected finding from a review), create steps to reproduce the problem and identify the root cause. Do not fix the bug unless the user asks you to. Either way, create a regression test the user can use to fix it with TDD.

# Process

## 1. Understand the report
Read the report and any attached logs or screenshots. Form a hypothesis about the actions or inputs that trigger the bug. Check that the bug is real and still present in the current code. If it is not, say why and stop.

## 2. Reproduce the bug
Create a regression test or a script that reproduces the bug. Extend the existing tests of the affected module when there are any. Use the cheapest test that reproduces the bug: a unit test when it isolates the bug, an end-to-end test when the bug only appears through the UI or an integration. If the bug is hard to reproduce, isolate the code into a script with hard-coded inputs.

Confirm the test is valid by prototyping a quick fix: the test must fail without the fix and pass with it. Then remove the prototype. If the user asked you to fix the bug, implement the proper fix after step 3 instead, and keep it.

This step is complete when you have steps that reliably reproduce the bug and a test that fails while the bug is present. If you cannot reproduce it, describe what you tried and the results, and ask the user how to proceed.

## 3. Identify the root cause
Trace the immediate cause back to its origin, such as where a bad input comes from, until you reach the root cause. Then use git history to find when the bug was introduced, and whether it is a regression since the last release tag or was already there.

## 4. Document your findings
Output a report with this format:

```markdown
A brief description of the bug, its symptoms, and under what conditions it occurs.

## Actual Behavior
Describe what actually happens when the bug occurs.

## Expected Behavior
Describe what should happen if the bug were not present.

## Root Cause
Describe the root cause of the bug. Include a causal chain of events if applicable.

## Introduced
The commit or release that introduced the bug, or that it was already present.

## Reproduction Steps
1. Step 1
2. Step 2
3. ...

<regression test code if applicable, in code blocks>

## Stack Trace
The stack trace if applicable.

## Fix
Only if you fixed the bug: what you changed and why.

```

Write the reproduction steps from the user's point of view (such as using the UI) whenever possible. If the bug could only be reproduced with a unit test, say that it cannot be reproduced through the UI and give the unit test. Embed the regression test code in the report as a code block.

If the user asks you to write the report to a file but doesn't specify a name, use `bug-investigation-<timestamp>-<slugified-short-description>.md`.
