# GAAP–IFRS Suite

**A deterministic conversion engine and grounded retrieval service for local generally accepted accounting principles and Korean International Financial Reporting Standards.**

The suite addresses two related tasks: converting a trial balance from a supported local accounting framework into a review-ready K-IFRS work product, and retrieving the exact accounting-standard paragraphs that support professional analysis. The conversion engine and retrieval service are independent, but they share a central design rule: calculations and citations must not be invented by a language model.

This is an independent portfolio project based on public information. It is not affiliated with or endorsed by PwC, Samil PwC, the Korea Accounting Standards Board, the IFRS Foundation, or any other standard setter.

## Components

| Component | Responsibility | Primary control |
| --- | --- | --- |
| Conversion engine | Maps trial-balance accounts, applies six supported measurement adjustments, produces financial statements, and explains profit and equity effects | Double-entry reconciliation and deterministic adjustment rules |
| Standards retrieval service | Searches a locally built corpus and returns source paragraphs through a Model Context Protocol server | Verbatim citation, source metadata, and explicit fallback states |

The conversion engine supports K-GAAP, United States GAAP, Chinese Accounting Standards, and Vietnamese Accounting Standards as source frameworks. The public repository does not distribute accounting-standard text. Users must supply material they are legally entitled to use and build the corpus locally.

## Architecture

```text
trial balance + supporting data             licensed source documents
              │                                       │
              ▼                                       ▼
 parse → map → adjust → reconcile          ingest → segment → index
              │                                       │
              ├── financial statements                └── BM25 / vector / fusion
              ├── reconciliation                             │
              └── impact analysis                            ▼
                                                   MCP citation response
```

The language model is used, when appropriate, to interpret a user's question and explain retrieved evidence. Account mapping, journal entries, balance checks, monetary effects, document provenance, and citation text are controlled by code.

## Installation

Python 3.11 or later is required.

```bash
git clone https://github.com/bridgewright/gaap-ifrs-suite.git
cd gaap-ifrs-suite
python -m pip install -e .
python -m pip install -e ./gaap-ifrs
```

For Codex:

```bash
codex plugin marketplace add bridgewright/gaap-ifrs-suite
codex plugin add gaap-ifrs-suite@gaap-ifrs-suite
```

For Claude Code:

```bash
claude plugin marketplace add bridgewright/gaap-ifrs-suite
claude plugin install gaap-ifrs-suite@gaap-ifrs-suite
```

## Conversion Example

```bash
gaap-ifrs convert \
  --input examples/kgaap/input_trial_balance.csv \
  --source-gaap K-GAAP \
  --extra examples/kgaap/input_adjustments.json \
  --out output
```

The engine supports six bounded adjustment families: expected credit loss, leases, property revaluation, development costs, defined-benefit obligations, and financial instruments. It does not perform an unrestricted accounting conversion.

## Retrieval Service

After building a lawful local corpus, start the Model Context Protocol server:

```bash
python -m gaap_standards_mcp
```

Without a vector model, the service falls back to BM25 retrieval. Without a valid corpus, it fails explicitly and provides setup guidance rather than returning unsupported answers. See [corpus/README.md](corpus/README.md) for the data boundary.

## Evaluation

```bash
python -m pytest -q
cd gaap-ifrs && python -m pytest -q
```

The original evaluation contained 177 automated tests: 47 conversion tests and 130 retrieval, citation, ingestion, and fallback tests. Full-corpus checks were run locally against 10,922 paragraphs across four accounting frameworks. The copyrighted corpus is not included in this repository; public continuous integration uses synthetic fixtures for code paths that require text.

Evaluation covers parsing, mapping, six adjustment families, double-entry reconciliation, citation fidelity, segmentation boundaries, hybrid retrieval, Model Context Protocol tools, missing-model fallback, and corpus-manifest validation.

## Limitations

- Outputs are review drafts, not accounting advice, audit evidence, or financial statements suitable for issuance.
- Adjustment logic is intentionally bounded and does not represent all recognition, measurement, presentation, or disclosure requirements.
- United States GAAP source text is not included in the retrieval corpus workflow.
- Retrieval quality depends on the lawfulness, completeness, version, and extraction quality of the user's local source documents.
- Accounting standards and interpretations change; source vintage must be controlled by the user.

## Licensing and Source Rights

Original software is licensed under the MIT License. Accounting standards, translations, source documents, trademarks, and other third-party material are excluded. The IFRS Foundation states that integrating IFRS content into products and services requires an appropriate license. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) before building a corpus.
