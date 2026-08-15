# Conversion Examples

Each directory contains a synthetic source trial balance, supporting adjustment data, and generated outputs for one accounting framework. Regenerate the examples with:

```bash
python3 examples/build_examples.py
```

| Directory | Source framework | Demonstrated behavior |
| --- | --- | --- |
| `kgaap/` | K-GAAP | All six adjustment families and the resulting equity bridge |
| `usgaap/` | United States GAAP | Mapping and selected measurement differences, including an expected-credit-loss reversal in the synthetic case |
| `vas/` | Vietnamese Accounting Standards | Mapping and a newly recognized expected-credit-loss allowance in the synthetic case |
| `cas/` | Chinese Accounting Standards | Mapping and selected cost-model and recognition differences |

Inputs are `input_trial_balance.csv` and `input_adjustments.json`. Outputs include converted statements, reconciliation, impact analysis, difference analysis, and a machine-readable result.

These are representative synthetic scenarios, not company records. Numerical validation against a real transition requires an authorized source trial balance and the corresponding IFRS 1 transition reconciliation.
