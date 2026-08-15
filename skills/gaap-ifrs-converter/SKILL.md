---
name: gaap-ifrs-converter
description: Use this skill to convert a trial balance from K-GAAP, Vietnamese Accounting Standards, Chinese Accounting Standards, or United States GAAP into a review-ready K-IFRS work product with reconciliation, difference analysis, and quantified profit and equity effects.
---

# GAAP-to-K-IFRS Conversion

## Inputs

1. A CSV or Excel trial balance containing account names and amounts.
2. Optional JSON supporting data for expected credit loss, leases, revaluation, development costs, defined-benefit obligations, and financial instruments.

## Run

```bash
gaap-ifrs convert \
  --input trial-balance.xlsx \
  --source-gaap K-GAAP \
  --extra adjustments.json \
  --out output
```

## Outputs

- `ifrs_financials.xlsx`: converted statement of financial position and income statement
- `reconciliation.xlsx`: mapping and adjustment reconciliation with an equity bridge
- `difference_analysis.md`: account-level and adjustment-level rationale, citation status, and quantified effects
- `impact_analysis.xlsx`: source-to-K-IFRS movements in assets, liabilities, equity, and profit
- `result.json`: machine-readable result

## Controls

- Account mapping and adjustment selection come from versioned rule data.
- Monetary effects are calculated by deterministic Python code.
- Every adjustment uses balanced double-entry entries.
- A citation may be inserted only from a lawful local corpus. If the paragraph is unavailable, label the basis as a curated summary that has not been verified against corpus text.
- An unmapped account or missing supporting input must be flagged for professional judgment; do not invent an amount.

The six implemented adjustment families are bounded examples, not a complete conversion methodology. Revenue recognition, impairment, consolidation, presentation, disclosures, and jurisdiction-specific transition decisions require additional analysis. Every output requires qualified accounting review.
