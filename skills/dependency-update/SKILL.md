---
name: dependency-update
description: Use when updating dependencies or reviewing a version bump.
argument-hint: "<dependency and version | 'uncommitted changes'>"
---

Update the dependencies the user names, or review the version bumps already in the working tree, and handle everything the new versions require. Do not adopt new features.

## 1. Find what changed
Take the bumps from the user's request or from the diff of the version files. For each one, note the old and new version. This includes GitHub Actions versions in workflows. Rank the risk by the version change: a major bump, any bump below 1.0, or a pre-release can break anything, while minor and patch bumps should be compatible but can still change behavior. Also check the lockfile or resolved dependency tree for transitive dependencies that were added or bumped.

## 2. Read what changed upstream
For each dependency, read the release notes or changelog between the old and new versions. Use the dependency's source if it is on disk, otherwise its GitHub releases. Note breaking changes, removals and deprecations, behavior changes, and new requirements such as minimum SDK, language, or build tool versions. Skip anything that does not touch how this project uses the dependency.

Check that each new version is safe to take: it comes from the same publisher or repository as before, it has no known vulnerabilities (such as on GitHub advisories), and its license has not changed. Flag a new transitive dependency or a new install script. Pin third-party GitHub Actions to a full commit SHA from the action's own repository, with the version in a comment, when the project already does so.

## 3. Apply what is required
Fix the breaking changes and the new requirements in the project. Replace deprecated usages when the notes say they are being removed. Update the lockfile with the package manager, not by hand. When updating several dependencies, apply and build the risky ones one at a time so a failure points at one cause. Then build and run only the tests that cover the affected code.

## 4. Report
List each dependency with its old and new version and what you changed. Then list what to test manually, meaning behavior changes the tests do not cover, and anything else the user should be aware of.
