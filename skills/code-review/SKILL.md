---
name: code-review
description: Perform a thorough code review.
disable-model-invocation: true
---

Your goal is to review the diff and identify any issues in it. After gathering some information about the intended behavior and standards, spin off parallel sub-agents to review the diff as you see fit. Once all sub-agents have completed their reviews, aggregate the results and present them to the user in a clear and concise manner.

## Process

### 1. Obtain the diff

If the user said what to use as the fixed point, use that. Otherwise, assume the merge base of the current branch and its upstream (usually `main`) is the fixed point. Assume uncommitted changes are included in the review unless the user says otherwise. If there is no upstream and no uncommitted changes, ask them to specify a fixed point.

Capture the diff command once: `git diff <fixed-point>...HEAD` (three-dot, so the comparison is against the merge-base). Also note the list of commits via `git log <fixed-point>..HEAD --oneline`.

### 2. Review for correctness

Use context clues to determine what correct means. That may be obtained by looking at commit history, comments, naming, or a user-provided description. If you can't figure out what the intent is, ask the user to clarify. If the user provided a GitHub issue, look that up with `gh issue view <issue-number>` and extract the title and body.

Look for these types of issues:
- Runtime errors and unhandled exceptions
- Performance degradation
- Security vulnerabilities
- Lack of backwards compatibility with missing migration (where applicable)
- Unintended side effects
- Incorrect logic/behavior
- Unhandled edge cases
- Doesn't match the specification or intended behavior

You should identify what it means to be correct (e.g., the specification/intended behavior) before spinning off sub-agents, and pass the details to them.

### 3. Review for standards compliance

Check the codebase for any docs, readmes, or other files that describe coding standards. Check other code in the codebase for common or related patterns.

Look for these types of issues:
- Doesn't follow the codebase's conventions (styling, naming, architecture, testing, etc.)
- Violation of the codebase's documented standards
- Common code smells
- Overly complex or confusing code
- Lack of maintainability

You should identify what the standards are before spinning off sub-agents, and pass the details to them.

### 4. Aggregate results

Take all of the findings and categorize them as either correctness issues or standards issues. If you find an issue, explain why it is an issue, and give it a priority. Sort the issues by priority. Do not nitpick. It is fine if there are no issues.

The output should be a list of issues (if any) in the form:

```
## 1. [<High|Medium|Low>] [<Correctness|Standards>] <one-line description of the issue>

<Detailed explanation of why it is an issue>

## 2. ...
```
