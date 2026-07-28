# ARGO Formula Reference

This is a conservative reference based on the ARGO wiki. Function names are case-insensitive in Excel, but examples use readable PascalCase.

## Core structure

A distribution occupies its own cell:

```excel
=RtaNormal(Mean,StandardDeviation)
```

Optional Val parameters follow the required arguments:

```excel
=RtaNormal(Mean,StandardDeviation,ValName("Name"),ValPointEstimate(Base))
```

Use the workbook's argument separator: comma or semicolon.

## Continuous distributions documented by ARGO

| Function | Required parameters | Key constraints/use |
|---|---|---|
| `RtaBeta` | Alpha, Beta, Min, Max | Alpha and Beta positive; bounded interval |
| `RtaBetaPERT` | Min, Mode, Max | Smooth three-point estimate |
| `RtaExponential` | Rate | Rate positive; lower bound zero |
| `RtaGamma` | Shape, Scale | Both positive |
| `RtaLogistic` | Mean, Scale | Symmetric; scale controls spread |
| `RtaLognormal` | LN Mean, LN Standard Deviation | Parameters are in log space |
| `RtaNormal` | Mean, Standard Deviation | SD non-negative; unbounded unless truncated |
| `RtaPareto` | Scale, Shape | Both positive |
| `RtaStudent` | Degrees of Freedom | Heavy-tailed symmetric distribution |
| `RtaTriangularAlt` | Refer to ARGO Function Wizard | Wiki lists it but does not provide detail on the page |
| `RtaTriangular` | Min, Mode, Max | Require Min <= Mode <= Max |
| `RtaTriGen` | Min, Mode, Max, Uncertainty Captured | Captured proportion between 0 and 1 |
| `RtaUniform` | Min, Max | Require Min <= Max |
| `RtaWeibull` | Shape, Scale | Both positive |

## Discrete distributions documented by ARGO

| Function | Required parameters | Key constraints/use |
|---|---|---|
| `RtaBernoulli` | Impact, Probability | Probability 0–1; returns impact or zero |
| `RtaBinomial` | Trials, Probability | Trials non-negative integer; probability 0–1 |
| `RtaGeometric` | Probability | Probability 0–1 |
| `RtaHypergeometric` | Successes, Trials, Population | Integer/count consistency required |
| `RtaNegBinomial` | Successes, Probability | Successes count; probability 0–1 |
| `RtaPoisson` | Rate | Rate non-negative |
| `RtaUniformDiscrete` | Min, Max | Integer limits; Min <= Max |

## Val parameters documented by ARGO

### `ValLikelihood(probability)`

Sets occurrence probability. With probability below 1, non-occurrence is represented as zero.

```excel
=RtaBeta(2,5,0,1,ValLikelihood(0.75))
```

### `ValLowerBound(value)`

Truncates values below the bound.

```excel
=RtaNormal(0,1,ValLowerBound(-2))
```

### `ValName(text)`

Names a distribution or result in the control panel.

```excel
=RtaLognormal(10,1,ValName("Risk1"))
```

### `ValPointEstimate(value)`

Controls the value displayed in Excel outside/alongside simulation behaviour. It takes precedence over the global distribution return-value preference.

```excel
=RtaExponential(0.7,ValPointEstimate(0.7))
```

### `ValShift(value)`

Shifts all samples.

```excel
=RtaNormal(0,1,ValShift(100))
```

### `ValUpperBound(value)`

Truncates values above the bound.

```excel
=RtaNormal(0,1,ValUpperBound(2))
```

## Results

The wiki examples use:

```excel
=RtaResult(SUM(A1:A5),ValName("Total Cost"))
```

Use a result around an existing deterministic calculation rather than replacing the calculation logic with duplicated formulas.

## Architecture rule

Correct:

```excel
D2 = RtaNormal(0,1)
E2 = RtaUniform(0,5)
D4 = D2*E2
```

Incorrect pattern:

```excel
=RtaNormal(0,1)*RtaUniform(0,5)
```

ARGO documentation says every distribution must be defined in its own cell and arithmetic belongs in a separate cell.
