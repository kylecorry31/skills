---
name: proof-of-concept
description: Create a throwaway proof-of-concept to test ideas quickly without affecting the main project.
disable-model-invocation: true
---

Create a proof of concept of the given idea or feature to evaluate its feasibility and potential impact. Proofs of concept are throwaway experiments used to determine if an idea is even feasible before investing significant time and resources. This means the code quality and overall implementation may be rough and not production-ready. It does not need to have tests, documentation, follow best practices, or pass linting (unless it blocks building/running). It can hardcode values (e.g., string literals, fixed numbers) and skip error handling.

A good proof of concept is focused to just the core idea or feature it aims to validate.

After you get something working, have the user evaluate it and provide feedback that you can quickly iterate on. If they are satisfied, they may ask you to give it a quick clean-up to make it easier to translate from a proof of concept to a more polished, production-ready implementation.

To clean up the proof of concept, refactor with the only goal of improving readability for someone using this as a reference for a more polished implementation. The focus here should be making sure that the diff is readable and easy to understand. You are not being asked to productionalize the code. Then write a markdown summary explaining the details of the changes made (Simplified Technical English, no fluff) to .scratch/proof-of-concept-<name of the proof of concept>.md.
