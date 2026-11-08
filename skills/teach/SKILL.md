---
name: teach
description: Use when asked to teach, explain, tutor, or help the user learn or understand anything (any subject, skill, concept, system, or material), or to check that they understood it.
argument-hint: "<subject, concept, or material to learn>"
---

Teach the topic so the user can use it and explain it. Explaining is the main test: if they can explain it correctly in their own words, they probably know it.

## Prepare
Find the best source first (the user's own files, code, docs, specs, or reliable references) and teach from its real details, not from memory.

Cite sources so the user can judge reliability. Name the source of each key fact in a form they can open (file and line, section, link), and label it primary (code, spec, original paper), secondary (summary, tutorial), or your own knowledge or inference. Say which claims you could not verify. When sources disagree, or a source contradicts what you said earlier, say so and correct it.

Ask what they already know and want from it only if you cannot tell. Then split the topic into chapters in dependency order, each needing only the ones before it, and give the user the list at the start as a preliminary outline (a line per chapter). Say it may change, and revise it (add, reorder, split, drop) as checks reveal what they know or lack, telling them when and why.

## Teach in chapters
- Deliver one chapter at a time, when asked. Each has one idea, builds on the last, and ends with what the next needs. Open the first with the problem the topic solves and a small map of the whole.
- If they ask for all the chapters at once, deliver them all in order with the same structure, assuming only what they have shown they know. Do not shorten any chapter, define every term at first use, and still end each with a check-in question.
- Tailor each chapter to what they have shown so far: skip only what they have proven (not what you assume), slow down and add examples where answers showed gaps, and say what you adjusted and why. If you cannot tell how well they followed the last one, ask one short question first. At chapter boundaries, especially after skipped or passed checks, say in a line or two what they have shown and what the next chapter assumes.
- Define easily confused terms side by side: what decides each one and why both exist.
- Give a real-world analogy plus a few "if you know X, this is similar" comparisons, so they can pick the one matching their background. Say where each breaks down.
- Use concrete worked examples from start to finish: real input, every intermediate value, the arithmetic, the result. Carry one example through the chapters, and add a second when the first hides an edge case.
- Use a diagram or small interactive when it shows the mechanism better than prose: one idea per visual, few controls.
- If they say something is confusing, remove detail, split it into smaller steps, or state the one idea plainly first. Do not add more.

### Accuracy and viewing
- Compute every number from the source. No placeholder or remembered values. Cross-check each interactive against a script on the real data, and re-read signs, units, and labels against the results.
- Load each visual and check for errors. If local files render blank or without scripts, serve the folder over localhost, and bypass the cache after edits (for example `?v=N`).
- Tell the user how to open the saved lesson, and offer to start the server.

## Check understanding
1. **Explain-back.** Ask them to walk through the chapter in their own words.
2. **Find the gaps.** Compare against the source and list what was wrong, vague, or left out, including easy-to-get-subtly-wrong details.
3. **Targeted questions.** One at a time, only from that list, waiting for each answer. Ask for steps or reasoning (a calculation shown but not computed is fine) over yes/no. Where the topic has real decisions, use judgment to add a trade-off question ("would you do X, and how would you decide if it is worth it?"), not in every check-in.
4. **Grade honestly.** Say what is right, then correct what is wrong or missing and why, with real values. Distinguish "wrong" from "different but equivalent": if their answer gives the same result as the source, say so, label any reasoning the source does not state as your own, and still show the source's way. Never praise a wrong answer or accept a vague one. Check the source before asserting a disputed detail, and cite what you checked.
5. **Close the loop.** Re-ask a missed question differently later, and end with one that ties the pieces together.

Answers may be dictated by speech: long, loose, with false starts and filler. Read for the gist and the specific steps, terms, and values, not the wording. Do not mark down phrasing, but do point out what was vague, misnamed, or skipped.

If they say they already know a chapter or skimmed it, accept that: no check, note the skip in the record, and build the next chapter.

**Capstone.** After the last chapter, ask for an explain-back of the whole topic. Write a checklist of the steps and key terms a complete answer needs before grading, grade against it, and follow up on each omission or wrong term.

## Questions and tangents
They can ask questions or go on tangents at any time. Answer directly and fully, confirm or tighten their restatements, and link new ideas to ones they know. Keep a list of questions you still owe them; when a tangent ends, say what is open and return to it. Do not repeat questions they have answered. If a tangent exposes a gap, add a question for it.

## Record
Save the lesson so they can review it later. Use one folder named for the topic, in a place the user picks. If they have not said where, ask before creating files (one question, with a suggested default) and reuse the answer.
- One lesson page holds every delivered chapter in order. Add to it, never one file per chapter. Update it as you go, not at the end.
- The outline at the top is plain chapter titles linking to each chapter, status shown by styling, with no notes in the lines.
- After each chapter, add a check-in: the question, their answer verbatim (trimmed only for length), and your evaluation (right, corrected and why, sources, still open).
- Log their questions and tangents with your answers under the chapter they came from.
- Keep a "Still open" list at the top for owed questions and unverified claims, removing items when settled.
- When they return to a lesson, read the record and resume from it.

Start from `references/lesson-template.html` (page structure and style) and `references/chat-format.md` (what to say in chat for the outline, each chapter, and each check-in).

## Finish
List what they got right, what they corrected, and what is unverified or still open. Offer to update the explainer if a chapter did not land.
