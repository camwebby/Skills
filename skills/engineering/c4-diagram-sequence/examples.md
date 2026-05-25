# C4 Diagram Sequence Examples

## Invocation

```txt
/c4-diagram-sequence
Use the architecture plan in this thread and write the C4 diagram doc.
```

## Invocation With File Target

```txt
/c4-diagram-sequence
Read MVP-CLOUD.md and the current thread. Write docs/architecture/auto-research-c4.md.
```

## Expected Behavior

The skill should recover the plan and context, ask for missing material only if necessary, normalize the architecture model, choose a useful diagram set, and output a full Markdown document with fenced Mermaid diagrams.

## Example Output Shape

```txt
# Auto-research cloud MVP - C4 diagrams

Scope:
- Cloud-native v1 auto-research cycle.

Key decisions:
- Cron is the only cycle starter.
- Cloudflare Workflow owns one durable cycle.
- Cloudflare Containers run interruptible eval compute.
- customer-api is the temporary bridge to the private prompt eval DB.

How to read these diagrams:
| Level | Diagram type | Question it answers |
| --- | --- | --- |
| 1 | System Context | Who uses the system and what external systems does it talk to? |
| 2 | Container | What are the major deployable/runtime pieces? |
| 3 | Component | What important modules live inside changed containers? |
| - | Dynamic | What happens step-by-step during a cycle? |
| - | Deployment | Where does each container run? |

## Level 1 - System Context

```mermaid
C4Context
    title Level 1 - System Context: Auto-research
```

## Level 2 - Container

...
```

## Good Diagram Set For A Cloud Workflow

- Context diagram
- Container diagram
- Component diagrams for Worker, eval container, and imported research modules
- Dynamic happy path
- Dynamic reject/failure paths if the approval or failure behavior is architecturally important
- Deployment diagram
- State diagrams for cycle and container lifecycle
- Data-flow summary if source-of-truth is easy to confuse
- Evolution table when previous designs were rejected

