#!/usr/bin/env python3
"""Generate an HTML view of fact-checked text.

Usage:
    python3 generate_report.py RESULTS_JSON SOURCE_TEXT --output REPORT.html

Claims are matched as exact substrings of SOURCE_TEXT. The source is rendered
as text, not HTML, so source content cannot alter the generated document.
"""

from __future__ import annotations

import argparse
import html
import json
import sys
from pathlib import Path
from urllib.parse import quote, urlsplit, urlunsplit


RESULT_CLASSES = {
    "accurate": "accurate",
    "inaccurate": "inaccurate",
    "partially accurate": "partial",
    "unverifiable": "unverifiable",
}


def read_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"Could not read JSON file {path}: {error}") from error
    if not isinstance(value, dict) or not isinstance(value.get("claims"), list):
        raise ValueError("Fact-check JSON must be an object containing a 'claims' list")
    return value


def result_class(result: object) -> str:
    return RESULT_CLASSES.get(str(result).strip().lower(), "unverifiable")


def is_url(value: str) -> bool:
    parsed = urlsplit(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def text_fragment_url(source: str, quote_text: str) -> str:
    """Append a browser text fragment for the evidence excerpt."""
    excerpt = " ".join(quote_text.split())
    if not excerpt:
        return source

    parts = urlsplit(source)
    anchor = parts.fragment.split(":~:", 1)[0]
    fragment = f"{anchor}:~:text={quote(excerpt, safe='')}"
    return urlunsplit((parts.scheme, parts.netloc, parts.path, parts.query, fragment))


def evidence_html(evidence: object) -> str:
    if not isinstance(evidence, dict):
        return ""
    source = str(evidence.get("source", "")).strip()
    quote = str(evidence.get("quote", "")).strip()
    if not source and not quote:
        return ""

    source_text = html.escape(source)
    if is_url(source):
        linked_source = text_fragment_url(source, quote)
        source_html = (
            f'<a href="{html.escape(linked_source, quote=True)}" target="_blank" '
            f'rel="noopener noreferrer">{source_text}</a>'
        )
    else:
        source_html = source_text
    quote_html = f'<q>{html.escape(quote)}</q>' if quote else ""
    return f"<li><strong>{source_html}</strong>{quote_html}</li>"


def claim_tooltip(claim: dict) -> str:
    reason = claim.get("fact_check_reason")
    reason_html = ""
    if isinstance(reason, str) and reason.strip():
        reason_html = (
            f'<strong>Reason</strong><p class="reason">'
            f"{html.escape(reason.strip())}</p>"
        )

    evidence = claim.get("evidence", [])
    if not isinstance(evidence, list):
        evidence = []
    items = "".join(evidence_html(item) for item in evidence)
    if not items:
        items = "<li>No evidence supplied.</li>"
    return f'<span class="tooltip">{reason_html}<strong>Evidence</strong><ul>{items}</ul></span>'


def find_claim_ranges(source: str, claims: list[dict]) -> list[tuple[int, int, dict]]:
    matches: list[tuple[int, int, dict]] = []
    for claim in claims:
        text = claim.get("claim") if isinstance(claim, dict) else None
        if not isinstance(text, str) or not text:
            continue
        start = source.find(text)
        if start == -1:
            print(f"Warning: claim not found in source: {text!r}", file=sys.stderr)
            continue
        while start != -1:
            end = start + len(text)
            matches.append((start, end, claim))
            start = source.find(text, end)

    # Prefer longer claims at the same position and omit overlapping ranges.
    matches.sort(key=lambda match: (match[0], -(match[1] - match[0])))
    selected: list[tuple[int, int, dict]] = []
    end = -1
    for match in matches:
        if match[0] >= end:
            selected.append(match)
            end = match[1]
    return selected


def render_source(source: str, matches: list[tuple[int, int, dict]]) -> str:
    output: list[str] = []
    cursor = 0
    for start, end, claim in matches:
        output.append(html.escape(source[cursor:start]))
        claim_text = source[start:end]
        status = result_class(claim.get("fact_check_result", "Unverifiable"))
        label = html.escape(
            f"{claim_text}: {claim.get('fact_check_result', 'Unverifiable')}", quote=True
        )
        output.append(
            f'<mark class="claim {status}" tabindex="0" aria-label="{label}">'
            f"{html.escape(claim_text)}{claim_tooltip(claim)}</mark>"
        )
        cursor = end
    output.append(html.escape(source[cursor:]))
    return "".join(output)


def generate_html(source: str, results: dict) -> str:
    claims = [claim for claim in results["claims"] if isinstance(claim, dict)]
    rendered = render_source(source, find_claim_ranges(source, claims))
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Fact-check report</title>
<style>
body {{ background: #f7f7f5; color: #202124; font: 16px/1.6 system-ui, sans-serif; margin: 0; }}
main {{ margin: 2rem auto; max-width: 55rem; padding: 0 1rem; }}
.source {{ background: white; border: 1px solid #ddd; border-radius: .5rem; box-shadow: 0 2px 8px #0000000d; padding: 1.5rem; white-space: pre-wrap; word-break: break-word; }}
.claim {{ border-radius: .2rem; box-decoration-break: clone; -webkit-box-decoration-break: clone; cursor: help; padding: .08em .12em; position: relative; }}
.accurate {{ background: #b7e4c7; }}
.inaccurate {{ background: #f5b7b1; }}
.partial {{ background: #ffe49a; }}
.unverifiable {{ background: #d5d8dc; }}
.tooltip {{ background: #202124; border-radius: .4rem; color: white; display: none; font-size: .9rem; font-weight: normal; left: 0; line-height: 1.4; max-height: 60vh; max-width: min(32rem, 80vw); overflow-y: auto; padding: .75rem 1rem; position: absolute; text-align: left; top: 100%; width: max-content; z-index: 2; }}
.tooltip .reason {{ margin: .4rem 0 .75rem; }}
.tooltip ul {{ margin: .4rem 0 0; padding-left: 1.2rem; }}
.tooltip li + li {{ margin-top: .5rem; }}
.tooltip a {{ color: #9dd8ff; }}
.claim:hover .tooltip, .claim:focus-within .tooltip {{ display: block; }}
@media (max-width: 40rem) {{ main {{ margin: 1rem auto; }} .source {{ padding: 1rem; }} .tooltip {{ bottom: 1rem; left: 1rem; max-width: none; position: fixed; right: 1rem; top: auto; width: auto; }} }}
</style>
</head>
<body><main><h1>Fact-check report</h1><div class="source">{rendered}</div></main></body>
</html>
'''


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate an HTML fact-check report.")
    parser.add_argument("results_json", type=Path, help="Fact-check JSON file")
    parser.add_argument("source_text", type=Path, help="Original source text file")
    parser.add_argument("-o", "--output", type=Path, required=True, help="HTML output file")
    args = parser.parse_args()

    try:
        results = read_json(args.results_json)
        source = args.source_text.read_text(encoding="utf-8")
        args.output.write_text(generate_html(source, results), encoding="utf-8")
    except (OSError, ValueError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
