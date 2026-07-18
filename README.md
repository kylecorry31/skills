# Skills

I prefer to use agents as a way to review my work, create scripts, automate tasks, implement small low-risk changes (e.g., something very easy to review and trivial to implement), and write automated tests. I enjoy design and development, so I don't plan to add skills in that area.

## Catalog

### code-review
A skill to help find bugs or deviations from standards. 

The intended use is to be as thorough as possible in your manual review and testing process so you catch most of the issues, and then use this skill to have the agent catch things that were missed.

It can be run on uncommitted changes, a branch, or against the last release (e.g., since tag 1.0.0).

I recommend running this at least once with a good model before you release a changeset. I've had success in it identifying edge cases after a month of development and testing.

Inspired by https://github.com/mattpocock/skills

### fact-check
A skill to help fact check claims.

The intended use is to take in text and optionally a list of authoritative sources and search online to ensure claims made in the text are accurate (supported by authoritative sources). It generates a report that highlights each claim and provides an assessment of whether it is accurate - this shouldn't be trusted, so it links to snippets in the sources.

Click on the highlight to make the tooltip stay open so you can click the links.

### proofread
A skill to help proofread text content. It will modify the file you point it at if there are issues, so use version control.

The intended use is for you to write all of the content yourself and use it as a spelling/grammar fix. It should be VERY limited in what it touches, but I recommend using a git diff viewer to make sure.

Inspired by https://en.wikipedia.org/wiki/Wikipedia:Writing_articles_with_large_language_models

### translation-review
A skill to determine if a translation is accurate.

The intended use is for you to provide it with both the source and translated text and determine if you should accept the translation as is or require changes. This is especially useful if you do not know the translated language and want to reduce the frequency of inaccurate translations in your project.

## Support
I don't plan on providing support if it isn't working for you. I'll keep it up to date if I find it useful.
