---
name: bug-investigation
description: Investigate a bug to identify the root cause and reproduction steps.
disable-model-invocation: true
---

Given a bug report (description, log, etc), create steps to reproduce the problem and identify the root cause. Do not actually fix the bug, but do create a regression test that the user can use to fix the bug using TDD.

# Process

## 1. Understand the bug report
Read the provided bug report and any associated logs, screenshots, or other information. If a stack trace is provided, identify where in the code it is thrown and what would cause it to be thrown. Trace up the call stack until a hypothesis can be made about which action would cause the error.

You should have an idea of what actions or inputs would cause the bug to occur.

## 2. Reproduce the bug
Create a regression test or a script to reproduce the bug. If there are existing tests in the same module as the bug, extend them. Otherwise, prefer an end-to-end test since that will capture the full context of the bug and should align with the repro steps. If the codebase is not set up with an end-to-end test suite or a unit test can clearly isolate the bug, then write a unit test. If the bug is difficult to reproduce, try to isolate the code or pull it into a script as a proof of concept with hard-coded inputs (or just hard-code inputs in the app's code) and test.

The output of this step should be a set of steps that can reliably reproduce the bug and a regression test that will fail when the bug is present and pass when it is fixed.

If you are unable to reproduce the bug, ask the user what the next steps should be. Describe what you tried and what the results were.

## 3. Identify the root cause
Analyze the code and any relevant data to determine the underlying cause of the bug. If a bad input is the immediate cause, trace back to where that input is coming from and why it is invalid. Continue doing this until you reach the root cause of the bug.

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

## Reproduction Steps
1. Step 1
2. Step 2
3. ...

<regression test code if applicable, in code blocks>

```

The reproduction steps should be user focused (e.g. how to reproduce the bug using the UI) whenever possible. If you were only able to reproduce the bug with a unit test, then include a note that the bug cannot be reproduced through the UI and just provide the unit test code. The regression test code should be embedded in the report as a code block.

If the user asks you to write the report to a file but doesn't specify a name, use the format `bug-investigation-<timestamp>-<slugified-short-description>.md`.