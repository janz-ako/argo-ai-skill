# Example: Construction Cost Input

Assume:
- low unit cost in D5;
- base/mode in E5;
- high in F5;
- name in A5.

Comma locale:

```excel
=RtaBetaPERT(D5,E5,F5,ValName(A5),ValPointEstimate(E5))
```

Semicolon locale:

```excel
=RtaBetaPERT(D5;E5;F5;ValName(A5);ValPointEstimate(E5))
```

Downstream cost:

```excel
=QuantityCell*UnitCostDistributionCell
```

Do not place the multiplication inside the distribution cell.

## Review questions

- Are low/high hard bounds or confidence bounds?
- Is BetaPERT more suitable than Triangular?
- Is the same inflation risk already applied elsewhere?
- Does quantity also vary?
- Should unit cost correlate with schedule or other work packages?
