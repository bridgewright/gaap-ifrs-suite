---
name: gaap-standards-qa
description: Use this skill for questions about accounting-standard text, interpretation, practical application, or comparison across K-IFRS, K-GAAP, Chinese Accounting Standards, and Vietnamese Accounting Standards. Search the local corpus before making a standards claim and keep source text separate from interpretation.
---

# Grounded Accounting-Standards Analysis

## Required method

1. Search with `search_standards` before answering a standards question.
2. Retrieve the exact paragraph and, where necessary, adjacent context and application guidance.
3. For a comparison, search each accounting framework separately.
4. Distinguish verbatim source text, interpretation, practical implications, and cross-framework comparison.
5. State clearly when no relevant paragraph was found.

## Evidence boundary

- A statement about what a standard requires must be supported by returned source text and provenance.
- Interpretation may explain the source but must be labeled and must not introduce a new requirement.
- Preserve source-language quotations. Label any translation as unofficial and subordinate to the source text.
- If extraction is flagged, disclose that the text requires source verification.
- If retrieval is degraded to BM25 or the Model Context Protocol server is unavailable, disclose the operating mode.
- United States GAAP text is not included in the local corpus workflow. Do not substitute model memory for a missing source.

## Response structure

- **Source text:** a short verbatim paragraph with framework, standard, paragraph number, and source.
- **Interpretation:** a plain-language explanation tied to the cited paragraph.
- **Practical application:** include only when supported by retrieved application material or clearly labeled professional judgment.
- **Comparison:** cite independently retrieved text for every framework included.
- **Qualification:** state that the response is a grounded review draft, not accounting or audit advice.

For an ambiguous question, ask one focused question about framework, topic, or accounting party before searching. Never fabricate a citation, paragraph number, effective date, recognition condition, or quantitative threshold.
