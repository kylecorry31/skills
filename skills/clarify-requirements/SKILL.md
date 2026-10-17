---
name: clarify-requirements
description: Interview the user until the requirements for a feature, change, or plan are clear.
disable-model-invocation: true
argument-hint: "<feature, change, or plan>"
---

Interview the user until every decision that affects the implementation is settled. Do not write code or a plan.

Explore the code, docs, and existing behavior first, and ask only what they cannot answer. Work through the decisions in dependency order, so an answer that makes later questions unnecessary is asked first.

Ask with the harness's question tool, not in plain text. Put your recommended answer first in each question's options. Batch independent questions into one call and ask dependent ones separately. Follow up on vague or conflicting answers rather than accepting them.

Stop when nothing that would change the implementation is left open, or when the user says to stop. Then summarize the settled decisions, the scope exclusions, and anything left unresolved, in a form that can be passed to the `handoff` skill.
