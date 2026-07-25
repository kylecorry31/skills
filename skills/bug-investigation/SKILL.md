---
name: bug-investigation
description: Investigate a bug to identify the root cause and reproduction steps.
disable-model-invocation: true
---

Given a bug report (description, log, etc), create steps to reproduce the problem and identify the root cause. Do not actually fix the bug.

# Process

## 1. Understand the bug report
Read the provided bug report and any associated logs, screenshots, or other information. If a stack trace is provided, identify where in the code it is thrown and what would cause it to be thrown. Trace up the call stack until a hypothesis can be made about which action would cause the error.

You should have an idea of what actions or inputs would cause the bug to occur.

## 2. Reproduce the bug
Create a regression test or a script to reproduce the bug. If it can be isolated using a unit test, that will be the fastest way, but an automated end-to-end test is also acceptable. If the bug is difficult to reproduce, try to isolate the code or pull it into a script as a proof of concept with hard-coded inputs (or just hard-code inputs in the app's code) and test.

The output of this step should be a set of steps that can reliably reproduce the bug and a regression test that will fail when the bug is present and pass when it is fixed.

If you are unable to reproduce the bug, ask the user what the next steps should be. Describe what you tried and what the results were.

## 3. Identify the root cause
Analyze the code and any relevant data to determine the underlying cause of the bug. If a bad input is the immediate cause, trace back to where that input is coming from and why it is invalid. Continue doing this until you reach the root cause of the bug.

## 4. Document your findings
Produce a report at `bug-investigation-<timestamp>-<slugified-short-description>.md` in this format:

```markdown
A brief description of the bug, its symptoms, and under what conditions it occurs.

## Reproduction Steps
1. Step 1
2. Step 2
3. ...

## Actual Behavior
Describe what actually happens when the bug occurs.

## Expected Behavior
Describe what should happen if the bug were not present.

## Root Cause
Describe the root cause of the bug. Include a causal chain of events if applicable.

## Tests
List the regression tests you created. If the tests are self-contained and small, include them directly in the report. Otherwise, provide a link to where they can be found.
```
