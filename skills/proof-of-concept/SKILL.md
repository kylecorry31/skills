---
name: proof-of-concept
description: Create a throwaway proof-of-concept to test ideas quickly without affecting the main project.
disable-model-invocation: true
argument-hint: "<idea, feature, or issue URL>"
---

Build a throwaway proof of concept to find out whether the given idea or feature is feasible before the user invests in it. Code quality can be rough: no tests, documentation, linting, or error handling, and values can be hardcoded, unless something blocks building or running. Keep it focused on the core idea.

Before building, say in a few sentences what question the proof of concept answers and how you will answer it.

Keep experiments quick. If a step will take more than a few minutes, such as a large download or training run, start with the smallest version that gives a signal and tell the user.

After you get something working, report what it showed: whether the idea is feasible, with measurements where they matter (performance, size, accuracy). Then let the user evaluate it and give feedback to iterate on. If they are satisfied, they may ask for a clean-up to make it easier to turn into a polished implementation.

To clean up, refactor only for readability, so the diff is easy to follow for someone using it as a reference. Do not productionalize the code. Then write a markdown summary of the changes (Simplified Technical English, no fluff) to `.scratch/proof-of-concept-<name of the proof of concept>.md`.
