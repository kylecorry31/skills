---
name: trim-prompt
description: Trim a skill or prompt down to what a frontier model would not do on its own.
disable-model-invocation: true
argument-hint: "<skill, prompt file, or directory>"
---

Edit the prompt so it keeps only what a capable model cannot infer. Cut anything it already knows or would do by default, and keep everything that steers it away from its defaults.

Keep:

- The user's preferences and constraints where they differ from the default behavior.
- Project-specific facts, names, formats, thresholds, and ordering rules.
- Behavior that must be exact, such as when to ask, when to stop, and what never to touch.

Cut:

- General knowledge, definitions, and generic best practices.
- Rationale, motivation, and examples that only restate a rule.
- Lists of obvious cases, hedging, emphasis, and repeated instructions.

When unsure whether the model would behave correctly without a line, keep it. Do not change what the prompt makes the model do, add new rules, or reword for style. Ask about anything where a cut could change behavior, with the harness's question tool, not in plain text.

Summarize the lines removed and list the non-obvious cuts so the user can restore them.
