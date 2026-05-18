---
name: compress-architecture
description: Use this skill when the user asks to simplify, refactor, audit, or reduce complexity in a codebase. Triggers include "this feels too complex", "too many layers", "simplify this", "is this over-engineered", "reduce abstraction", "clean up architecture", "too many files", "raptor this", or requests for a Raptor 3 audit. Produces a ranked compression report with actionable recommendations and waits for confirmation before editing files.
---

# Compress Architecture

Perform a Raptor 3 audit: reduce accidental complexity while preserving complexity the problem actually demands. Every abstraction, layer, and module must justify its existence. If it cannot, recommend collapsing, deleting, renaming, moving, or splitting it.

Ask the user to scope the audit first if the codebase is large.

## Workflow

### 1. Map the System

Before judging, silently inventory:

- Architectural boundaries: services, packages, repositories, modules, layers.
- Wrappers: adapters, facades, utility files, thin services.
- Files or modules under about 60 lines that mostly delegate.
- Types or interfaces that only rename another type.
- Folders with only one file.

Use this inventory as working memory. Do not print it raw.

### 2. Classify Components

Assign each inventoried item exactly one label:

- `load-bearing`: Removing it increases total system complexity.
- `speculative`: Built for a requirement that does not exist yet.
- `delegating`: Mostly passes calls through with little logic.
- `duplicate`: Repeats logic or structure already present elsewhere.
- `misplaced`: Right idea, wrong abstraction level or location.

If classification is genuinely hard, note that ambiguity in the report.

### 3. Apply Compression Questions

For each `speculative`, `delegating`, `duplicate`, or `misplaced` item, evaluate:

- Earn-your-existence: Does removing it increase or decrease total complexity?
- Single-concept: Does it do one role, or are multiple roles coupled together?
- Rate-of-change: Does it change at the same rate as neighboring code?
- Connascence: Is coupling domain-justified or incidental?
- Integration opportunity: Can it collapse into an adjacent thin module without losing clarity?

## Red Lines

Never recommend removing or collapsing:

- Domain boundaries for genuinely separate business concerns.
- Testability seams, including small adapters that make third-party services swappable.
- Code that changes at different rates, such as DB and UI modules.
- Explicit error handling layers.
- Public API contracts.

If a candidate hits a red line, label it `load-bearing` and explain why in one sentence.

## Output Format

Present a ranked list, most impactful first. Use this exact structure for each candidate:

```text
### [Component name or path]
Label: delegating | speculative | duplicate | misplaced
Proposed action: COLLAPSE | DELETE | RENAME | MOVE | SPLIT | KEEP (justified)
Complexity delta: High / Medium / Low
Reasoning: [1-3 direct sentences.]
```

After the list, include:

```text
Summary: X load-bearing, Y candidates for compression (Z High / W Medium / V Low impact).
```

## Interaction Rules

- Ask before acting. Present the compression report and wait for confirmation before touching files.
- Change one thing at a time. Never collapse multiple candidates in one edit.
- Keep tests green. After each compression step, run the relevant tests.
- If no tests cover the area, flag that before proceeding.
- Rename before deleting when deadness is uncertain.
- Use only this vocabulary for labels: `load-bearing`, `speculative`, `delegating`, `duplicate`, `misplaced`.
- Use only this vocabulary for actions: `collapse`, `delete`, `rename`, `move`, `split`, `keep`.

## Tone

Be direct. Skip basics unless they support the recommendation. Keep sentences short.
