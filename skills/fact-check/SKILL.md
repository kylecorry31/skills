---
name: fact-check
description: Fact check content using trusted sources.
disable-model-invocation: true
---

1. If the user did not provide text, ask for it.
2. Identify each factual claim as an exact substring of the text.
3. Check every claim against the user's trusted sources, or authoritative online sources when none are provided. Try to identify multiple different sources for each claim. Use parallel subagents for independent groups of claims when useful.
4. Save the original text to `/tmp/fact-check-source-<source-slug>-<timestamp>.txt` and results to `/tmp/fact-check-result-<source-slug>-<timestamp>.json`. The results must validate against this JSON Schema:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "additionalProperties": false,
  "required": ["claims"],
  "properties": {
    "claims": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["claim", "fact_check_result", "evidence"],
        "properties": {
          "claim": {
            "type": "string",
            "description": "The verbatim text of the claim from the user's text."
          },
          "fact_check_result": {
            "type": "string",
            "enum": ["Accurate", "Inaccurate", "Partially Accurate", "Unverifiable"]
          },
          "fact_check_reason": {
            "type": "string",
            "description": "Optional commentary explaining why the evidence supports the fact-check result, in 1-4 sentences. Omit it when the source quotes are sufficient."
          },
          "evidence": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": false,
              "required": ["source", "quote"],
              "properties": {
                "source": {
                  "type": "string",
                  "description": "Source name or URL; prefer the URL."
                },
                "quote": {
                  "type": "string",
                  "description": "A concise, verbatim excerpt from the source."
                }
              }
            }
          }
        }
      }
    }
  }
}
```

5. Generate the visual report using this skill's packaged script:

```
python3 scripts/generate_report.py /tmp/fact-check-result-<source-slug>-<timestamp>.json /tmp/fact-check-source-<source-slug>-<timestamp>.txt --output /tmp/fact-check-report-<source-slug>-<timestamp>.html
```

Claims are matched using their exact text from the JSON. Evidence whose `source` is an HTTP(S) URL is shown as a clickable link. The link uses the verbatim `quote` as a browser text fragment, so supported browsers open the source at the highlighted excerpt.

6. Open the report in the user's default web browser
