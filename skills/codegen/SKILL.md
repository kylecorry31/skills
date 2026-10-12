---
name: codegen
description: Generate or regenerate code in any language from pseudocode the user writes, check pseudocode for errors, change its level of detail, or write pseudocode for existing code.
disable-model-invocation: true
argument-hint: "[implement|check|update|level|create] <pseudocode file, or what to describe>"
---

Translate the user's pseudocode into code. The user makes the design decisions and the pseudocode records them; this skill is a compiler, not a designer. The pseudocode is the source of truth and the code is a build artifact of it, so the user can edit the pseudocode and regenerate. It is a file that may include natural language steps and structure such as `Class ABC: <interface>`. The code must do exactly what the pseudocode says, no more and no less, and the same pseudocode must produce the same code on every run.

# Commands

- `/codegen [implement] <pseudocode file>`: implement the pseudocode, or update the code if it is already implemented. `implement` is optional.
- `/codegen check <pseudocode file>`: compile the pseudocode and report its errors and warnings, or `No errors.`, without writing code.
- `/codegen update <pseudocode file>`: update the pseudocode to match the current code.
- `/codegen level <low|medium|high> <pseudocode file>`: rewrite the pseudocode at another level of detail.
- `/codegen create [low|medium|high] <what to describe>`: create pseudocode from existing code. Save it where the user says, otherwise next to the repo's other pseudocode files, or in `pseudocode/<short-description>.md` if there are none.

Tell the user about these commands if they invoke the skill without arguments or the arguments are unclear.

# Levels

The level says how much of the how the user cares about. The generator fills in what the level leaves open with the repo's existing patterns, otherwise standard practice, and never invents a choice that has neither.

- **Low:** the pseudocode is the implementation. Translate it step for step, keeping its functions, loops, conditions, order, and names. Supply only what the language requires, such as syntax, types, and imports.
- **Medium:** the pseudocode gives the algorithm, every step that decides behavior, and the generator fills in the mechanical code around it, such as plumbing, type conversions, error propagation, calls into existing APIs, and small helpers. Use this when boilerplate would hide the real algorithm.
- **High:** the pseudocode gives the components, their interfaces, and what each one does in terms of existing code, libraries, or standard algorithms, such as "map each `Row` to a `User`" or "cache results in the repo's `LruCache`". The generator writes the rest, including any algorithm the pseudocode does not name. Use this for code that is all boilerplate.

Mark a level with a `Level: <low|medium|high>` line directly under a heading. It applies to that heading's section and its subsections, until a subsection marks its own. A marker under the title sets the level for the whole file, and a file with no marker is medium.

Inside a code block, a `// Level: <low|medium|high>` comment line sets the level for the lines after it, until the next such comment or the end of the block. After the block, the section's level applies again.

# Generate code from pseudocode

## 1. Establish the target
Use the language and code location the pseudocode states. Otherwise infer them from the file's name and location, existing code, build files, and other pseudocode files.

## 2. Compile the pseudocode
Treat the pseudocode like source code and any problem with it like a compile error. Before writing any code, read the whole file and find every place where it cannot be cleanly implemented as written:
- **Ambiguous:** a reasonable reader could implement it two ways that behave differently.
- **Conflicting:** two parts contradict each other, or a step contradicts a stated goal.
- **Nonsensical:** it cannot work, such as an impossible step or a loop with no exit.
- **Unresolved:** it references something that does not exist.
- **Unimplementable:** it cannot be done in the target language or repo without deviating from the pseudocode.
- **Undecided:** filling the gap means making a choice the level leaves to the user, with no repo pattern or standard practice to follow.

Judge each place at the level that applies there:
- **Low:** anything left open that the language or context does not settle is an error.
- **Medium:** the steps that decide behavior belong to the user. A missing or open one is an error unless standard practice settles it. Fill everything else with the repo's patterns or standard practice.
- **High:** only the public interface and the behavior callers can depend on belong to the user. Fill everything else, including the choice of algorithm or data structure, with the repo's patterns or standard practice. A gap in observable behavior is an error unless standard practice settles it.

Conflicts and nonsensical steps are errors at any level.

A line may read at a higher level than its marked level, such as a natural language rule in low pseudocode. Judge it at the level it reads at: if it compiles there, report a warning and fill it in as that level would; otherwise it is an error.

Trace the values that flow between steps and functions. A degenerate output one step can produce, such as an empty list or a zero length, must be something the step that consumes it can handle.

Do not be nitpicky. Report an error only if two competent implementers would make different choices that the level leaves to the user, or the pseudocode cannot work. It is not an error when:
- the language, repo, or common practice leaves only one reasonable reading;
- the pseudocode gives signatures that require updating callers, tests, or other wiring;
- the pseudocode uses a term standard in its domain, such as a well-known formula, or one the repo already implements; use that meaning.

When unsure, prefer the standard or best-practice choice over an error, and report an error only when no such choice exists. Apply the same bar every run, so pseudocode that compiles once compiles again unless it changed.

Report every error and warning at once, in this form:

```
error: <what is wrong with the pseudocode>
  --> <pseudocode file>:<line>
   | <the pseudocode line, quoted>
   = needs: <the detail required to resolve it>

warning: reads at <level> level, but is marked <level>
  --> <pseudocode file>:<line>
   | <the pseudocode line, quoted>
   = fills: <how the code will fill it in>
```

If there are any errors, write no code and stop. Do not guess, pick a default, work around the problem, or generate partial output. Wait for the user to update the pseudocode, or offer to resolve the errors with them. Warnings alone do not stop generation.

For `/codegen check`, stop after compiling.

### Resolve errors with the user
If the user asks, go through the errors as questions, asking independent errors together and any that depend on an earlier answer afterward. Give the options for each, and recommend one only when the repo's existing code points to it. Then edit the pseudocode with the smallest change that records the user's answer, at the level of the surrounding text and in the user's own wording where possible.

After the last answer, compile again. Trace each changed rule through every step that uses its results, because a fix often exposes a case the original wording hid. When it is clean, continue with the original command.

## 3. Write the code
- Where the pseudocode gives steps, keep their order, conditions, and side effects. Where it names an algorithm or data structure, use that one.
- Keep the pseudocode's structure recognizable at every level: each function, component, and named step should map to identifiable code, so the user can read the pseudocode and code side by side.
- Add nothing the pseudocode does not call for, such as validation, logging, retries, caching, optimizations, abstractions, or configuration, unless the repo requires it of all such code.
- Fill gaps the same way each run: follow the repo's existing patterns, otherwise standard practice, and between equal options write the most direct code.
- Use the names and signatures the pseudocode gives, including parameter and return types, in the language's casing.
- If existing code uses different names or signatures, the pseudocode wins: change them and update the callers and tests that break. Ask first if the change touches public API, callers outside the repo, or code that differs from the pseudocode because of manual edits.
- If writing the code shows the pseudocode cannot be followed as written, such as needing a different signature, a case it leaves undefined, or a choice the level leaves to the user, do not choose for it. Stop and report it as a compile error.
- Do not restate the pseudocode in comments.

## 4. Regenerate after pseudocode changes
When code for the pseudocode already exists, update it with the smallest diff that matches the revised pseudocode. Keep the existing algorithm where the pseudocode is silent.

Compare the whole file to the code, not only the lines that changed, since the code may have drifted. If the code differs from the pseudocode in ways the change does not explain, such as manual edits, ask before overwriting them. Leave code that the pseudocode no longer describes untouched, and mention it in the summary.

## 5. Verify
Run the build and tests, then check each requirement in the pseudocode against the code. If a test fails because it encodes behavior the pseudocode changed, update the test. If a failure instead suggests the pseudocode's behavior is wrong, report it with a recommended change to the pseudocode, and change neither the pseudocode nor the test. Add tests for new or changed behavior when that fits the repo's conventions.

Finish with a short summary of every change in observable behavior from the old code, including edge cases, accuracy, and performance, separate from pure refactors, and of anything you could not verify. Repeat any warnings.

# Write or update pseudocode from existing code

For `create` and `update`, do not change the code. `create` takes the code to describe. `update` takes the pseudocode file, and the code is at the location it states. Ask if either is missing.

## Create
If the user gives a level, write the whole file at that level. Otherwise write it at medium level, going low for sections whose exact steps matter, such as a specific algorithm, a required order of operations, or a performance constraint, and high for sections that are all boilerplate. State the levels in the file.

The pseudocode must be good enough to regenerate the code with this skill:
- Describe what the code actually does, not what it ought to do, including behavior callers can depend on, such as edge cases, error behavior, ordering, and side effects.
- Give the public structure and signatures with the code's real names and types, so the pseudocode and code stay aligned. Give values descriptive names.
- Follow the format of the repo's existing pseudocode files, and keep it consistent within the file, such as writing every function heading the same way.

## Update
The code is the source of truth. Change only text whose described behavior no longer matches the code, at the level of the surrounding text. Leave everything else as written, including wording, names, order, and formatting.

## Compile
Created pseudocode must compile without errors or warnings, since it will be the input when regenerating; fix any it reports. For updated pseudocode, fix errors and warnings in the text you changed, and report those in the text you left alone.

Finish with a short summary, including any apparent bugs or surprising behavior you preserved in the pseudocode.

# Change the level

Rewrite the pseudocode at the requested level so it generates the same observable behavior callers can depend on. Do not change the code. Compile it first; if it has errors, report them and stop, since equivalence cannot be guaranteed.

- **Going up:** remove detail that does not pin down behavior callers can depend on, such as helper functions, caching, and internal structure. Raise only the lines the new level makes unnecessary, so steps stay steps with some lines reworded as rules. Rewrite a whole block as prose only if the user asks. Keep every requirement, edge case, and public signature, and any detail that must stay exact, such as a specific algorithm or order.
- **Going down:** add the detail from the code the pseudocode describes, as `create` would, and ask where the code is if the file does not state it. Do not invent detail. If the code does not match the pseudocode, report that and stop.

Update the stated levels, compile the result, and fix any new errors. Finish with a short summary of what was removed or added, which parts stayed below the new level, and any code behavior that is now pinned down.
