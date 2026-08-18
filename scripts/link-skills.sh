#!/usr/bin/env bash
set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"

link_skills_into() {
  local dest="$1"

  if [ -L "$dest" ]; then
    resolved="$(readlink "$dest")"
    case "$resolved" in
      "$REPO"|"$REPO"/*)
        echo "error: $dest is a symlink into this repo ($resolved)." >&2
        echo "Remove it and re-run; this script will recreate per-skill symlinks." >&2
        exit 1
        ;;
    esac
  fi

  mkdir -p "$dest"

  find "$REPO/skills" -name SKILL.md -not -path '*/node_modules/*' -print0 |
    while IFS= read -r -d '' skill_md; do
      src="$(dirname "$skill_md")"
      name="$(basename "$src")"
      target="$dest/$name"

      if [ -e "$target" ] && [ ! -L "$target" ]; then
        echo "skipping $target because it exists and is not a symlink" >&2
        continue
      fi

      ln -sfn "$src" "$target"
      echo "linked $name -> $src (in $dest)"
    done
}

link_skills_into "${CODEX_HOME:-$HOME/.codex}/skills"
link_skills_into "${PI_AGENT_DIR:-$HOME/.pi/agent}/skills"
