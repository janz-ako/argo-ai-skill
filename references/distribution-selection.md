# Distribution Selection Guide

Choose from process knowledge and evidence, not visual preference.

| Situation | Candidate | Questions before use |
|---|---|---|
| Hard minimum, mode, hard maximum | Triangular | Are the bounds truly possible limits? |
| Expert three-point estimate, smoother centre | BetaPERT | Is the mode defensible? |
| Low/high are confidence bounds, not limits | TriGen | What proportion of uncertainty lies inside them? |
| All interval values equally plausible | Uniform | Is equal plausibility actually justified? |
| Symmetric aggregation of many small effects | Normal | Can negatives occur? Should bounds be added? |
| Positive multiplicative uncertainty | Lognormal | Are log-space parameters available and understood? |
| Event occurs or does not occur | Bernoulli | Is impact independent of occurrence? |
| Number of events in fixed interval | Poisson | Is a stable independent event rate plausible? |
| Failures/successes over trials | Binomial family | Are trials independent with stable probability? |
| Waiting time/reliability | Exponential, Gamma, Weibull | Does the physical process fit the distribution? |
| Heavy-tailed symmetric uncertainty | Student | Is tail risk supported by data? |

## Three-point estimates

Check:

```text
minimum <= mode <= maximum
```

Clarify whether minimum and maximum mean:
- absolute conceivable bounds;
- credible practical bounds;
- observed historical extrema;
- P10/P90-like confidence bounds;
- management targets.

These are not interchangeable.

## Point estimates

`ValPointEstimate` is a workbook display/base-case choice, not automatically:
- the mean;
- the median;
- the mode;
- the simulation's deterministic equivalent.

Choose it deliberately and document the choice.

## Correlation

Independence is an assumption, not a default truth. Common dependencies include:
- labour and material inflation;
- schedule delay and financing cost;
- sales price and absorption;
- construction cost and duration;
- exit yield and market rent growth;
- defects and rework duration.

Do not impose a correlation matrix merely to "make the model realistic." Every material relationship needs direction, magnitude rationale, and sensitivity testing.
