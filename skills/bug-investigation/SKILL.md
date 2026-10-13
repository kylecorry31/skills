---
name: bug-investigation
description: Investigate a bug to identify the root cause and reproduction steps.
disable-model-invocation: true
argument-hint: "<bug report, issue URL, stack trace, logs, or suspected finding>"
---

Given a bug report (description, issue, log, stack trace, or a suspected finding from a review), create steps to reproduce the problem and identify the root cause. Do not fix the bug unless the user asks you to. Either way, create a regression test the user can use to fix it with TDD.

# Process

## 1. Understand the report
Read the report and any attached logs or screenshots. Read the code involved until you understand how it is meant to work. Form a hypothesis about the actions or inputs that trigger the bug, starting with the most likely explanation and with what changed recently. Check that the bug is real and still present in the current code. If it is not, say why and stop.

## 2. Reproduce the bug
Create a regression test or a script that reproduces the bug. Extend the existing tests of the affected module when there are any. Use the cheapest test that reproduces the bug: a unit test when it isolates the bug, an end-to-end test when the bug only appears through the UI or an integration. If the bug is hard to reproduce, isolate the code into a script with hard-coded inputs. Then shrink the inputs and steps to the smallest set that still fails. For intermittent bugs, find the conditions that matter, such as timing, ordering, time zone, or device state, and control them rather than relying on many runs.

Confirm the test is valid by prototyping a quick fix: the test must fail without the fix and pass with it. Then remove the prototype. If the user asked you to fix the bug, implement the proper fix after step 3 instead, and keep it.

This step is complete when you have steps that reliably reproduce the bug and a test that fails while the bug is present. If you cannot reproduce it, describe what you tried and the results, and ask the user how to proceed.

## 3. Identify the root cause
Trace the immediate cause back to its origin, such as where a bad input comes from, until you reach the root cause. Confirm each step by observing the actual values, with logging, a debugger, or assertions, rather than reasoning about what they should be. When the cause is unclear, narrow it by halving the search space, and change one thing at a time. Keep a short list of the hypotheses you ruled out and the evidence against each, and include it in the report.

Then find when the bug was introduced, and whether it is a regression since the last release tag or was already there. If the history is long or the cause is unclear and the working tree is clean, use `git bisect run` with the reproduction test or script, kept outside the repository, and return to the original commit with `git bisect reset` when done.

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

## Ruled Out
Hypotheses you eliminated and the evidence against each, if any.

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
