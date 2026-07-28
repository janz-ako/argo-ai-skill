# Excel Locale and Formula Repair

## Argument separator

Excel commonly uses either:
- comma: `,`
- semicolon: `;`

Detect the convention from nearby formulas. Preserve it.

Comma:

```excel
=RtaTriangular(F5,D5,G5,ValName("A5"),ValPointEstimate(D5))
```

Semicolon:

```excel
=RtaTriangular(F5;D5;G5;ValName("A5");ValPointEstimate(D5))
```

## Colon is not an argument separator

In Excel, `:` normally creates a range. This is structurally wrong:

```excel
G5:ValName("A5"):ValPointEstimate(D5)
```

Use argument separators instead.

## Leading `@`

Modern Excel may insert `@` for implicit intersection or compatibility with dynamic arrays. It is not part of the ARGO function name.

Do not remove it automatically. Check:
- whether the formula was imported from an older workbook;
- whether Excel inserted it;
- whether the formula returns `#NAME?`, `#VALUE!`, or a scalarisation problem;
- whether nearby working ARGO formulas contain it.

## Literal text versus cell value

```excel
ValName("A5")
```

names the item literally `A5`.

```excel
ValName(A5)
```

attempts to use the value in cell A5. Use this only if the installed ARGO version accepts a cell-text argument and that is the user's intent.

## Decimal separator

Do not convert decimal commas or points without checking the workbook locale. Formula argument separators and decimal separators are related locale choices.

## Quotes

Use straight Excel-compatible quotes:

```excel
"Total Cost"
```

Smart quotes copied from documents may break formulas:

```text
“Total Cost”
```

Replace them with straight quotes.

## Formula repair response format

| Item | Content |
|---|---|
| Original | exact formula |
| Failure | exact structural/syntax issue |
| Candidate | corrected formula |
| Locale alternative | optional |
| Remaining check | what must be verified in Excel |
