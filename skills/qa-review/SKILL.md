---
name: qa-review
description: Perform a QA review of changes
disable-model-invocation: true
argument-hint: "<changes to test: branch, tag range, PR, or feature> [build, device, time limit]"
---

Test the changes you are asked to review to ensure they are in good shape to roll out to users. Act as a user: go through the available documentation (user guide, release notes, in-app text, work items, etc.) and hit all the new features, changes, and bug fixes, including edge cases and alternate ways of using them. Interact only with visible elements, and view screenshots to confirm what is on screen.

Test only the changes the user named. Before testing, confirm the installed build contains those changes (version, commit, or branch) and is not a different branch. If the user gives a time limit or asks for a smoke test, cover only the major changes, but keep the same tracking files below.

If you have the option to test with multiple build types, prefer a release or staging build over a debug build. Follow any build, URL, or device instructions from the user. Use an emulator unless told otherwise. On a physical device, do not install builds or change settings unless the user said you may, and say when you are done with it so they can unplug it. How you automate interactions depends on the target platform and installed tools. Other skills may be available to help.

You can write automated tests to help, but do not modify the code under test, except temporary log statements when the user allows them (remove them afterward). If you find a bug, report it in the QA findings and let the developers fix it.

Create `.scratch/<name-for-review>-qa/TODO.md` and `.scratch/<name-for-review>-qa/review.md` before running the first test. Keep both files up to date throughout the review. Use the following template for `review.md`:

```markdown
# <Release Version Name> QA Findings

## Test Results

### <Feature 1>
- **PASS**: Describe what was tested (include commit/issue/PR number) and why you believe it behaved as expected. No appendix needed.
- **FAIL**: Describe what was tested (include commit/issue/PR number) and why you believe it did not behave as expected. Include repro steps, stack traces, screenshots, and other details that a developer would find useful to fix this in the Appendix section. Include the Appendix letter here.
- **PARTIAL**: Describe what was tested (include commit/issue/PR number) and why you are unsure if it behaved as expected or not. Include repro steps, stack traces, screenshots, and other details that a developer would find useful to fix this in the Appendix section. Include the Appendix letter here.
- **NOT TESTED**: Describe what you couldn't test and why. Provide steps for how to test this manually if possible. No appendix needed.

### <Feature 2>
...

### <Feature 3>
...

### Misc. Features
You can put small changes here rather than creating feature sections. Use the same format as the feature sections.

## Appendix

### Appendix A
Put detailed stack traces, screenshots (use markdown images), etc. here. Screenshots and other large assets can be stored in `.scratch/<name-for-review>-qa/assets/`.

### Appendix B
...
```

# Process

## 1. Set up tracking
Create a TODO item for each test scenario, including edge cases and alternate user paths. Derive scenarios from each change, then vary them where bugs tend to hide, as far as the change makes them relevant (not all of these are needed, use judgement based on what changed):

- **Inputs**: boundary values, empty, invalid, very long, and unusual units, time zones, or locales.
- **State**: first use, existing data after upgrading from the previous release, and moving between the feature's states, such as on/off or before/after a setting changes.
- **Interruptions**: rotation, backgrounding and resuming, the app process being killed and restored, screen lock, and losing network or a permission mid-task.
- **Environment**: permissions denied, light and dark theme, large font size, and a screen reader for changed UI.
- **Regressions**: existing features that share code or screens with the change.

Before running a scenario, decide what the correct result is from the documentation, the previous release, or consistency with the rest of the app, not from what the build does. Mark a scenario's item in progress (change `[ ]` to `[~]`) and save `TODO.md` immediately before starting it, including each scenario in a batch.

## 2. Run the tests
Run scenarios individually, or in small batches when they are independent or share setup, state, or tooling. Do not batch scenarios when one depends on another's result, changes shared state in a way that affects the others, or would make progress ambiguous.

Capture screenshots, logs, and reproduction details while testing. Watch the logs for crashes, errors, and warnings even when the screen looks correct. For each failure, record the build, device, exact steps, expected and actual results, and how often it reproduces. As each scenario finishes, in the same turn, add its `PASS`, `FAIL`, `PARTIAL`, or `NOT TESTED` result to `review.md` and mark its TODO item `[x]` if complete or `[!]` if blocked or failed. Before starting the next scenario or batch, confirm every completed scenario has a result in both files. If testing is interrupted, leave both files showing the completed and in-progress scenarios so another reviewer can resume. Do not reconstruct either file at the end.

## 3. Finish the review
When testing is complete, check both files: every TODO item has a terminal status, every tested scenario has one clear result in `review.md`, every `FAIL` and `PARTIAL` includes the appendix details, assets are linked correctly, and no findings or blocked tests are missing. Resolve any discrepancies.
