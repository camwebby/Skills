# Compress Architecture

![SpaceX Raptor 1, 2, and 3 comparison](https://www.eonmsk.com/wp-content/uploads/2024/08/raptor1-2-3-comparison-2.jpg)

Image source: [EONMSK, attributed to SpaceX](https://www.eonmsk.com/2024/08/03/spacex-raptor-1-vs-raptor-2-vs-raptor-3/).

## The Hook

SpaceX's Raptor engine progression is a useful mental model for software architecture.

Raptor 1 looked dense with external plumbing. Raptor 2 reduced and reorganized it. Raptor 3 integrated more of the system, reduced exposed complexity, and improved performance at the same time.

This skill asks the same question of a codebase:

```txt
Can the system do the same job with fewer visible parts?
```

The target is not minimalism for its own sake. The target is less accidental complexity: fewer speculative layers, fewer pass-through modules, fewer duplicate concepts, and fewer abstractions that no longer earn their keep.

## What This Skill Does

`/compress-architecture` runs a Raptor-style audit of a codebase or a scoped part of a codebase.

It makes the agent:

- map architectural boundaries before judging them
- classify components with a fixed vocabulary
- challenge thin abstractions and speculative layers
- protect boundaries that are genuinely load-bearing
- produce a ranked compression report before editing files

The skill does not immediately refactor. It reports first, waits for confirmation, and then changes one thing at a time.

## Software Ideas Behind It

This skill combines several durable software design ideas:

| Idea | What it contributes |
| --- | --- |
| KISS | Prefer the simplest design that solves the real problem. |
| YAGNI | Remove infrastructure for requirements that do not exist yet. |
| DRY | Collapse duplicate logic and duplicate concepts. |
| XP Simple Design | Passes tests, reveals intention, removes duplication, and minimizes elements in that order. |
| Refactoring | Change structure without changing behavior. |
| Essential vs. accidental complexity | Preserve domain complexity; remove complexity created by implementation choices. |
| Connascence | Identify coupling and decide whether that coupling is domain-justified or incidental. |
| Rate of change | Keep things separate when they evolve for different reasons. |

The important distinction is from Rich Hickey's "Simple Made Easy": simple means one concept, not necessarily familiar or nearby.

## Compression Vocabulary

Every component gets one label:

| Label | Meaning |
| --- | --- |
| `load-bearing` | Removing it increases total system complexity. Keep it. |
| `speculative` | Built for a requirement that does not exist yet. |
| `delegating` | Mostly passes calls through with little logic of its own. |
| `duplicate` | Repeats logic or structure already present elsewhere. |
| `misplaced` | Right idea, wrong abstraction level or location. |

Recommended actions use this vocabulary:

```txt
collapse · delete · rename · move · split · keep
```

## When To Use It

Use this skill when you say things like:

- "This feels too complex."
- "There are too many layers here."
- "Raptor this."
- "Can we simplify this architecture?"
- "Is this abstraction earning its existence?"
- "Audit this feature before we add more code."

For large codebases, scope the audit first:

```txt
/compress-architecture
Audit the billing workflow only. Focus on services, repositories, and adapters.
```

## Example Output

```txt
### src/billing/invoice-service.ts
Label: delegating
Proposed action: collapse
Complexity delta: Medium
Reasoning: This service forwards calls to the repository without adding policy, validation, or error handling. Collapsing it into the billing command handler removes a layer without weakening a domain boundary.

Summary: 4 load-bearing, 3 candidates for compression (1 High / 1 Medium / 1 Low impact).
```

## What "Complexity Delta" Means

Complexity delta is the expected net change in total system complexity if the recommendation is applied.

- `High`: removes a major layer, boundary, or repeated concept
- `Medium`: simplifies a local workflow or collapses a thin abstraction
- `Low`: tidies a small pass-through file, folder, or type

If the term feels too opaque in practice, rename it to `Impact`. The concept is just priority: do the changes that reduce the most complexity first.

## Red Lines

The skill should not collapse:

- real domain boundaries
- testability seams
- public API contracts
- explicit error handling layers
- modules that change at different rates

Small is not automatically bad. Thin is only suspect when it does not protect a real boundary.

## Files

- [SKILL.md](SKILL.md): agent instructions
- [examples.md](examples.md): example invocation and output shape
