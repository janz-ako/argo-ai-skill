# Construction and Investment Modelling Patterns

## Recommended model layers

1. Assumptions and evidence
2. Uncertain input distributions
3. Quantities and deterministic calculations
4. Schedule/cash-flow timing
5. Financing
6. Revenue/exit
7. Tax
8. Decision outputs
9. Simulation statistics
10. Sensitivities and scenarios

## Construction cost

Model uncertain cost drivers at the level where evidence exists. Avoid placing independent triangular distributions on every line item when the uncertainty is mainly driven by common inflation or programme effects.

Possible decomposition:

```text
base quantity × uncertain unit rate
+ uncertain scope events
+ schedule-driven preliminaries
+ escalation
+ rework/defect impact
```

Do not randomise both a cost line and an aggregate contingency for the same risk unless contingency is deliberately modelled as a financing reserve rather than additional expected cost.

## Schedule

Use separate drivers for:
- design and permit;
- procurement lead time;
- factory production;
- site preparation;
- assembly;
- commissioning;
- sales/lease-up.

Connect duration to:
- preliminaries;
- financing interest;
- escalation exposure;
- revenue timing;
- liquidated damages where relevant.

## Revenue and absorption

Do not model selling price and sales volume independently without considering market linkage. Potential relationships:
- higher price reduces absorption;
- delayed completion changes market price and financing;
- incentives increase absorption but reduce net price.

## Financing

Model:
- draw timing;
- interest rate;
- commitment/utilisation fees;
- capitalised interest;
- debt ceiling;
- equity timing;
- peak funding;
- refinancing/exit date.

Make sure interest is based on simulated balances and dates rather than a separate random interest-cost percentage if the workbook already calculates it.

## NPV and IRR

Check:
- nominal cash flow with nominal discount rate;
- real cash flow with real discount rate;
- timing convention;
- terminal value;
- taxes;
- sign convention;
- annual versus monthly periods.

## Break-even output

For required rent or selling price:
- solve through the same cash-flow structure;
- specify target NPV, IRR, margin, or DSCR;
- avoid dividing a loss by units unless the relationship is genuinely linear;
- report the distribution of the required price and the probability it exceeds market benchmarks.

## Recommended outputs

- total cost;
- cost per net saleable square metre;
- completion month;
- peak cash requirement;
- project profit;
- margin;
- NPV;
- IRR;
- probability of loss;
- probability margin falls below hurdle;
- required price/rent;
- financing headroom;
- P10/P50/P90.

## Reconciliation

Explain why the simulation mean differs from the deterministic result. Common reasons:
- nonlinear formulas;
- asymmetric distributions;
- truncation;
- correlations;
- probability-of-occurrence events;
- timing effects;
- max/min logic;
- taxes or covenants;
- point estimates differing from distribution means.
