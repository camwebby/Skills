# Nine-Dimension Scorecard

Use this scorecard after the six-stage pipeline. Score each dimension 0-10, multiply by weight, and explain evidence quality.

## Dimensions and Weights

| Dimension | Weight | Measures |
|---|---:|---|
| Problem severity | 15% | urgency, frequency, cost of inaction, workaround pain |
| Market size | 12% | enough reachable demand for the intended business type |
| Market timing | 10% | why now, tailwinds, trigger events, adoption readiness |
| Competitive moat | 12% | defensibility, differentiation, switching costs, proprietary access |
| Unit economics | 15% | pricing, gross margin, CAC/payback plausibility, LTV durability |
| Founder-market fit | 8% | access, credibility, insight, network, execution edge |
| Technical or operational feasibility | 10% | buildability, data dependencies, workflow complexity, support burden |
| GTM clarity | 10% | ICP clarity, channel access, sales motion, first 100 customers |
| Risk profile | 8% | likelihood and severity of kill risks |

## Scoring Rubric

Use whole or half points. Do not score above 7 without medium or strong evidence.

| Score | Meaning |
|---:|---|
| 0-2 | unsupported, confused, contradicted, or structurally weak |
| 3-4 | plausible but mostly assumption-driven |
| 5-6 | some encouraging evidence, unresolved risks remain |
| 7-8 | strong evidence on the main claim, manageable risks |
| 9-10 | unusually strong evidence, clear pull, defensible path, low ambiguity |

## Evidence Adjustment Rules

- Cap any dimension at 5 if evidence is mostly founder intuition.
- Cap any dimension at 6 if evidence comes only from opinions or survey intent.
- Cap any dimension at 7 if there is no behavioral signal.
- Allow 8+ only with strong behavioral evidence or credible comparable market proof.
- Penalize contradictions: if customer pain is high but willingness-to-pay is absent, lower unit economics and risk profile.

## Verdict Thresholds

| Weighted score | Verdict | Meaning |
|---:|---|---|
| 80-100 | go | proceed, but still run the next smallest reversible test |
| 60-79 | conditional go | promising, but riskiest assumptions must be tested before major build or spend |
| 40-59 | pivot | there is something here, but target customer, wedge, pricing, or product must change |
| 0-39 | no-go | do not build unless new evidence changes the premise |

## Scorecard Output Format

| Dimension | Weight | Score | Weighted contribution | Evidence quality | Rationale | Decision |
|---|---:|---:|---:|---|---|---|
| Problem severity | 15% | 0-10 | score * 15 | weak/medium/strong | concise rationale | go/conditional/pivot/no-go |
