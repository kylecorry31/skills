---
name: automated-testing
description: Use when writing, updating, reviewing, or fixing unit tests or end-to-end tests. Also use when performing a refactor or bug fix.
---

## Automated Testing Guidelines

- Reduce test code duplication by using parameterized tests, helper functions, and shared setup code.
- Prefer unit tests over e2e tests.
- Do not write tests that are tightly coupled to the implementation details.
- Obtain expected values from an independent source, not from the code under test.
- Prefer real implementations over mocks when possible, but use mocks for slow, non-deterministic, or hard-to-control dependencies.
- Do not weaken or remove tests to make them pass.
- Use TDD when fixing a bug or refactoring code.
- Seed the starting state of expensive e2e tests rather than performing the setup through the UI.