# C4 Diagram Sequence

Use `/c4-diagram-sequence` when you already have an architecture plan, decision thread, or rough design and want it turned into a polished C4-style diagram document.

This skill is for architecture communication. It does not just redraw what you wrote. It normalizes the architecture, sharpens names and boundaries, chooses the useful diagrams, and produces a readable Markdown document with Mermaid diagrams.

## What This Skill Does

`/c4-diagram-sequence` takes a plan plus context and writes a diagram sequence that explains the system from broadest view to operational detail:

- **System Context**: who uses the system and what external systems it talks to.
- **Container**: major deployable/runtime pieces, data stores, queues, workers, CLIs, and hosted services.
- **Component**: important modules inside changed containers.
- **Dynamic**: step-by-step runtime flows such as approvals, retries, async work, failures, sharding, and handoffs.
- **Deployment**: where the runtime pieces live and which infrastructure boundaries matter.
- **Supporting diagrams**: state machines, data flow, branch flow, or architecture evolution when they make the design easier to reason about.

The output is intended to be pasted into an architecture doc, PRD, ADR appendix, or implementation plan.

## Required Inputs

The skill needs two things:

1. **Plan**: the proposed architecture, feature design, refactor direction, or system change.
2. **Context**: the surrounding architecture, constraints, docs, codebase, ADRs, or decision thread that the diagrams should respect.

These can come from the current conversation, linked files, repository docs, or source code. If either the plan or context is missing and cannot be recovered, the agent should ask for the missing piece before drawing.

## When To Use It

Use this skill when you say things like:

- "Turn this architecture plan into C4 diagrams."
- "Improve this diagram doc."
- "Write the system context/container/component diagrams for this MVP."
- "Make this design easier to explain."
- "Create a Mermaid C4 sequence from the plan in this thread."
- "Read `MVP-CLOUD.md` and write the architecture diagrams."

It works especially well for cloud workflows, orchestration systems, async jobs, approval flows, research/eval loops, multi-container features, deployment changes, and refactors where the boundary between modules is easy to blur.

## What Good Output Looks Like

A good result is a single Markdown document:

```txt
# [System/change name] - C4 diagrams

Scope:
- ...

Key decisions:
- ...

How to read these diagrams:
| Level | Diagram type | Question it answers |
| --- | --- | --- |

## Level 1 - System Context
## Level 2 - Container
## Level 3 - Component
## Dynamic diagrams
## Deployment diagram
## Supporting diagrams
## Architecture evolution
## Related docs
```

The diagrams should be sparse enough to read, consistent across levels, and explicit about what was intentionally omitted.

## Diagram Selection

The skill always considers system context and container diagrams.

It adds other diagrams only when useful:

| Diagram | Use it when |
| --- | --- |
| Component | Important modules inside a container need explanation. |
| Dynamic | Runtime ordering, async behavior, retries, approvals, failures, or sharding matter. |
| Deployment | Hosting, infrastructure, environments, networking, or ownership affect the design. |
| State | Lifecycle statuses, gates, retries, interruptions, or terminal states matter. |
| Data flow | Source of truth, write paths, or read paths are easy to confuse. |
| Branch/evolution | Promotion, stacked branches, or rejected architectures explain the current shape. |

The skill should not create a code-level diagram unless specific interfaces, schemas, classes, functions, or contracts are architecturally important.

## Example Invocation

```txt
/c4-diagram-sequence
Use the architecture plan in this thread and write the C4 diagram doc.
```

With a target file:

```txt
/c4-diagram-sequence
Read MVP-CLOUD.md and the current architecture thread. Write docs/architecture/auto-research-c4.md.
```

## Guardrails

- Do not ask for context that can be recovered from the repo.
- Do not dump every possible diagram.
- Do not mix C4 levels: external systems stay outside, containers stay runtime/deployable, components stay inside one container.
- Do not hide assumptions inside diagram nodes. State assumptions in prose.
- Do not let implementation detail crowd out the architecture story.
- Prefer fewer, clearer diagrams over a complete but unreadable diagram set.

## Files

- [SKILL.md](SKILL.md): agent instructions
- [examples.md](examples.md): example invocation and output shape

