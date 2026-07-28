---
name: ARGO Monte Carlo Skill
description: Build, review, repair, document, and explain Monte Carlo simulation models made with Booz Allen Hamilton's ARGO Excel add-in. Use for ARGO formulas, Rta distributions, RtaResult outputs, Val parameters, Op statistics, uncertainty modelling, P10/P50/P90 analysis, construction or investment risk models, and troubleshooting ARGO workbooks.
---

# ARGO Excel Monte Carlo Modelling

Use this skill whenever the task involves Booz Allen Hamilton's ARGO add-in for Microsoft Excel, formulas beginning with `Rta`, Val parameters such as `ValName`, or Op analysis functions.

## Non-negotiable rules

1. Treat the ARGO wiki and bundled references as the syntax authority.
2. Never invent an ARGO function, parameter, separator, or workbook feature.
3. Distinguish verified ARGO syntax from modelling advice and from Excel-version behaviour.
4. Put each ARGO probability distribution in its own cell. Perform arithmetic in downstream cells.
5. Preserve the workbook's locale, formula separator, sheet names, absolute references, named ranges, number formats, and units.
6. Do not assume the leading `@` is part of ARGO syntax. It may be Excel's implicit-intersection operator.
7. Do not use `:` to concatenate optional Val parameters. In Excel, `:` normally denotes a range. Val parameters are additional function arguments separated by the workbook's argument separator.
8. Validate parameter order and domains before proposing a formula.
9. Never confuse a deterministic point estimate with the distribution's expected value.
10. Do not claim a formula has run successfully unless it was executed in Excel with ARGO loaded.
11. ARGO is archived and no longer actively developed. Prefer conservative compatibility guidance.
12. ARGO's published requirements are Windows and legacy desktop Excel. Do not claim native Mac Excel compatibility.

## First response workflow

Determine the requested mode:

- **Build**: convert deterministic inputs into a simulation model.
- **Repair**: diagnose broken ARGO or Excel formulas.
- **Review**: audit a workbook's statistical logic, formulas, and outputs.
- **Explain**: translate a formula or simulation result into business language.
- **Design**: specify a model before editing a workbook.
- **Troubleshoot**: diagnose installation, loading, or add-in errors.

When a workbook or formula is supplied, inspect it before proposing changes. When evidence is incomplete, state exactly what remains unverified and give the safest candidate formula.

## Required modelling sequence

### 1. Define the decision

State:
- decision being supported;
- decision threshold;
- time horizon;
- outputs required;
- downside and upside measures;
- simulation trial count if known.

### 2. Map the workbook

Separate:
- assumptions;
- uncertain inputs;
- deterministic calculations;
- simulated outputs;
- dashboards and reports.

Identify units and signs. Costs, revenues, percentages, dates, durations, quantities, and probabilities must not be mixed silently.

### 3. Register uncertain inputs

For every uncertain input capture:
- variable name;
- workbook cell;
- unit;
- deterministic/base value;
- minimum;
- most likely or central value;
- maximum;
- chosen distribution;
- parameter rationale;
- point estimate;
- source/evidence;
- dependency or correlation;
- confidence level;
- owner/date.

Use [templates/assumption-register.md](templates/assumption-register.md).

### 4. Choose a distribution

Load [references/distribution-selection.md](references/distribution-selection.md).

Prefer:
- `RtaTriangular(min, mode, max)` for genuine hard bounds and a defensible mode;
- `RtaBetaPERT(min, mode, max)` for smoother three-point expert estimates;
- `RtaTriGen(min, mode, max, captured)` when low/high are confidence bounds rather than absolute bounds;
- `RtaUniform(min, max)` only when values in the interval are genuinely equally plausible;
- `RtaNormal(mean, sd)` only for approximately symmetric, unbounded uncertainty or with justified truncation;
- `RtaLognormal(lnMean, lnSD)` only when its log-space parameterisation is understood;
- `RtaBernoulli(impact, probability)` for an event that either occurs with a numeric impact or returns zero;
- discrete count distributions only when the process assumptions fit.

Do not use triangular merely because three cells exist.

### 5. Construct formulas

Read [references/formula-reference.md](references/formula-reference.md).

Generic verified pattern:

```excel
=RtaTriangular(Min,Mode,Max,ValName("Variable"),ValPointEstimate(Base))
```

The actual separator may be comma or semicolon depending on Excel locale. Preserve the workbook convention.

Correct architecture:

```excel
D2: =RtaNormal(0,1)
E2: =RtaUniform(0,5)
D4: =D2*E2
```

Do not put arithmetic around distributions within the same distribution cell.

### 6. Define outputs

Use `RtaResult(expression, optional Val parameters)` for decision outputs when supported by the workbook pattern.

Typical outputs:
- total development cost;
- completion date or duration;
- revenue;
- EBITDA;
- project profit;
- margin;
- NPV;
- IRR;
- peak cash requirement;
- minimum cash balance;
- required rent or selling price;
- covenant headroom.

Name outputs clearly with `ValName`.

### 7. Analyse results

Use verified Op functions and the ARGO UI. Read [references/op-functions.md](references/op-functions.md).

Default decision statistics:
- expected value;
- median;
- P10, P50, P90 with direction convention explicitly stated;
- probability of loss;
- probability of missing target;
- expected loss conditional/unconditional interpretation;
- minimum and maximum observed samples;
- sensitivity and correlation;
- deterministic-versus-simulation reconciliation.

For cost and duration, larger values are usually worse. For profit and NPV, smaller values are worse. Do not call P90 "downside" without defining the convention.

### 8. Validate

Run the checklist in [references/validation-checklist.md](references/validation-checklist.md).

At minimum verify:
- parameter order and domains;
- one distribution per cell;
- no duplicated uncertainty;
- no missing material uncertainty;
- no unsupported independence assumption;
- correlations are justified;
- point estimates match the deterministic case;
- outputs capture the full dependency chain;
- units and signs are consistent;
- tails are economically plausible;
- percentiles are interpreted correctly;
- formulas preserve locale;
- workbook opens without formula corruption.

### 9. Report

Return:
1. conclusion;
2. formula or cell changes;
3. assumptions and rationale;
4. validation findings;
5. unresolved issues;
6. business interpretation.

For workbook edits, provide a cell-change table with sheet, cell, old formula/value, proposed formula/value, and rationale.

## Formula-repair protocol

When given a broken formula:

1. Preserve the original verbatim.
2. Parse the outer Excel function and nested ARGO functions.
3. Identify likely Excel operators accidentally used as separators.
4. Check parentheses, quotes, argument order, locale separator, and cell-reference types.
5. Remove `@` only when evidence shows implicit intersection is causing the problem; otherwise explain it separately.
6. Produce a comma-locale and, when useful, semicolon-locale candidate.
7. Explain why the original fails.
8. Mark the result as "candidate—verify in Excel with ARGO" unless execution was actually confirmed.

Example repair:

```excel
Original:
=@RtaTRIANGULAR(F5,D5,G5:ValNAME("A5"):ValPOINTESTIMATE(D5))

Likely comma-locale candidate:
=RtaTriangular(F5,D5,G5,ValName("A5"),ValPointEstimate(D5))

Likely semicolon-locale candidate:
=RtaTriangular(F5;D5;G5;ValName("A5");ValPointEstimate(D5))
```

Also check whether the intended name is the literal `"A5"` or the text/value stored in cell A5. If the latter, use `ValName(A5)` if ARGO accepts the cell's text in that workbook.

## Construction and investment modelling rules

Load [references/construction-investment-patterns.md](references/construction-investment-patterns.md) for development models.

Pay special attention to:
- common-cause construction inflation;
- correlation among labour, materials, preliminaries, and schedule;
- schedule-to-finance-cost dependency;
- sales price and absorption dependency;
- VAT and tax scenarios;
- contingency as an output or risk allowance rather than an automatic extra random input;
- double-counting escalation;
- terminal value and exit-yield consistency;
- nominal/real discount-rate consistency;
- debt draw timing and interest capitalisation;
- break-even rent or price calculations.

## Additional resources

- [references/formula-reference.md](references/formula-reference.md): verified formula families and Val parameters.
- [references/distribution-selection.md](references/distribution-selection.md): distribution choice logic.
- [references/op-functions.md](references/op-functions.md): verified output-statistics functions.
- [references/excel-locale.md](references/excel-locale.md): commas, semicolons, `@`, and formula repair.
- [references/construction-investment-patterns.md](references/construction-investment-patterns.md): project-finance and construction applications.
- [references/troubleshooting.md](references/troubleshooting.md): installation and loading failures.
- [references/validation-checklist.md](references/validation-checklist.md): model QA.
- [references/source-index.md](references/source-index.md): provenance and limitations.
- [examples/](examples/): worked formula and modelling examples.
- [scripts/validate_argo_formula.py](scripts/validate_argo_formula.py): static formula linting; it does not execute Excel or ARGO.
