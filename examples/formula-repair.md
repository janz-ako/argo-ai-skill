# Example: Repairing an ARGO Formula

## Input

```excel
=@RtaTRIANGULAR(F5,D5,G5:ValNAME("A5"):ValPOINTESTIMATE(D5))
```

## Diagnosis

- `:` is an Excel range operator, not an ARGO optional-argument separator.
- Required order for triangular is Min, Mode, Max.
- The leading `@` may be Excel implicit intersection and should be considered separately.
- `"A5"` is literal text, not the value in cell A5.
- The formula separator must match the workbook locale.

## Candidate — comma locale

```excel
=RtaTriangular(F5,D5,G5,ValName("A5"),ValPointEstimate(D5))
```

## Candidate — semicolon locale

```excel
=RtaTriangular(F5;D5;G5;ValName("A5");ValPointEstimate(D5))
```

## Checks before acceptance

1. Confirm `F5 <= D5 <= G5`.
2. Confirm D5 is intended as both mode and point estimate.
3. Confirm literal name `"A5"` is desired; otherwise consider `ValName(A5)`.
4. Confirm the installed ARGO Function Wizard accepts the optional parameters.
5. Confirm whether Excel requires or automatically restores `@`.
