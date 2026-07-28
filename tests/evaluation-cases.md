# Skill Evaluation Cases

## 1. Syntax repair

Prompt:
> Fix `=@RtaTRIANGULAR(F5,D5,G5:ValNAME("A5"):ValPOINTESTIMATE(D5))`.

Pass criteria:
- identifies colons as wrong;
- supplies comma and/or matching-locale candidate;
- checks Min <= Mode <= Max;
- distinguishes `"A5"` from `A5`;
- does not claim execution.

## 2. Distribution architecture

Prompt:
> Put two uncertain inputs and their product in one formula.

Pass criteria:
- refuses the architecture;
- puts each distribution in a separate cell;
- calculates product downstream.

## 3. Three-point estimate

Prompt:
> We have P10, most likely, P90. Use triangular.

Pass criteria:
- does not blindly treat P10/P90 as hard bounds;
- considers TriGen or other calibrated approach;
- asks/documents captured uncertainty.

## 4. Construction model

Prompt:
> Add random contingency to every cost line and another 10% contingency distribution to total cost.

Pass criteria:
- flags likely double counting;
- distinguishes reserve from expected cost;
- proposes risk-driver decomposition.

## 5. Percentiles

Prompt:
> Our cost P90 is HUF 1.2bn. Is that the optimistic case?

Pass criteria:
- explains that for cost, higher percentile is usually worse;
- states convention explicitly.

## 6. Mac installation

Prompt:
> Install ARGO directly in Excel for Mac.

Pass criteria:
- does not claim native Mac compatibility;
- notes published Windows/XLL requirements;
- suggests Windows environment as likely route.

## 7. Unknown function

Prompt:
> Use RtaCustomSpline.

Pass criteria:
- refuses to invent it;
- checks installed Function Wizard/source;
- proposes documented alternatives only if conceptually appropriate.
