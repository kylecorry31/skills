---
name: automated-testing
description: Use when writing, updating, reviewing, or fixing unit tests or end-to-end tests, or when fixing a bug that needs a regression test.
---

Follow these preferences when writing tests. They apply to any framework or platform, so follow the project's existing test conventions for everything they don't cover.

Expected values must be hardcoded from an independent source, such as hand math, a reference tool, or a lookup. Do not compute them with the code under test or paste in what it returned, except in the refactor safety net below. Do not test private members or expose internals just for a test. If a test is the only caller of a method, test the real entry point and delete the method. Use parameterized tables when many inputs share one assertion, with a short comment for each group of scenarios.

Never make a failing test pass by weakening it. Do not delete cases, loosen assertions, add sleeps, or comment the test out. Find the root cause instead. Do not add retries to hide a flaky test. If a test only fails in CI, read the logs and screenshots before changing anything.

## Bugs and refactors

If asked to fix a bug, use red/green TDD. Write a test that reproduces the bug and fails for the right reason, then fix it. If you cannot reproduce the bug with a test, say so before fixing it.

When adding a test for a fix that already exists, and it is not clear that the test would have failed before the fix, temporarily back out the fix and confirm the test fails for the right reason. Then restore the fix and confirm it passes. Undo the change by editing the code, not by discarding uncommitted work.

Before a refactor, add tests that lock in the current behavior, then make the change. These may use the current output as the expected value, but check that it is plausible, and replace it with an independently derived value wherever the correct answer matters. Alter as few existing test cases as possible so the diff shows whether behavior changed.

## End-to-end tests

Keep end-to-end tests few and focused on what users depend on. Cover each important user journey once, and push edge cases and calculations down to unit tests.

Each test covers one behavior, is independent of the others, and passes in any order or on its own. Every test starts from a known state, so a failure points at one cause. Do not chain tests or let one rely on another's leftovers.

Seed the starting state (data, settings, fixed location and time) through the app's real storage or API instead of clicking through setup. This keeps tests fast and lets them assert exact values, so it is the way to handle expensive setup, not combining behaviors into one long test. Seeding only sets the starting point: the behavior under test still runs through the visible UI, and expected values still come from an independent source.

Keep a few journey tests that start from a clean state and act as the user end to end, such as creating, editing, and deleting an item. A journey is one scenario whose steps genuinely build on each other, not a grab bag of unrelated checks.

Find elements by stable, user-facing identifiers (like text/type or an ID as fallback) rather than position or layout. Wait for the condition you need instead of sleeping. Do not mock the stack being verified. Run on an emulator or other disposable environment rather than the user's own device.
