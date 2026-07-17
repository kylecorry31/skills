---
name: fact-check
description: Fact check content using authoritative sources.
disable-model-invocation: true
---

Your goal is to fact-check claims made in text content using authoritative sources and present the results to the user in a way that lets them easily verify the claims themselves. You must not make any changes to the text content itself.

# Process

## 1. Obtain the text to fact check
If the user did not provide text, ask for it.

If the user provided a file path, read the text from that file.

Save the verbatim original text to `/tmp/fact-check-source-<source-slug>-<timestamp>.txt`. If the user specified a specific section of a file, save only that section. 

## 2. Identify factual claims
Identify each factual claim as an exact substring of the text. A claim is a statement that can be verified as true or false.

## 3. Fact-check each claim
Check every claim against the user's authoritative sources, or authoritative online sources when none are provided. Try to identify multiple different sources for each claim.

Extract verbatim quotes from the sources that support or refute the claim. Retain the source URLs.

Use parallel subagents for independent groups of claims when useful.

## 4. Generate a JSON report of the fact check results

Save the results to `/tmp/fact-check-result-<source-slug>-<timestamp>.json`. The results must validate against this JSON Schema:

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

## 5. Generate a visual report
Generate the visual report using this skill's packaged script:

```
python3 scripts/generate_report.py /tmp/fact-check-result-<source-slug>-<timestamp>.json /tmp/fact-check-source-<source-slug>-<timestamp>.txt --output /tmp/fact-check-report-<source-slug>-<timestamp>.html
```

Claims are matched using their exact text from the JSON. Evidence whose `source` is an HTTP(S) URL is shown as a clickable link. The link uses the verbatim `quote` as a browser text fragment, so supported browsers open the source at the highlighted excerpt.

## 6. Open the report
Run a command to open the report in the user's default web browser.
