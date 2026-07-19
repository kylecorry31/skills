---
name: root-cause-analysis
description: Investigate bug reports, crashes, exceptions, stack traces, and regressions to establish repro steps, trace the evidence-backed cause-and-effect chain, and recommend immediate and systemic fixes without implementing them.
---

# Root-Cause Analysis

Investigate the reported failure before suggesting a fix. Separate what is observed from what is inferred, and trace the failure from the visible symptom through the immediate technical cause to the process, product, or design gap that allowed it.

This is an analysis skill only. Do not modify code, tests, configuration, or documentation unless the user explicitly asks for a separate implementation task.

## Process

### 1. Establish the problem

Collect or extract the following from the user's report:

- Expected behavior
- Actual behavior and user-visible impact
- Exact error message, exception type, and complete stack trace when available
- Reproduction steps, inputs, environment, versions, and frequency
- Recent changes, affected users, and relevant logs or telemetry

If critical information is missing, ask focused questions before drawing conclusions. If enough information exists to begin, proceed and list the missing information as investigation gaps.

Turn the report into a precise problem statement:

> When `<actor/input/context>` performs `<action>`, `<system/component>` produces `<observable failure>` instead of `<expected result>`.

Do not replace a specific symptom with a vague statement such as "the app is broken."

### 2. Confirm the issue

Use the available repository and runtime evidence to verify the report:

1. Locate the failing code path from the stack trace, error text, symbols, or affected feature.
2. Inspect callers, inputs, validation, state transitions, and boundary conditions around the failure.
3. Reproduce the issue when feasible. Use the user's steps first; create the smallest deterministic reproduction when they are incomplete.
4. Compare actual and expected behavior at the first point where they diverge.
5. Check whether the failure is deterministic, input-dependent, environment-dependent, or a regression.

Report the result as one of `reproduced`, `not reproduced`, `partially reproduced`, or `unable to test`, with the exact evidence and commands or steps used. A stack trace identifies where an error surfaced; it does not by itself prove where the invalid state originated.

### 3. Build the causal chain

Run an evidence-backed Five Whys analysis from the observed failure toward the earliest actionable cause. Five is a heuristic, not a stopping rule. Stop when the next "why" would be speculation, or when the chain reaches a controllable process, design, validation, or observability gap that explains recurrence.

For every link, ask:

- What specifically caused the previous condition?
- What evidence supports that relationship?
- Is this confirmed, strongly inferred, or still a hypothesis?
- What observation or experiment would disprove it?

Write the chain as a technical stack trace of causality:

```text
Observed failure
  <- immediate cause
  <- enabling condition
  <- upstream invalid input or state
  <- product/process/design gap
```

Branch the analysis when multiple independent causes are required. Do not force every incident into one linear root cause. Avoid blame-focused explanations such as "the user did it wrong"; translate them into the system condition that made the mistake possible, likely, or undetectable.

Use this distinction:

- **Symptom:** what the user or system observed.
- **Immediate cause:** the operation or condition that directly produced the failure.
- **Contributing cause:** a condition that made the immediate cause possible or more likely.
- **Root cause:** the earliest actionable system, design, process, or requirement gap whose correction would prevent recurrence.
- **Detection gap:** why the issue was not rejected, handled, or detected earlier.

### 4. Evaluate the root cause

Treat a proposed root cause as credible only when it explains the observed failure, fits the reproduction, and is supported by evidence. Validate it with counterfactual reasoning:

> If this condition were corrected while the other conditions stayed the same, would the reported failure be prevented?

If the answer is unknown, label the cause as a hypothesis and specify the smallest useful verification step. Record knowledge gaps instead of inventing facts. If the evidence only supports an immediate cause, say that the root cause remains unresolved.

### 5. Recommend fixes without implementing them

Recommend fixes in separate categories, tied to causal links:

- **Immediate mitigation:** reduce impact or prevent the known crash now.
- **Root-cause correction:** remove the upstream condition that creates the invalid state.
- **Input and state validation:** reject impossible, ambiguous, or unsafe data at the earliest appropriate boundary.
- **Error handling and recovery:** provide safe behavior when invalid state still occurs.
- **Observability:** add useful logs, metrics, assertions, diagnostics, or context at the point where the chain becomes uncertain.
- **Process or UX improvement:** clarify workflows, constrain choices, or add feedback when user action can create the invalid state.

For each recommendation, state which cause it addresses, expected effect, tradeoffs, and how to verify it. Do not claim that an exception guard alone fixes the root cause when it merely masks or contains the symptom.

## Output

Present the analysis in this order:

1. **Problem statement**
2. **Impact and scope**
3. **Reproduction status** with steps and environment
4. **Evidence examined** including relevant files, symbols, logs, and tests
5. **Causal chain** as a numbered table or indented chain; include evidence and confidence for every link
6. **Root cause** and why it is the root rather than an immediate symptom
7. **Open questions and verification plan**
8. **Potential fixes** grouped by mitigation, root-cause correction, validation, handling, observability, and UX/process

Use confidence labels `confirmed`, `strongly inferred`, or `hypothesis`. Keep facts, interpretations, and recommendations visibly separate.

## Example

For a map crash reported as `NaN`:

```text
Crash: map rendering receives NaN and fails
  <- projection divides by zero
  <- projection receives two identical points
  <- the saved route permits identical start and end points
  <- the input flow does not explain that distinct points are required
  <- validation and UX requirements do not encode or communicate that constraint
```

The immediate mitigation may be to handle `NaN` safely. The root-cause correction is to prevent or clearly reject identical points before saving, while preserving error handling and adding diagnostics so future invalid geometry is explainable.

## Method Notes

Five Whys is an iterative cause-and-effect technique. Its value is the evidence-backed chain, not the number five. It can stop earlier, continue further, or branch into multiple causes. Use a fishbone-style or tabular branch when a single chain would hide independent contributors. Treat unsupported answers as investigation gaps and avoid stopping at the first plausible symptom.
