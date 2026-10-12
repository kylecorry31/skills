---
name: codegen
description: Generate or regenerate code in any language from a high-level spec of pseudocode, English, or structure, check a spec for errors, change its level of detail or simplify it, write a spec for existing code, or interview the user to draft or revise a spec from a description.
disable-model-invocation: true
argument-hint: "[implement|check|update|simplify|level|create|draft] <spec file, or what to describe>"
---

Generate code from a high-level spec. The spec is the source of truth and the code is a build artifact of it, so the user can edit the spec and regenerate. The spec is a file and may mix pseudocode, English steps, and structure such as `Class ABC: <description or interface>`. The code must do exactly what the spec says, no more and no less.

# Commands

- `/codegen [implement] <spec file>`: implement the spec, or update the code if it is already implemented. `implement` is optional.
- `/codegen check <spec file>`: compile the spec and report its errors, or `No errors.`, without writing code.
- `/codegen update <spec file>`: update the spec to match the current code.
- `/codegen simplify <spec file>`: rewrite the spec in simpler language without changing what it generates.
- `/codegen level <low|medium|high> <spec file>`: rewrite the spec at another level of detail.
- `/codegen create [low|medium|high] <what to describe>`: create a spec from existing code. Save it where the user says, otherwise next to the repo's other specs, or in `specs/<short-description>.md` if there are none.
- `/codegen draft [low|medium|high] <description, or spec file and the change>`: interview the user to write a new spec or revise an existing one. Save a new spec as `create` does.

Tell the user about these commands if they invoke the skill without arguments or the arguments are unclear.

# Spec levels

Each level up leaves more of the how to the generator.

- **Low:** line-level pseudocode. It fixes the steps, their order, conditions, and side effects, plus the names, signatures, and structure of everything it mentions.
- **Medium:** pseudocode or English for the rules and algorithms that decide behavior, with names and signatures for the public interface. It leaves helper functions, caching, and how the code is split up to the generator.
- **High:** English description of what the code does, its public interface, and the rules callers can depend on. It leaves the algorithms, and any names and structure it does not mention, to the generator.

A spec can mix levels, going lower only where the exact steps matter.

# Generate code from a spec

## 1. Establish the target
Use the language and code location the spec states. Otherwise infer them from the spec's file name and location, existing code, build files, and other specs.

## 2. Compile the spec
Treat the spec like source code and any problem with it like a compile error. Before writing any code, read the whole spec and find every place where it cannot be cleanly implemented as written:
- **Ambiguous:** a reasonable reader could implement it two ways that behave differently.
- **Conflicting:** two parts contradict each other, or a step contradicts a stated goal.
- **Nonsensical:** it cannot work, such as an impossible step or a loop with no exit.
- **Unresolved:** it references something that does not exist.
- **Unimplementable:** it cannot be done in the target language or repo without deviating from the spec.

Judge each place at the level the spec uses there. Line-level pseudocode leaves almost no room, so anything it leaves open that context does not settle is an error. A high-level description leaves the implementation open, so only report ambiguity that changes what the code does, not how it does it. Conflicts and nonsensical steps are errors at any level.

Trace the values that flow between steps and functions. A degenerate output one step can produce, such as an empty list or a zero length, must be something the step that consumes it can handle.

Do not be nitpicky. Report an error only if two competent implementers would produce observably different behavior, or the spec cannot work. It is not an error when:
- the language, repo, or common practice leaves only one reasonable reading;
- the spec gives signatures that require updating callers, tests, or other wiring;
- the spec uses a term standard in its domain, such as a well-known formula, or one the repo already implements; use that meaning.

When unsure, it is not an error. Apply the same bar every run, so a spec that compiles once compiles again unless it changed.

If there are any errors, write no code. Report every error at once, in this form, and stop:

```
error: <what is wrong with the spec>
  --> <spec file>:<line>
   | <the spec line, quoted>
   = needs: <the detail required to resolve it>
```

Do not guess, pick a default, work around the problem, or generate partial output. Wait for the user to update the spec, or offer to resolve the errors with them.

For `/codegen check`, stop after compiling.

### Resolve errors with the user
If the user asks, go through the errors as questions, asking independent errors together and any that depend on an earlier answer afterward. Suggest an answer for each, preferring the one that changes the least existing code and public API. Then edit the spec with the smallest change that resolves the error, at the level of the surrounding text.

After the last answer, compile again. Trace each changed rule through every step that uses its results, because a fix often exposes a case the original wording hid. When it is clean, continue with the original command.

## 3. Write the code
- Where the spec gives steps, keep their order, conditions, and side effects, without transliterating line by line. Where it names an algorithm or data structure, use that one.
- Use the names and signatures the spec gives, including parameter and return types, in the language's casing.
- If existing code uses different names or signatures, the spec wins: change them and update the callers and tests that break. Ask first if the change touches public API, callers outside the repo, or code that differs from the spec because of manual edits.
- If writing the code shows the spec cannot be followed as written, such as needing a different signature or a case it leaves undefined, do not choose for it. Stop and report it as a compile error.
- Do not restate the spec in comments.

## 4. Regenerate after spec changes
When code for the spec already exists, update it with the smallest diff that matches the revised spec. Keep the existing algorithm where the spec is silent.

Compare the whole spec to the code, not only the lines that changed, since the code may have drifted. If the code differs from the spec in ways the spec change does not explain, such as manual edits, ask before overwriting them. Leave code that the spec no longer describes untouched, and mention it in the summary.

## 5. Verify
Run the build and tests, then check each requirement in the spec against the code. If a test fails because it encodes behavior the spec changed, update the test. If a failure instead suggests the spec's behavior is wrong, report it with a recommended change to the spec, and change neither the spec nor the test. Add tests for new or changed behavior when that fits the repo's conventions.

Finish with a short summary of every change in observable behavior from the old code, including edge cases, accuracy, and performance, separate from pure refactors, and of anything you could not verify.

# Write or update a spec from existing code

For `create` and `update`, do not change the code. `create` takes the code to describe. `update` takes the spec, and the code is at the location it states. Ask if either is missing.

## Create
If the user gives a level, write the whole spec at that level. Otherwise choose the level that best captures what the code does, leave out implementation details that do not affect it, and go lower only where the exact steps matter, such as a specific algorithm, a required order of operations, or a performance constraint.

The spec must be good enough to regenerate the code with this skill:
- State the target language and the code's location.
- Describe what the code actually does, not what it ought to do, including behavior callers can depend on, such as edge cases, error behavior, ordering, and side effects.
- Give the public structure and signatures with the code's real names and types, so the spec and code stay aligned. Give values descriptive names, not single letters.
- Follow the format of the repo's existing specs, and keep it consistent within the file, such as writing every function heading the same way.

## Update
The code is the source of truth. Change only text whose described behavior no longer matches the code, at the level of the surrounding text. Leave everything else as written, including wording, names, order, and formatting.

## Compile
A created spec must compile without errors, since it will be the input when regenerating; fix any it reports. For an updated spec, fix errors in the text you changed, and report errors in the text you left alone.

Finish with a short summary, including any apparent bugs or surprising behavior you preserved in the spec.

# Draft a spec with the user

For `draft`, interview the user until the spec is settled, then write it. Do not write code.

## 1. Explore first
Read the relevant code, docs, and existing specs before asking anything, and for a revision, the spec and its code. Do not ask what the repo already answers, such as the language, location, conventions, or the types and APIs the code must use. State those findings briefly so the user can correct them.

## 2. Interview
Resolve the decisions that others depend on first, such as scope and the public interface, before behavior, edge cases, errors, and constraints. Ask in rounds of up to four independent questions, each with a recommended answer that is the simplest option consistent with the existing code. Trace each answer through the rest of the design, and press on vague answers, contradictions, and cases it leaves open. Prefer concrete examples, such as "what does `merge([], [])` return?", to abstract questions.

Ask only about decisions that change observable behavior or the public interface, or that the user has a stake in, such as a specific algorithm or library. Keep going until none remain, or the user says to stop.

## 3. Write the spec
Write it as `create` would, at the level the user gave. Without one, write it at high or medium level, with pseudocode only where the exact steps matter, such as an algorithm the user chose or a tricky edge case. Record every decision from the interview, and nothing the user did not agree to. For a revision, edit the spec as `update` does, changing only what the interview changed.

Compile the spec and resolve its errors with the user. If the user stopped the interview early, report the open decisions as errors. Finish with the spec's path and a short summary of the decisions it records.

# Change a spec's level

Rewrite the spec at the requested level so it generates the same observable behavior callers can depend on. Do not change the code. Compile it first; if it has errors, report them and stop, since equivalence cannot be guaranteed.

- **Going up:** remove detail that does not pin down behavior callers can depend on, such as helper functions, caching, and internal structure. Raise only the lines the new level makes unnecessary, so pseudocode stays pseudocode with some lines reworded as rules. Rewrite a whole block as prose only if the user asks. Keep every requirement, edge case, and public signature, and any detail that must stay exact, such as a specific algorithm or order.
- **Going down:** add the detail from the code the spec describes, as `create` would, and ask where the code is if the spec does not state it. Do not invent detail. If the code does not match the spec, report that and stop.

Compile the result and fix any new errors. Finish with a short summary of what was removed or added, which parts stayed below the new level, and any code behavior that is now pinned down.

# Simplify a spec

Rewrite the spec with simpler language and less text so it generates the same observable behavior callers can depend on. Compile it first; if it has errors, report them and stop.

Merge or remove repeated statements and detail the generate step would supply anyway. Keep every requirement and any detail that pins down behavior, such as steps, order, algorithms, signatures, and edge cases, and keep the author's structure and terms unless they cause the redundancy. Do not add requirements.

Compile the result and fix any new errors. Finish with a short summary of what you removed or merged.
