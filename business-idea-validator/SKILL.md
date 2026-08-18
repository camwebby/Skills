---
name: business-idea-validator
description: validates startup and business ideas before building by combining a nine-dimension startup idea scorecard with a six-stage validation pipeline, adversarial red-team review, evidence grading, and riskiest-assumption experiments. use when a user asks to validate an idea, assess whether something is worth building, red-team a startup concept, design validation tests, compare startup opportunities, prepare a founder memo, or decide go, conditional go, pivot, or no-go.
---

# Business Idea Validator

## Purpose

Use this skill to turn a raw business idea into an evidence-based validation decision. Combine a six-stage agent pipeline with a weighted nine-dimension scorecard, a red-team pass, and a concrete experiment plan.

Do not cheerlead. Prefer decision-useful evidence over polished optimism. When evidence is weak, lower confidence even if the idea sounds attractive.

## Default Inputs

Accept any of these as input:
- rough idea notes
- startup pitch or one-liner
- customer interview notes
- landing page copy
- market or competitor research
- founder constraints, target geography, budget, timeline, or business model

When the user gives incomplete input, proceed with explicit assumptions instead of blocking. Ask clarifying questions only when the missing detail would change the decision materially.

## Core Workflow

Always run the workflow in this order unless the user asks for a specific subsection.

1. Intake and hypothesis framing
2. Six-stage validation pipeline
3. Nine-dimension scorecard
4. Adversarial red-team review
5. Riskiest-assumption experiment plan
6. Decision memo

Use these references when relevant:
- `references/six-stage-pipeline.md` for stage agents and decision gates
- `references/nine-dimension-scorecard.md` for scoring weights and rubrics
- `references/red-team-checklist.md` for adversarial review prompts
- `references/experiment-menu.md` for validation experiments and pass/fail thresholds
- `references/report-template.md` for the default final report format

If the user provides structured scores or asks to calculate a weighted score, use `scripts/score_validation.py`.

## Step 1: Intake and Hypothesis Framing

Rewrite the idea into this brief:

- Idea name
- One-sentence description
- Target customer and buyer
- Pain/problem
- Current alternatives and workarounds
- Proposed solution
- Business model and likely pricing basis
- Distribution path
- Geography or market scope
- Founder unfair advantages or constraints
- Riskiest assumptions

Separate facts from assumptions. Mark each item as:
- `known`
- `claimed`
- `assumed`
- `unknown`

## Step 2: Six-Stage Validation Pipeline

Run each stage as a separate mental agent. Each stage must produce:
- core question
- supporting evidence
- opposing evidence
- confidence score from 0 to 100
- decision gate: `pass`, `conditional`, `fail`, or `unknown`
- next action

Stages:
1. Problem and market validation
2. Customer and ICP validation
3. Competitive and positioning validation
4. Business model and unit economics validation
5. Feasibility, operations, and trust validation
6. GTM and execution roadmap validation

Use `references/six-stage-pipeline.md` for details.

## Step 3: Nine-Dimension Scorecard

Score each dimension from 0 to 10 and multiply by its weight:

1. Problem severity
2. Market size
3. Market timing
4. Competitive moat
5. Unit economics
6. Founder-market fit
7. Technical or operational feasibility
8. GTM clarity
9. Risk profile

Use the rubric in `references/nine-dimension-scorecard.md`. A high score requires evidence, not merely a plausible narrative.

Default verdict thresholds:
- `80-100`: go
- `60-79`: conditional go, validate riskiest assumptions first
- `40-59`: pivot
- `<40`: no-go

## Step 4: Red-Team Review

Run an adversarial pass after the scorecard. The red-team review must try to invalidate the idea from these perspectives:

- customer skeptic
- buyer/budget skeptic
- incumbent defender
- GTM skeptic
- pricing skeptic
- operational skeptic
- trust/security skeptic
- regulatory or platform-risk skeptic
- founder-fit skeptic

Use `references/red-team-checklist.md`. Include the strongest failure case, not a softened version.

## Step 5: Experiment Plan

Create 3 to 7 experiments that test the riskiest assumptions first. Each experiment must include:
- assumption tested
- experiment type
- setup
- target audience
- cost/time estimate
- pass threshold
- fail threshold
- what decision changes based on the result

Prefer experiments that produce behavioral evidence: payment, signed LOI, qualified conversion, workflow completion, repeated usage, data access, referrals, or switching behavior.

Use `references/experiment-menu.md`.

## Step 6: Decision Memo

Use the structure in `references/report-template.md` unless the user requests another format.

The memo must include:
- verdict: `go`, `conditional go`, `pivot`, or `no-go`
- weighted score and confidence
- top three reasons to believe
- top three reasons it fails
- red-team summary
- validation roadmap
- exact next smallest reversible step
- what evidence would change the decision

## Evidence Rules

Grade evidence quality explicitly:

- `strong`: money, signed commitments, observed workflows, repeated usage, switching costs, high-intent conversions, budget owner confirmation
- `medium`: customer interviews with repeated pain patterns, credible competitor signals, public pricing, search/community demand, waitlist with qualification
- `weak`: opinions, surveys without behavior, founder intuition, generic market reports, vanity signups, unsupported TAM claims

Never let weak evidence create high confidence. If evidence is missing, say so and recommend a test.

## Browsing and Source Use

When current market, competitor, pricing, trend, legal, or regulatory information matters, search the web or available connected sources. Cite important external or internal evidence in the final response when the platform supports citations.

When the user provides files, interviews, notes, transcripts, or internal docs, prioritize those sources before public web information.

## Output Style

Be direct and skeptical. Do not use inflated startup language. Avoid vague statements like "large market opportunity" unless the analysis explains why.

Use tables for scorecards, decision gates, and experiment plans. Use short paragraphs for synthesis.

## Shortcut Modes

If the user asks for a quick scan, produce:
- 10-line intake brief
- top 5 risks
- rough 9-dimension scorecard
- 3 experiments
- provisional verdict

If the user asks for a full validation, produce the complete report template.

If the user asks only to red-team, skip scoring unless useful and focus on failure modes, falsification tests, and decision-changing evidence.
