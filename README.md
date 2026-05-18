# Skills

Practical agent skills for disciplined software work.

Right now this repo starts with one skill: `/compress-architecture`.

## Quickstart

Install the skill with your agent's skill installer, or copy the skill folder into your local skills directory.

```bash
npx skills@latest add yourname/skills/compress-architecture
```

Local install:

```bash
cp -R skills/engineering/compress-architecture ~/.codex/skills/
```

## Skills

### Engineering

| Skill | Use it when |
| --- | --- |
| [`/compress-architecture`](skills/engineering/compress-architecture/README.md) | A codebase feels over-engineered, too layered, or ready for a simplification audit. |

## Philosophy

These skills are small, composable, and meant to be edited. They do not replace judgment. They encode repeatable workflows so agents can follow a disciplined process instead of improvising every time.

Every skill should follow this shape:

```txt
Trigger -> Inputs -> Process -> Output -> Guardrails -> Examples
```

## Repository Layout

```txt
skills/
  engineering/
    compress-architecture/
      README.md
      SKILL.md
      examples.md
```
