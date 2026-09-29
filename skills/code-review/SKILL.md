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

Capture the diff once and write it to a temporary file: `git diff -U1 -w -M <fixed-point>` (minimal context, whitespace ignored, renames detected; agents can open the file for more context). This compares the working tree to the fixed point, so it includes uncommitted changes (use `git diff <fixed-point>...HEAD` instead if the user asked to exclude them). If the fixed point is the merge base, resolve it first with `git merge-base <base> HEAD`. `git diff` skips untracked files, so list them with `git ls-files --others --exclude-standard` and append each with `git diff --no-index /dev/null <file>`.

Exclude files that don't need review (lock files, generated code, vendored dependencies, minified files, snapshots, binaries, deleted files, pure renames/moves, large data files). For large new files (data, fixtures), don't include their contents; list their name and size instead. Note the list of commits via `git log <fixed-point>..HEAD --oneline` and the size of the diff via `git diff --stat <fixed-point>`. Read from the temporary file for the review rather than running `git diff` constantly.

You are looking to identify issues with what changed, not what was already in the codebase, unless what changed impacts existing code.

### Current state review
Identify the paths/files of code you are tasked with reviewing. If the user didn't specify, confirm with them what they want to review.

## 2. Review

Scale the review to the size of the change:
- **Small** (roughly under 300 changed lines in a few files): review it yourself in a single pass covering both angles below. Don't launch subagents.
- **Medium**: launch 2 independent review subagents in parallel, one per angle below. Pass each the path to the diff file.
- **Large** (roughly over 1500 changed lines, or multiple disconnected areas): split the 'correctness' angle into one agent per area (group by directory/feature), each given its own diff file. Write one per area with the same command and exclusions as above, limited to that area's paths (`git diff -U1 -w -M <fixed-point> -- <paths>`), so no agent pays to read another area's changes. Use at most 4 correctness agents: merge small areas, and split an area over roughly 1000 changed lines by file rather than by feature. The 'standards' agent does not get the full diff; give it the `git diff --stat` output, the file list, and the diff file path, and tell it to read only the hunks of files that look off-convention.
- **Huge** (roughly over 5000 changed lines after exclusions): don't review everything. Tell the user the size and offer to review a subset instead (a directory, or the highest-risk files such as auth, security, concurrency, migrations, and high-churn files). Proceed only once they choose.

Give the subagents these instructions:
- Read the diff first, then only the code needed to verify a suspicion (the full changed file, its callers, or the definitions it uses). Don't survey the rest of the codebase.
- Only report issues you are confident are real and would have a noticeable impact. Drop nitpicks and speculation instead of reporting them.
- Return findings with `file`, `line`, a one-line `summary`, and a `description` (2-3 sentences) about why it is an issue. Don't restate the diff or describe code that is fine.
- Budget: read at most ~15 files beyond the diff. Use grep to find callers and definitions instead of reading whole files.
- Report at most the 10 highest-confidence findings.
- Write findings to a file (path given by you) and return only that path and a count of findings, in the structured form above.
- Don't build, test, or lint the code since those can be assumed to all pass.
- The 'standards' agent doesn't need deep reasoning, so run it on a smaller/faster model.
- Run the 'correctness' agents on a smaller/faster model only if you judge the change simple (mechanical edits, renames, config, docs, boilerplate, or straightforward logic with no concurrency, security, or data-migration concerns). Otherwise use the default model.

Once you launch the review agents, your only task is to wait for their completion so you can aggregate the results.

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

Check the root-level docs (README, CONTRIBUTING, CLAUDE.md/AGENTS.md, lint/style configs) for coding standards. Compare against a few sibling files next to the changed code (not the whole codebase) for common or related patterns.

Look for these types of issues:
- Doesn't follow the codebase's conventions (styling, naming, architecture, testing, etc.)
- Comments that are misleading, incorrect, missing, or unnecessary
- Violation of the codebase's documented standards
- Code that is more complex, confusing, or duplicated than it needs to be, or that reimplements something that already exists in the codebase

## 3. Aggregate results

Wait for all review agents to complete, deduplicate the findings, and assign them each a priority level. Read the findings files the agents wrote. Trust the agents' findings; only re-read code to resolve a conflict between agents or when a finding is unclear.

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
