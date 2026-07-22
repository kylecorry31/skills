---
name: code-review
description: Perform a thorough code review.
disable-model-invocation: true
---

Your goal is to review code changes and identify issues with them. Do not make any changes to the code.

# Process

## 1. Obtain the diff

If the user said what to use as the fixed point, use that. Otherwise, assume the merge base of the current branch and its base branch (usually `main`) is the fixed point. Assume uncommitted changes are included in the review unless the user says otherwise. If there is no base branch and no uncommitted changes, ask them to specify a fixed point.

Capture the diff command once and write it to a temporary file: `git diff <fixed-point>...HEAD`. Note the list of commits via `git log <fixed-point>..HEAD --oneline`. Read from the temporary file for the review rather than running `git diff` constantly.

## 2. Review

Delegate the review to parallel sub-agents where needed.

### Correctness

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

### Standards

Check the codebase for any docs, README files, or other files that describe coding standards. Check other code in the codebase for common or related patterns.

Look for these types of issues:
- Doesn't follow the codebase's conventions (styling, naming, architecture, testing, etc.)
- Violation of the codebase's documented standards
- Common code smells
- Overly complex or confusing code
- Lack of maintainability

## 3. Aggregate results

Take all of the findings and categorize them as either correctness or standards issues. If you find an issue, explain why it is an issue, and give it a priority. Sort the issues by priority. Do not nitpick. It is fine if there are no issues.

The overall summary should be brief and highlight the overall correctness and quality of the code changes. It shouldn't attempt to summarize the changes themselves, but rather be high-level commentary on the quality of the changes. If there are no issues, just say "No issues found."

The output should be a list of issues (if any) in the form:

```
## Overall
<High-level summary of the correctness and quality of the code changes>

## 1. [<High|Medium|Low>] [<Correctness|Standards>] <one-line description of the issue>

<Detailed explanation of why it is an issue>

## 2. ...
```
