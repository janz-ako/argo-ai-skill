# Example: Project NPV Output

Keep uncertain inputs in dedicated cells. Let the workbook calculate monthly project cash flows in `CashFlow!B10:BI10`.

Illustrative output:

```excel
=RtaResult(NPV(DiscountRate,CashFlow!C10:BI10)+CashFlow!B10,ValName("Project NPV"))
```

This is an illustrative Excel cash-flow convention. Verify timing and whether Excel's NPV treatment matches the model.

Statistics:

```excel
=OpAverage(ProjectNPVCell)
=OpPercentile(ProjectNPVCell,0.10)
=OpPercentile(ProjectNPVCell,0.50)
=OpPercentile(ProjectNPVCell,0.90)
```

Probability of loss can be calculated with `OpPercentInterval` using a model-appropriate lower limit and zero as the upper limit.

## Interpretation

For NPV:
- P10 is a lower-value outcome;
- P90 is a higher-value outcome;
- probability below zero is the loss probability.

Always state that convention because cost outputs use the opposite intuitive downside direction.
