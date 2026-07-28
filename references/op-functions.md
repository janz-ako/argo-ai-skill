# ARGO Op Functions

Op functions retrieve raw simulation samples or statistics from ARGO distributions/results.

Verified from the wiki:

| Function | Purpose |
|---|---|
| `OpData(distribution, orientation)` | Returns samples as row/column array |
| `OpAverage(distribution)` | Mean |
| `OpMedian(distribution)` | Median |
| `OpMode(distribution)` | Mode |
| `OpMin(distribution)` | Minimum observed sample |
| `OpMax(distribution)` | Maximum observed sample |
| `OpCount(distribution)` | Sample count |
| `OpPercentile(distribution, k)` | kth percentile; k between 0 and 1 |
| `OpPercentInterval(distribution, lower, upper)` | Fraction within inclusive interval |
| `OpCorr(a,b,type)` | Pearson if true/default; Spearman if false |
| `OpCorrMat(distributions,type)` | Correlation matrix |
| `OpCorrMatAdjusted(matrixDefinition)` | Nearest valid adjusted rank-correlation matrix |
| `OpCV(distribution)` | Coefficient of variation |
| `OpAveDev(distribution)` | Average absolute deviation from average |
| `OpKurt(distribution)` | Kurtosis |
| `OpFrequency(distribution,bins)` | Frequency by intervals |
| `OpExpGain(distribution)` | Expected positive gain measure described by ARGO |
| `OpExpLoss(distribution)` | Expected negative loss measure described by ARGO |
| `OpExpGainRatio(distribution)` | ARGO wiki wording is unclear; verify in Function Wizard |
| `OpExpLossRation(distribution)` | Wiki contains this spelling; verify exact installed function name |
| `OpExpValMargin(distribution)` | Difference between gain/loss ratio measures |
| `Op(distribution)` | Deprecated; use `OpData` |

## Percentile examples

```excel
=OpPercentile(ProjectProfit,0.10)
=OpPercentile(ProjectProfit,0.50)
=OpPercentile(ProjectProfit,0.90)
```

Use actual cell references or named ranges accepted by the workbook.

## Probability examples

Probability of loss:

```excel
=OpPercentInterval(ProjectProfit,-1E+99,0)
```

This is a modelling pattern, not a special ARGO probability function. Use a lower bound appropriate to the model rather than blindly copying `-1E+99`.

Probability of meeting a margin range:

```excel
=OpPercentInterval(ProjectMargin,0.05,1)
```

## Caution

The ARGO wiki has apparent typos or ambiguous descriptions in some expected gain/loss ratio entries. Do not silently "correct" the installed function name. Check Excel IntelliSense or the Function Wizard in the user's installed version.
