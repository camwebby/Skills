---
name: c4-diagram-sequence
description: Use this skill when the user has an architecture plan and context, or wants to provide them, and wants a polished sequence of C4-style diagrams. It turns a plan into a readable architecture document with context, container, component, dynamic, deployment, state, data-flow, and evolution diagrams where appropriate.
---

# C4 Diagram Sequence

Turn an architecture plan plus context into a coherent C4 diagram document.

The user must have a plan and context either in the current thread, linked files, or the repository. If either is missing and cannot be recovered from the codebase, ask for it before producing diagrams.

The output should improve the plan, not merely reformat it.

## Inputs

Recover inputs in this order:

1. Current thread context.
2. Files or docs the user references.
3. `CONTEXT.md`, architecture docs, ADRs, README files, infra config, and relevant source code.
4. User clarification, only when the plan or context is genuinely missing.

If the plan is missing, ask:

```text
Please paste the architecture plan or describe the system/change you want diagrammed.
```

If context is missing, ask:

```text
Please provide the relevant context: current architecture, repo docs, constraints, or the decision thread this diagram should reflect.
```

Do not ask questions that can be answered by reading the repository.

## Process

### 1. Normalize The Architecture

Before drawing, extract a clean architecture model:

- **Scope**: system/change being diagrammed.
- **Primary story**: what happens end-to-end.
- **People**: users, operators, approvers, admins, or other human roles.
- **External systems**: systems outside the system boundary.
- **Containers**: deployable/runtime units, data stores, queues, CLIs, workers, hosted services, or durable runtimes.
- **Components**: important modules inside specific containers.
- **Dynamic flows**: runtime sequences that explain the architecture.
- **Deployment topology**: where containers run.
- **State/data facts**: statuses, durable records, queues, branches, lineage, or data ownership.
- **Architecture evolution**: rejected or superseded shapes that explain why the current shape exists.

Improve unclear plans by tightening names, separating source of truth from compute, moving hosting details to deployment diagrams, removing duplicate relationships, and marking assumptions explicitly.

### 2. Choose The Diagram Set

Always consider:

- **Level 1 - System Context**: who uses the system and which external systems it talks to.
- **Level 2 - Container**: major deployable/runtime pieces and data stores.

Add only when useful:

- **Level 3 - Component**: important modules inside changed containers.
- **Dynamic diagrams**: step-by-step runtime flows, especially async, approval, retry, failure, or sharded workflows.
- **Deployment diagram**: where things run and how infrastructure boundaries affect the design.
- **State diagrams**: lifecycle statuses, retries, interruptibility, gates, or terminal states.
- **Data-flow diagrams**: source-of-truth and write/read paths.
- **Branch/evolution diagrams**: stacked branches, promotion rules, or superseded architecture decisions.

Do not create a code-level diagram unless the plan depends on specific classes, interfaces, schema shapes, or function contracts.

### 3. Write The Diagram Document

Use this structure:

```text
# [System/change name] - C4 diagrams

Short intro.

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

Use fenced Mermaid blocks:

````markdown
```mermaid
C4Context
    title ...
```
````

Prefer C4 Mermaid diagram types when they fit:

- `C4Context`
- `C4Container`
- `C4Component`
- `C4Dynamic`
- `C4Deployment`

Use normal Mermaid diagrams for supporting views:

- `stateDiagram-v2`
- `flowchart`
- `gitGraph`

### Diagram Rules

- Keep each diagram readable. Split dense diagrams instead of producing a hairball.
- Use stable identifiers and consistent display names across diagrams.
- Put each element at the correct C4 level.
- Keep system context free of internal components.
- Keep container diagrams focused on deployable/runtime units and data stores.
- Keep component diagrams scoped to one container at a time.
- Label relationships with meaningful verbs.
- Include protocol or mechanism only when it clarifies the architecture.
- Prefer concrete names over generic "service", "manager", or "processor".
- Mark assumptions in prose, not as fake diagram nodes.

## Quality Pass

Before finalizing, check:

- Every relationship endpoint exists in the same diagram.
- Names are consistent across levels.
- External systems are not drawn as internal containers.
- Containers are not drawn as components.
- Deployment nodes contain runtime/container instances, not abstract concepts.
- Dynamic steps are numbered and follow the real lifecycle.
- The document states which diagrams are intentionally omitted.
- Mermaid syntax is plausible and fenced correctly.
- The final result answers the architecture questions, not just the implementation details.

## Output

Return the full Markdown diagram document unless the user gave a file path. If the user gave a path, write the document there and summarize the file created.

If the architecture is under-specified, produce a short "missing context" section and ask the smallest number of questions needed to continue.

