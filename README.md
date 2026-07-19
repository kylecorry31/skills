# Skills

I prefer to use agents as a way to review my work, create scripts, automate tasks, implement small low-risk changes (e.g., something very easy to review and trivial to implement), and write automated tests. I enjoy design and development, so I don't plan to add skills in that area. All skills should be human-in-the-loop and have justification for why it makes sense to use AI for it.

## Catalog

### code-review
A skill to help find bugs or deviations from standards.

**Intended use:** Be as thorough as possible in your manual review and testing process so you catch most of the issues, and then use this skill to have the agent catch things that were missed. It can be run on uncommitted changes, a branch, or against the last release (e.g., since tag 1.0.0). I recommend running this at least once with a good model before you release a changeset. I've had success in it identifying edge cases after a month of development and testing.

**Justification for AI use:** It adds another line of defense against bugs.

**How a human remains in the loop:** It does not replace manual review and does not fix any of the findings itself.

**Drawbacks:**
- Creates a false sense of security if no bugs are detected
- Overreliance can lessen knowledge about the codebase or let bugs slip through that would usually be caught by a thorough manual review
- Some of the findings may be false positives

Inspired by https://github.com/mattpocock/skills

### fact-check
A skill to help fact-check claims.

**Intended use:** It takes in text and optionally a list of authoritative sources and searches online to ensure claims made in the text are accurate (supported by authoritative sources). It generates a report that highlights each claim and provides an assessment of whether it is accurate - this shouldn't be trusted, so it links to snippets in the sources. Click on the highlight to make the tooltip stay open so you can click the links.

**Justification for AI use:** It automates the matching of authoritative sources to claims to help you avoid misinformation. This can be a very time consuming process for large bodies of text.

**How a human remains in the loop:** You should click each claim to view the tooltip, read the reason/quotes, and click the links to verify yourself (on most sites it will open the site with the quoted text highlighted).

**Drawbacks:**
- Does not reliably work for printed sources (e.g. books)
- Overreliance can lead to trusting the findings - be sure to at least read the source quotes and preferably click on the links for every claim you are fact checking
- It may hallucinate something as true/false when it is the opposite (regardless of what sources it finds)
- It may choose unreliable sources
- Increases AI-originated traffic to websites

### proofread
A skill to help proofread text content. It will modify the file you point it at if there are issues, so use version control.

**Intended use:** You write all of the content yourself and use it as a spelling/grammar fix. It should be VERY limited in what it touches and you should use a git diff viewer to make sure.

**Justification for AI use:** It adds another line of defense against spelling and grammar mistakes. Spelling and grammar checkers already exist, but this helps if you do your writing in a simpler text editor.

**How a human remains in the loop:** It should only make very minor spelling and grammar fixes which you can easily confirm via a git diff viewer. It will also make some recommendations for segments that are not very readable that you can act on. It should not rewrite any of your content or change your tone/style. It does not replace manual proofreading.

**Drawbacks:**
- It may decide to rewrite some of your content
- A git diff viewer is required to properly check the results since it edits the files
- The readability recommendations may be inaccurate or noise
- Overreliance could lead to lack of improvement in spelling and grammar skills
- While not the intent of the author, lack of perfect grammar can add a human touch which this skill may remove

Inspired by https://en.wikipedia.org/wiki/Wikipedia:Writing_articles_with_large_language_models

### translation-review
A skill to determine if a translation is accurate.

**Intended use:** Provide it with both the source and translated text and it determines if you should accept the translation as is or require changes. This is especially useful if you do not know the translated language and want to reduce the frequency of inaccurate translations in your project.

**Justification for AI use:** It adds a line of defense for mistranslated text, especially if the reviewer doesn't know the language and does not have time to machine translate each entry.

**How a human remains in the loop:** It presents a list of findings to you with reasons for why it is mistranslated. You decide which translations to reject and can use machine translation to confirm. 

**Drawbacks:**
- It may raise findings for valid translations which could lead the maintainer to reject something that should have been accepted
- It may miss improper translations which could lead the maintainer to accept something that is wrong (likely better than the alternative of just accepting all community translations)

## Support
I don't plan on providing support if it isn't working for you. I'll keep it up to date if I find it useful.
