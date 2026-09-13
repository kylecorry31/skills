---
name: code-review
description: Perform a thorough code review.
disable-model-invocation: true
---

Your goal is to review code and identify issues with it. Do not make any changes to the code.

# Process

## 1. Obtain the code to review

There are two types of code reviews:
- **Diff review**: You are given a fixed point in the codebase and you review the changes made since that point.
- **Current state review**: You are given a snapshot of the codebase and you review the current state of the code.

If the user didn't specify which type of review they want:
- If they are on a branch that isn't `main`/`master`, have provided a fixed point, or have uncommitted changes, assume they want a diff review.
- If they are on `main`/`master` with no uncommitted changes, assume they want a current state review.

If provided with a link to a pull request, you can either check it out if it is in the same repo you are currently in and there are no uncommitted changes, or you can clone it to a temporary directory.

### Diff review
If the user said what to use as the fixed point, use that. Otherwise, assume the merge base of the current branch and its base branch (usually `main` or `master`) is the fixed point. Assume uncommitted changes are included in the review unless the user says otherwise. If there is no base branch and no uncommitted changes, ask them to specify a fixed point.

Capture the diff command once and write it to a temporary file: `git diff <fixed-point>...HEAD`. Note the list of commits via `git log <fixed-point>..HEAD --oneline`. Read from the temporary file for the review rather than running `git diff` constantly.

You are looking to identify issues with what changed, not what was already in the codebase, unless what changed impacts existing code.

### Current state review
Identify the paths/files of code you are tasked with reviewing. If the user didn't specify, confirm with them what they want to review.

## 2. Review

Launch at least 2 independent review subagents in parallel to conduct the code review. Pass each agent the diff/path to the diff file and one of the angles below. If there are multiple disconnected areas to review, you may spin up more than one 'correctness' review agent with a narrow focus on each area. Each returns its findings with `file`, `line`, a one-line `summary`, and a more detailed `description` about why it is an issue. Don't build, test, or lint the code since those can be assumed to all pass.

Once you launch the review agents, your only task it to wait for their completion so you can aggregate the results.

### Correctness

Use context clues to determine what correct means. That may be obtained by looking at commit history, comments, naming, documentation, or a user-provided description. If you can't figure out what the intent is, ask the user to clarify. If the user provided a work item/issue, look that up and extract the title, body, comments, etc.

Look for these types of issues:
- Runtime errors and unhandled exceptions
- Performance degradation
- Security vulnerabilities
- Lack of backward compatibility due to a missing migration (where applicable)
- Unintended side effects
- Incorrect logic/behavior
- Unhandled edge cases
- Concurrency issues (deadlocks, race conditions, etc.)
- Doesn't match the specification or intended behavior
- Tests (if included) are incorrect or won't fail if the code is broken

### Standards

Check the codebase for any docs, README files, or other files that describe coding standards. Check other code in the codebase for common or related patterns.

Look for these types of issues:
- Doesn't follow the codebase's conventions (styling, naming, architecture, testing, etc.)
- Comments that are misleading, incorrect, missing, or unnecessary
- Violation of the codebase's documented standards
- Common code smells
- Code that is more complex than it needs to be
- Confusing or unclear code
- Lacks maintainability

## 3. Aggregate results

Wait for all review agents to complete, deduplicate the findings, and assign them each a priority level.

Priority levels:
- **High**: The issue is a serious problem that must be addressed as soon as possible. It will likely cause significant impact if delivered as-is.
- **Medium**: The issue is a problem that should be addressed. It may cause some impact if delivered as-is.
- **Low**: The issue is a minor problem that should eventually be addressed. It is unlikely to cause much impact if delivered as-is.

If there are no issues, just say "No issues found."

If an issue is a nitpick, informational, or otherwise will not cause any noticeable impact, it must be left out of the report.


The output should be a list of issues (if any) sorted by priority descending in the form:

```
# Code Review Results

## 1. [<High|Medium|Low>] [<Correctness|Standards>] <one-line description of the issue>

<Detailed explanation of why it is an issue>

## 2. ...
```

If the user asks you to write the report to a file but doesn't specify a name, use the format `code-review-<timestamp>-<slugified-short-description>.md`.
