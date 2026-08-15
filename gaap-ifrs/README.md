# Conversion Engine

The package converts a supported local-GAAP trial balance into review-ready K-IFRS statements, reconciliation schedules, difference analysis, and impact analysis.

## Install and run

```bash
python -m pip install -e .
gaap-ifrs convert \
  --input trial-balance.xlsx \
  --source-gaap K-GAAP \
  --extra adjustments.json \
  --out output
```

The pipeline is `parse → map → adjust → build → reconcile → impact → report`.

## Scope

- Account mapping for K-GAAP, United States GAAP, Chinese Accounting Standards, and Vietnamese Accounting Standards
- Six adjustment families: expected credit loss, leases, property revaluation, development costs, defined benefits, and financial-instrument fair value
- Deterministic double-entry calculations and reconciliation
- Optional grounding of accounting-basis references against a lawful local corpus

When required supporting data is absent, the engine flags the item rather than estimating an amount. When source text is unavailable, it labels the accounting basis as a curated summary rather than presenting it as a verified quotation.

## Test

```bash
python -m pytest -q
```

The package tests parsing, mapping, all six adjustment families, statements, reconciliation, impact reporting, command-line behavior, validation, and citation fallback.

## Limitation

This package is a bounded prototype. It does not implement all recognition, measurement, presentation, disclosure, consolidation, tax, or transition requirements. Outputs require qualified professional review and do not constitute accounting advice or audit evidence.
