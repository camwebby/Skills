# Skills

Practical agent skills for disciplined software work.

## Quickstart

Install a skill with your agent's skill installer, or copy the skill folder into your local skills directory.

```bash
npx skills@latest add yourname/skills/compress-architecture
```

Local install:

```bash
cp -R skills/engineering/compress-architecture ~/.codex/skills/
```

To list skills in this repo:

```bash
./scripts/list-skills.sh
```

To symlink all skills into `~/.codex/skills` and `~/.pi/agent/skills`:

```bash
./scripts/link-skills.sh
```

For **pi**, also add the repo skills tree to `~/.pi/agent/settings.json` (or project `.pi/settings.json`):

```json
{
  "skills": ["/Users/cameron/Documents/Skills/skills"]
}
```

## Skills

### Engineering

| Skill | Use it when |
| --- | --- |
| [`/compress-architecture`](skills/engineering/compress-architecture/README.md) | A codebase feels over-engineered, too layered, or ready for a simplification audit. |
| [`/c4-diagram-sequence`](skills/engineering/c4-diagram-sequence/README.md) | You have an architecture plan and context and want a polished sequence of C4-style diagrams. |

### Media

| Skill | Use it when |
| --- | --- |
| [`/tiktok-short`](skills/media/tiktok-short/README.md) | You have a 16:9 video and want a TikTok-style 9:16 short with zoom cuts, opening warp, and karaoke captions. |

## Philosophy

These skills are small, composable, and meant to be edited. They do not replace judgment. They encode repeatable workflows so agents can follow a disciplined process instead of improvising every time.

Every skill should follow this shape:

```txt
Trigger -> Inputs -> Process -> Output -> Guardrails -> Examples
```

## Repository Layout

```txt
skills/
  media/
    tiktok-short/
      README.md
      SKILL.md
      reference.md
      examples.md
      scripts/
        build_tiktok_short.py
  engineering/
    compress-architecture/
      README.md
      SKILL.md
      examples.md
    c4-diagram-sequence/
      README.md
      SKILL.md
      examples.md
scripts/
  list-skills.sh
  link-skills.sh
```

