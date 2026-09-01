---
name: qa-review
description: Perform a QA review of changes
disable-model-invocation: true
---

Test the changes you are asked to review to ensure they are in good shape to roll out to users. Try to act as a user by going through the available documentation (user guide, release notes, in-app text, work items, etc.) and try to hit all the new features, changes, and bug fixes. Obtain and view screenshots to ensure it looks correct and to make sure you are only interacting with visible elements. Not all users will use the app in the same way, so try to test it in multiple ways and be sure to test edge cases.

You can write automated tests to help with your QA review, but do not modify the code under test. If you find a bug, report it in the QA findings and let the developers fix it.

If testing an Android app, perform your testing using a release/staging build on the connected emulator. Use ADB or Android tests for interacting with the device.

Continuously report your findings to `.scratch/<release-version-name>-qa/review.md` using the following template:

```markdown
# <Release Version Name> QA Findings

## Test Results

### <Feature 1>
- **PASS**: Describe what was tested (include commit/issue/PR number) and why you believe it behaved as expected.
- **FAIL**: Describe what was tested (include commit/issue/PR number) and why you believe it did not behave as expected. Include repro steps, stack traces, screenshots, and other details that a developer would find useful to fix this in the Appendix section. Include the Appendix letter here.
- **PARTIAL**: Describe what was tested (include commit/issue/PR number) and why you are unsure if it behaved as expected or not.
- **NOT TESTED**: Describe what you couldn't test and why. Provide steps for how to test this manually if possible.

### <Feature 2>
...

### <Feature 3>
...

### Misc. Features
You can put small changes here rather than creating feature sections. Use the same format as the feature sections.

## Appendix

### Appendix A
Put detailed stack traces, screenshots, etc. here. Screenshots and other large assets can be stored in `.scratch/<release-version-name>-qa/assets/`.

### Appendix B
...
```

Use `.scratch/<release-version-name>-qa/TODO.md` to create a to-do list for what you need to test. Keep this updated as you go along.