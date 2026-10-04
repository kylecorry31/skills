---
name: proofread
description: Proofread text for grammar and spelling.
disable-model-invocation: true
argument-hint: "<files, directory, or 'staged changes'>"
---

Proofread the provided files and ONLY make minor corrections to grammar or spelling. Keep the author's wording, tone, markdown structure, and line breaks. For a directory, proofread each text file in it. For staged or uncommitted changes, proofread only the changed lines. In code and config files such as source and YAML, change only comments and user-visible text.

Summarize what you changed and why.

If you do not have the ability to edit, output a list of the issues you found and suggested fixes. Include enough context for each issue so the user can easily find and fix them.

If there are readability issues, list them out to the user rather than changing the text.
