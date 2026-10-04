---
name: codegen
description: Generate or regenerate code in any language from a high-level spec of pseudocode, English, or structure, or write a spec for existing code.
disable-model-invocation: true
argument-hint: "[implement|check|update|simplify|level|create] <spec file, prompt, or what to describe>"
---

Generate code from a high-level spec. The spec is the source of truth and the code is a build artifact of it, so the user can edit the spec and regenerate. The spec is a prompt or a file and may mix pseudocode, English steps, and structure such as `Class ABC: <description or interface>`. Its detail can range from line-level pseudocode to a loose description of behavior (see Spec levels).

The code must do exactly what the spec says, and be idiomatic, readable, and performant for the target language and repo.

# Commands

- `/codegen [implement] <spec file or prompt>`: implement the spec, or update the code if it is already implemented. `implement` is optional.
- `/codegen check <spec file>`: compile the spec and report its errors, or `No errors.`, without writing code.
- `/codegen update <spec file>`: update the spec to match the current code.
- `/codegen simplify <spec file>`: rewrite the spec in simpler language without changing what it generates.
- `/codegen level <low|medium|high> <spec file>`: rewrite the spec at another level of detail. See Change a spec's level.
- `/codegen create [low|medium|high] <what to describe>`: create a spec from existing code, at the given level if any. Save it where the user says. Otherwise save it next to the repo's other specs, or in `specs/<short-description>.md` if there are none.

Tell the user about these commands if they invoke the skill without arguments or the arguments are unclear.

# Spec levels

A spec is written at one of three levels. Each level up leaves more of the how to the generator.

- **Low:** line-level pseudocode. It fixes the steps, their order, conditions, and side effects, plus the names, signatures, and structure of everything it mentions.
- **Medium:** pseudocode or English for the rules and algorithms that decide behavior, with names and signatures for the public interface. It leaves helper functions, caching, and how the code is split up to the generator.
- **High:** English description of what the code does, its public interface, and the rules callers can depend on. It leaves the algorithms to the generator.

A spec can mix levels, going lower only where the exact steps matter. Compile each part at the level it is written at.

# Generate code from a spec

## 1. Establish the target
Infer the language, package, and output location from context clues: the spec's file name and location, existing code and build files, other specs, and docs. Follow the conventions of the nearby code.

## 2. Compile the spec
Treat the spec like source code and any problem with it like a compile error. Before writing any code, read the whole spec and find every place where it cannot be cleanly implemented as written:
- **Ambiguous:** a reasonable reader could implement it two ways that behave differently.
- **Conflicting:** two parts contradict each other, or a step contradicts a stated goal.
- **Nonsensical:** it cannot work, such as an impossible step or a loop with no exit.
- **Unresolved:** it references something that does not exist.
- **Unimplementable:** it cannot be done in the target language or repo without deviating from the spec.

Resolve what you can from context before reporting anything. If the repo leaves only one reasonable reading, it is not an error. If it leaves more than one, such as the target language when the repo has several candidates, it is.

Judge each place at the level of detail the spec uses there. Line-level pseudocode leaves almost no room, so anything it leaves open that context does not settle is an error. A high-level description leaves the implementation open, so only report ambiguity that changes what the code does, not how it does it. Conflicts and nonsensical steps are errors at any level.

Trace the values that flow between steps and functions. A degenerate output one step can produce, such as an empty list or a zero length, must be something the step that consumes it can handle.

Do not be nitpicky. Report an error only if two competent implementers would produce observably different behavior, or the spec cannot work. Do not report missing detail that the language, repo conventions, or common practice settle. When unsure, it is not an error. Apply the same bar every run, so a spec that compiles once compiles again unless it changed.

If there are any errors, write no code. Report every error at once, in this form, and stop:

```
error: <what is wrong with the spec>
  --> <spec file or "prompt">:<line>
   | <the spec line, quoted>
   = needs: <the detail required to resolve it>
```

Do not guess, pick a default, work around the problem, or generate partial output. Wait for the user to update the spec, or to ask you to resolve the errors with them. Mention that option after the errors.

### Resolve errors with the user
If the user asks, go through the errors one at a time as questions. For each, ask what the spec should say, with a suggested answer the user can accept as is. They can also type their own. Then edit the spec with the smallest change that resolves the error, at the level of detail of the surrounding text. If the spec is a prompt rather than a file, show the revised spec instead.

After the last answer, compile again, since the edits may have introduced new errors. Trace each changed rule through every step that uses its results, because a fix often exposes a case the original wording hid. When it is clean, continue with the original command.

## 3. Write the code
- Where the spec gives steps, keep their order, conditions, and side effects. Where it names an algorithm or data structure, use that one. Do not transliterate line by line.
- Where the spec leaves the how open, choose the simplest approach that performs well at realistic scale.
- Use the classes, functions, names, and signatures the spec gives, in the language's casing. Signatures include parameter and return types. If existing code uses different ones, the spec wins: rename or change it and update the callers and tests that break. How much the spec pins down depends on its level of abstraction: a high-level spec leaves names, signatures, and structure to you, and a low-level spec fixes them. Do not add features, parameters, abstractions, or error handling it does not call for, unless the language or repo requires them.
- Do not restate the spec in comments.

## 4. Regenerate after spec changes
When code for the spec already exists, update it to match the revised spec with the smallest diff. Change behavior only where the spec calls for it, and keep the existing algorithm where the spec is silent.

Compare the whole spec to the code, not only the lines that changed, since the code may have drifted from the spec. If the existing code differs from the spec in ways the spec change does not explain, such as manual edits, ask before overwriting them.

Leave code that the spec no longer describes untouched, and mention it in the summary.

## 5. Verify
Run the build and existing tests when possible, then check each requirement in the spec against the code. If an existing test fails because it encodes behavior the spec changed, update the test to match the spec. If a failure instead suggests the spec's behavior is wrong, report it and do not change the spec or the test. Add tests for new or changed behavior in the spec when that fits the repo's testing conventions. Finish with a short summary of every change in observable behavior from the old code, including edge cases, accuracy, and performance, separate from pure refactors, and of anything you could not verify.

# Write or update a spec from existing code

For `create` and `update`, do not change the code. `create` takes the code to describe. `update` takes the spec, and the code is the location it states. Ask if either is missing.

## Create
The user may give a level (low, medium, or high). Without one, choose the level that best captures the functionality of the code, and leave out implementation details that do not affect it. If told to use a level, write the whole spec at that level, otherwise adjust the level to maintain the functionality of the code.

The spec must be good enough to regenerate or update the code with this skill:
- State the target language and the code's location.
- Describe what the code actually does, not what it ought to do, including behavior callers can depend on, such as edge cases, error behavior, ordering, and side effects.
- Give the structure and public signatures that other code depends on, with the code's real parameter and return types.
- Use the code's real names, in the language's casing, for the types, functions, and values the spec mentions, so the spec and code stay aligned. Give values descriptive names, not single letters.
- Follow the structure and format of the repo's existing specs, and keep it consistent within the file, such as writing every function heading the same way.
- Go below the chosen level only where the exact steps matter, such as a specific algorithm, a required order of operations, or a performance constraint.

## Update
The code is the source of truth. Make the smallest edit that brings the spec into alignment: change only text whose described behavior no longer matches the code, adding what the code now does and removing what it no longer does. Write each change at the level of detail of the surrounding spec. Leave everything else as written, including wording, names, order, and formatting.

## Compile
Compile the spec as described above. A created spec must produce no errors, since the same text will be the input when regenerating. Fix any it reports. For an updated spec, fix errors in the text you changed, and report errors in the text you left alone instead of editing it.

Finish with a short summary, including any apparent bugs or surprising behavior you preserved in the spec.

# Change a spec's level

Rewrite the spec at the requested level so it generates the same behavior. Compile it first. If it has errors, report them and stop, since equivalence cannot be guaranteed. Do not change the code.

- **Going up (for example low to medium):** remove detail that does not pin down behavior callers can depend on, such as helper functions, caching, and internal structure, and describe the rules in plainer terms. Keep every requirement, edge case, and public signature. Keep detail that must stay exact, such as a specific algorithm or a required order, and say in the summary which parts stayed below the new level.
- **Going down (for example high to medium):** add the detail from the code the spec describes, as `create` would, and ask where the code is if the spec does not state it. Do not invent detail. If the code does not match the spec, report that and stop, since the added detail would change the spec's meaning.

Compile the result and fix any new errors. Finish with a short summary of what was removed or added, so the user can check that nothing important was lost, and of any code behavior the spec did not state that is now pinned down.

# Simplify a spec

Rewrite the spec so it generates the same behavior with simpler language and less text. Compile it first. If it has errors, report them and stop, since equivalence cannot be guaranteed.

- Use plainer wording and shorter sentences.
- Merge or remove statements that repeat each other and detail that adds nothing the generate step would not supply anyway.
- Keep every requirement and any detail that pins down behavior, such as steps, order, algorithms, signatures, and edge cases. Do not add requirements.
- Keep the author's structure and terms unless they cause the redundancy.

Compile the result and fix any new errors. Finish with a short summary of what you removed or merged, so the user can check that nothing important was lost.
