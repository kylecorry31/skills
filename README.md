# Skills

## Catalog

- **automated-testing**: Guides writing unit and end-to-end tests the way I prefer: public-behavior tests, hardcoded independent expectations, red/green TDD for bugs, and stable UI automation. Framework and platform agnostic.
- **bug-investigation**: Investigates a reported bug. Provide the report and any logs or screenshots, and it reproduces the bug, finds the root cause, and writes an investigation report. It fixes the bug too if you ask.
- **ci-failure**: Finds why a CI run or job failed, decides whether it is a regression, flaky, environmental, or transient, and fixes the root cause when there is one.
- **code-review**: Finds bugs or deviations from standards in a diff or codebase snapshot. Use it as a second pass after your own manual review.
- **dependency-update**: Updates dependencies or reviews version bumps by reading the upstream changes, applying breaking changes, and listing what to test manually.
- **fact-check**: Checks claims in text against authoritative sources and generates a report linking each claim to source snippets. Click each claim's highlight to verify the quotes and links yourself.
- **handoff**: Writes a self-contained handoff document that another agent or developer, possibly in a different repo, can implement from.
- **proof-of-concept**: Builds a throwaway experiment to test whether an idea or feature is feasible before you invest in a polished implementation.
- **proofread**: Fixes spelling and grammar in a text file with minimal changes. It edits the file, so use version control and review the diff. Inspired by https://en.wikipedia.org/wiki/Wikipedia:Writing_articles_with_large_language_models
- **qa-review**: Tests a change before release, such as against an emulator for Android apps. Use it as a second line of defense after your own QA.
- **simplify**: Removes and simplifies code while preserving behavior, preferring deletion, reuse of what exists, and flatter code over new abstractions. It edits files, so use version control and review the diff.
- **streamline**: Reviews a workflow, feature, or process and suggests removals, defaults, and automations that ask less of the user. It only makes suggestions and does not edit anything.
- **translation-review**: Compares source and translated text and reports whether the translation should be accepted or changed. Useful when you don't know the target language.

## Installation
This repository is an [Agent Plugin](https://agent-plugins.org/) containing reusable Agent Skills for software and content review. It is skills-only and does not provide an MCP server.

## Support
I don't plan on providing support if it isn't working for you. I'll keep it up to date if I find it useful.
