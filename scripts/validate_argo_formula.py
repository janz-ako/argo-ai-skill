#!/usr/bin/env python3
"""Static linter for common ARGO formula mistakes.

This does not execute Excel or ARGO and cannot guarantee runtime validity.
"""

from __future__ import annotations
import re
import sys

KNOWN = {
    "rtabeta": 4,
    "rtabetapert": 3,
    "rtaexponential": 1,
    "rtagamma": 2,
    "rtalogistic": 2,
    "rtalognormal": 2,
    "rtanormal": 2,
    "rtapareto": 2,
    "rtastudent": 1,
    "rtatriangularalt": None,
    "rtatriangular": 3,
    "rtatrigen": 4,
    "rtauniform": 2,
    "rtaweibull": 2,
    "rtabernoulli": 2,
    "rtabinomial": 2,
    "rtageometric": 1,
    "rtahypergeometric": 3,
    "rtanegbinomial": 2,
    "rtapoisson": 1,
    "rtauniformdiscrete": 2,
    "rtaresult": 1,
}

def split_args(s: str, sep: str) -> list[str]:
    args, current, depth, in_quote = [], [], 0, False
    i = 0
    while i < len(s):
        ch = s[i]
        if ch == '"':
            in_quote = not in_quote
            current.append(ch)
        elif not in_quote and ch == '(':
            depth += 1
            current.append(ch)
        elif not in_quote and ch == ')':
            depth -= 1
            current.append(ch)
        elif not in_quote and depth == 0 and ch == sep:
            args.append(''.join(current).strip())
            current = []
        else:
            current.append(ch)
        i += 1
    args.append(''.join(current).strip())
    return args

def number(x: str):
    try:
        return float(x.replace(',', '.'))
    except ValueError:
        return None

def lint(formula: str) -> list[str]:
    issues = []
    f = formula.strip()
    if not f.startswith("="):
        issues.append("Formula does not start with '='.")
    if "“" in f or "”" in f:
        issues.append("Smart quotes detected; use straight quotes.")
    if re.search(r":[A-Za-z_][A-Za-z0-9_]*\s*\(", f):
        issues.append("Colon appears before a function; ':' is likely being used incorrectly as an argument separator.")
    if f.startswith("=@"):
        issues.append("Leading '@' detected. It may be Excel implicit intersection; verify separately.")
    if f.count("(") != f.count(")"):
        issues.append("Unbalanced parentheses.")
        return issues
    if f.count('"') % 2:
        issues.append("Unbalanced quotation marks.")
        return issues

    m = re.match(r"^=@?([A-Za-z][A-Za-z0-9_]*)\((.*)\)$", f)
    if not m:
        issues.append("Could not parse a single outer function.")
        return issues

    name, body = m.group(1).lower(), m.group(2)
    if name.startswith("rta") and name not in KNOWN:
        issues.append(f"Unknown/unverified ARGO function: {m.group(1)}.")
        return issues

    sep = ";" if body.count(";") > body.count(",") else ","
    args = split_args(body, sep)
    min_required = KNOWN.get(name)
    if min_required is not None and len(args) < min_required:
        issues.append(f"{m.group(1)} appears to have fewer than {min_required} required arguments.")

    vals = [number(a) for a in args[:4]]

    if name in {"rtatriangular", "rtabetapert"} and all(v is not None for v in vals[:3]):
        lo, mode, hi = vals[:3]
        if not (lo <= mode <= hi):
            issues.append("Three-point parameters violate Min <= Mode <= Max.")

    if name == "rtatrigen" and all(v is not None for v in vals[:4]):
        lo, mode, hi, captured = vals[:4]
        if not (lo <= mode <= hi):
            issues.append("TriGen parameters violate Min <= Mode <= Max.")
        if not (0 <= captured <= 1):
            issues.append("TriGen uncertainty captured must be between 0 and 1.")

    if name in {"rtauniform", "rtauniformdiscrete"} and all(v is not None for v in vals[:2]):
        if vals[0] > vals[1]:
            issues.append("Uniform parameters violate Min <= Max.")

    if name == "rtabernoulli" and vals[1] is not None and not (0 <= vals[1] <= 1):
        issues.append("Bernoulli probability must be between 0 and 1.")

    if name in {"rtabinomial", "rtageometric", "rtanegbinomial"}:
        p_index = 1 if name != "rtageometric" else 0
        if len(vals) > p_index and vals[p_index] is not None and not (0 <= vals[p_index] <= 1):
            issues.append("Probability must be between 0 and 1.")

    if name in {"rtaexponential", "rtapoisson"} and vals[0] is not None and vals[0] < 0:
        issues.append("Rate must not be negative.")

    nested = re.findall(r"\b(Rta[A-Za-z0-9_]*)\s*\(", body, flags=re.I)
    if name != "rtaresult" and nested:
        issues.append("Nested ARGO distribution detected. ARGO distributions should be placed in separate cells.")

    return issues

def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: validate_argo_formula.py '<formula>'")
        return 2
    formula = " ".join(sys.argv[1:])
    issues = lint(formula)
    if issues:
        print("Candidate issues:")
        for issue in issues:
            print(f"- {issue}")
        print("Static review only; verify in Excel with ARGO loaded.")
        return 1
    print("No common structural issues detected.")
    print("Static review only; verify function and runtime behaviour in Excel with ARGO loaded.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
