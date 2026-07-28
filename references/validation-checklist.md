# ARGO Model Validation Checklist

## Formula integrity

- [ ] Every ARGO distribution is in its own cell.
- [ ] All parentheses and quotes balance.
- [ ] Workbook argument separator is preserved.
- [ ] No colon is used as a fake argument separator.
- [ ] Distribution function exists in the reference or installed Function Wizard.
- [ ] Parameter order is correct.
- [ ] Parameter domains are valid.
- [ ] Optional Val parameters are separate arguments.
- [ ] `ValName` uses intended literal/cell text.
- [ ] `ValPointEstimate` is deliberate.
- [ ] Bounds do not contradict distribution domain.

## Model logic

- [ ] Decision and thresholds are explicit.
- [ ] Units and signs are consistent.
- [ ] Uncertainty is neither omitted nor duplicated.
- [ ] Correlation assumptions are documented.
- [ ] Timing dependencies flow through cash flow.
- [ ] Taxes and financing use simulated drivers.
- [ ] No independent distributions are used for quantities derived from the same risk.
- [ ] Scenario assumptions are separated from random uncertainty where appropriate.
- [ ] Tail values are physically/economically plausible.
- [ ] The deterministic case can be reconciled.

## Output validity

- [ ] Outputs are named.
- [ ] Output formulas include the whole dependency chain.
- [ ] Percentile convention is explained.
- [ ] Probability thresholds use correct inequality direction.
- [ ] Sample count is sufficient for the reported precision.
- [ ] Sensitivities are interpreted as association, not causation.
- [ ] Expected gain/loss functions are verified in installed ARGO due to wiki ambiguity.

## Workbook quality

- [ ] Inputs, calculations, and outputs are visually separated.
- [ ] Assumptions include sources, dates, and owners.
- [ ] No formula references are broken.
- [ ] Named ranges are unique and meaningful.
- [ ] Workbook opens and recalculates with ARGO loaded.
- [ ] A clean copy is retained before edits.
