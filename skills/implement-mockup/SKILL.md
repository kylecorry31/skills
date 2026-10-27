---
name: implement-mockup
description: Implement or update one piece of a UI to match a drawing or mockup.
disable-model-invocation: true
metadata:
  status: experimental
argument-hint: "<mockup image or file> <which part of the UI to implement>"
---

Implement the named part of the UI shown in the mockup, creating it or updating the existing UI to match. Change only that part; ignore the rest of the mockup.

Build only the UI. Wire it to data and actions that already exist, but do not write business logic that is missing. Use placeholder data and no-op handlers for anything without a backing implementation.

Treat the mockup as a rough sketch of structure, content, and behavior, not a pixel spec. Use the project's existing components, theme, spacing, and conventions in place of the sketch's exact sizes, colors, fonts, and alignment, and adjust anything the sketch gets awkward or inconsistent with the rest of the app. If the sketch conflicts with the existing UI or leaves out a state that matters, such as empty, loading, or error, make a reasonable choice instead of asking.

If the project can run the UI, check that the result works and looks like the mockup's intent. Summarize what you built, each place you deliberately deviated from the mockup, and what is stubbed.
