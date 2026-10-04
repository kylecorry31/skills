---
name: ci-failure
description: Use when given a failing CI run or job, or asked why CI failed.
argument-hint: "<run or job URL> [investigate only | fix]"
---

Find out why a CI run failed and fix it, or explain why no fix is needed. Do not push, re-run, or cancel workflows, and do not edit workflow files unless the failure is in the workflow itself. Ask the user to do those. If the user says not to run anything, only read logs and code.

## 1. Gather the evidence
Read the failed job's log, not just the summary, and download its artifacts such as test results and screenshots. Look at the screenshots before deciding on a cause. Find the first error, since later ones are often fallout.

## 2. Classify the failure
Compare against the previous runs of the same workflow to see whether this is new, recurring, or intermittent, and which commit first broke it. Then decide which it is:

- **Regression**: a change broke something. Name the commit.
- **Flaky**: the same code passes and fails. Show the evidence.
- **Environment**: it passes locally but fails in CI. Find the difference, such as OS or API level, timing, hardware, missing state, or tool versions.
- **Transient**: a network outage, rate limit, or runner problem. Cite the log line.

If the failure is transient, report that and change nothing.

## 3. Reproduce locally
Run only the failing test or step, not the whole suite. Use an emulator, not a physical device, for tests that need one. If you cannot reproduce it, say so and fix the environment difference you found.

## 4. Fix the root cause
Make the failing run pass by fixing the cause. Do not weaken or delete the test, add retries, or add sleeps. If a new test caused the failure and is not worth its cost, say so and ask whether to remove it.

## 5. Report
State the class of failure, the root cause, and the fix. Separate what you verified locally from what only a new CI run can confirm.
