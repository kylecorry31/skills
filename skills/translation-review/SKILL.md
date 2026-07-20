---
name: translation-review
description: Use when evaluating whether a translation is accurate.
---

Your goal is to review whether a translation is accurate. Do not make any changes to the source or translated text.

## Process

### 1. Obtain the translations

You should be given the source text and the translated text. If you are not given both, ask the user to provide them.

### 2. Review for accuracy

For each translation, compare it to the source text and check for the following types of issues:
- The meaning is changed or distorted
- Content is added that isn't in the source (e.g., extra phrases, opinions, embellishments)
- Content is omitted that IS in the source
- Tone is significantly altered (e.g., formal → casual or vice versa) in a way that changes user-facing meaning
- Placeholders/variables (e.g., `%s`, `%1$d`, `%2$s`) are missing, reordered incorrectly, or altered
- HTML tags or formatting present in source are removed or changed in a way that affects meaning
- The translation introduces region-specific idioms or cultural spin not implied by the source

The following are not considered issues:
- Natural grammatical restructuring required by the target language
- Pluralization differences due to language rules
- Articles/pronouns added because the target language requires them
- Word order changes due to target language syntax rules

### 3. Aggregate results

Take all of the findings and explain why each is an issue, and give each one a priority. Sort the issues by priority. Do not nitpick. It is fine if there are no issues.

The output should be a list of issues (if any) in the form:

```
## 1. [<High|Medium|Low>] <one-line description of the issue>

Source: <source text snippet or identifier>

Translated: <translated text snippet or identifier>

<Detailed explanation of why it is an issue>

## 2. ...
```
