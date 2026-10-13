---
name: automated-testing
description: Use when writing, updating, reviewing, or fixing unit tests or end-to-end tests, or when fixing a bug that needs a regression test.
---

Follow these preferences when writing tests. They apply to any framework or platform, so follow the project's existing test conventions for everything they don't cover.

Write the fewest tests that pin down the behavior that changed. Skip trivial or incidental behavior, but do cover the boundaries and error paths of the changed behavior, such as empty input, limits, and invalid values. Prefer a unit test over an end-to-end test when it would catch the same regression.

Test behavior through the public API, the way real callers use it, so a test only breaks when the behavior does. Do not test private members or expose internals just for a test. If a test is the only caller of a method, test the real entry point and delete the method. Assert on the returned value or resulting state, not on which internal calls were made.

Each test covers one behavior, is laid out as arrange, act, assert, and is named for the scenario and expected outcome. Keep the details that matter to the outcome visible in the test body rather than hidden in shared setup; prefer clear repetition over clever helpers. Avoid loops, conditionals, and computed strings in tests. Use parameterized tables when many inputs share one assertion, with a short comment for each group of scenarios. Make failures readable: assert with the matcher that reports expected and actual values, not a bare true/false check.

Expected values must be hardcoded from an independent source, such as hand math, a reference tool, or a lookup. Do not compute them with the code under test or paste in what it returned, except in the refactor safety net below.

Tests must be deterministic and hermetic. Inject or fix the clock, time zone, locale, random seeds, and coroutine or thread dispatchers, and never depend on the network or other tests' state.

For dependencies, prefer the real implementation when it is fast and deterministic, then an existing or simple fake, then a stub that returns canned values. Verify calls on a mock only when the call itself is the behavior, such as sending a message or a cache avoiding a fetch, and check only the arguments that matter. Do not mock types you don't own when a fake or the real thing would work.

Never make a failing test pass by weakening it. Do not delete cases, loosen assertions, add sleeps, or comment the test out. Find the root cause instead. Do not add retries to hide a flaky test. If a test only fails in CI, read the logs and screenshots before changing anything.

## Bugs and refactors

If asked to fix a bug, use red/green TDD. Write a test that reproduces the bug and fails for the right reason, then fix it. If you cannot reproduce the bug with a test, say so before fixing it.

When adding a test for a fix that already exists, and it is not clear that the test would have failed before the fix, temporarily back out the fix and confirm the test fails for the right reason. Then restore the fix and confirm it passes. Undo the change by editing the code, not by discarding uncommitted work.

Before a refactor, add tests that lock in the current behavior, then make the change. These may use the current output as the expected value, but check that it is plausible, and replace it with an independently derived value wherever the correct answer matters. Alter as few existing test cases as possible so the diff shows whether behavior changed.

## End-to-end tests

Keep end-to-end tests few and focused on what users depend on. Cover each important user journey once, and push edge cases and calculations down to unit tests. When an end-to-end test catches a bug that no unit test caught, add the unit test too.

Each test starts from a known state, so a failure points at one cause. Tests are independent: they pass in any order or on their own, and none relies on another's leftovers.

Seed the starting state (data, settings, fixed location and time) through the app's real storage or API instead of clicking through setup. This keeps tests fast and lets them assert exact values, so it is the way to handle expensive setup, not combining behaviors into one long test. Seeding only sets the starting point: the behavior under test still runs through the visible UI, and expected values still come from an independent source.

Keep a few journey tests that start from a clean state and act as the user end to end, such as creating, editing, and deleting an item. A journey is one scenario whose steps genuinely build on each other, not a grab bag of unrelated checks.

Find elements by user-facing text or type, falling back to an ID, never by position. Wait for the condition you need instead of sleeping. Do not mock the stack being verified, but do replace external services you don't control, such as remote APIs, with fakes so the test stays hermetic. Run on an emulator or other disposable environment rather than the user's own device.
