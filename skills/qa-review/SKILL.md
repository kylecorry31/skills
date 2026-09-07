---
name: qa-review
description: Perform a QA review of changes
disable-model-invocation: true
---

Test the changes you are asked to review to ensure they are in good shape to roll out to users. Try to act as a user by going through the available documentation (user guide, release notes, in-app text, work items, etc.) and try to hit all the new features, changes, and bug fixes. Obtain and view screenshots to ensure it looks correct and to make sure you are only interacting with visible elements. Not all users will use the app in the same way, so try to test it in multiple ways and be sure to test edge cases.

You can write automated tests to help with your QA review, but do not modify the code under test. If you find a bug, report it in the QA findings and let the developers fix it.

If testing an Android app, perform your testing using a release/staging build on the connected emulator. Use ADB or Android tests for interacting with the device.

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
Create a TODO item for each test scenario, including edge cases and alternate user paths. Before starting the first test, mark the relevant item(s) as in progress (for example, change `[ ]` to `[~]`) and save `TODO.md`.

## 2. Run the tests
Run scenarios individually, or in small batches when they are independent or share setup, state, or tooling. Do not batch scenarios when one depends on another's result, changes shared state in a way that affects the others, or would make progress ambiguous.

Capture screenshots, logs, and reproduction details while testing. As each scenario finishes, immediately add its `PASS`, `FAIL`, `PARTIAL`, or `NOT TESTED` result to `review.md`. In the same turn, mark its TODO item `[x]` if complete or `[!]` if blocked or failed, and save `TODO.md`.

Before starting another scenario or batch, confirm that every completed scenario from the previous batch has a result in both files. If testing is interrupted, leave the files showing the completed scenarios and any in-progress items so another reviewer can resume. Do not reconstruct either file at the end of the review.

## 3. Finish the review
After all testing is complete, review both files for completeness and clarity. Confirm that every TODO item has a terminal status, every tested scenario has one clear result in `review.md`, every `FAIL` and `PARTIAL` result includes the required appendix details, screenshots and other assets are linked correctly, and no findings or blocked tests are missing. Resolve any discrepancies before finishing the review.