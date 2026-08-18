#!/usr/bin/env python3
"""Compute weighted business idea validation scores from JSON.

Input JSON may be either:
{
  "problem_severity": 7,
  "market_size": 6,
  ...
}

or:
{
  "scores": {
    "problem_severity": 7,
    ...
  }
}

Scores are 0-10. Output is a compact JSON verdict.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

WEIGHTS = {
    "problem_severity": 15,
    "market_size": 12,
    "market_timing": 10,
    "competitive_moat": 12,
    "unit_economics": 15,
    "founder_market_fit": 8,
    "technical_or_operational_feasibility": 10,
    "gtm_clarity": 10,
    "risk_profile": 8,
}

ALIASES = {
    "problem": "problem_severity",
    "market": "market_size",
    "timing": "market_timing",
    "moat": "competitive_moat",
    "economics": "unit_economics",
    "feasibility": "technical_or_operational_feasibility",
    "technical_feasibility": "technical_or_operational_feasibility",
    "gtm": "gtm_clarity",
    "risk": "risk_profile",
}


def normalize_key(key: str) -> str:
    normalized = key.strip().lower().replace("-", "_").replace(" ", "_")
    return ALIASES.get(normalized, normalized)


def verdict(total: float) -> str:
    if total >= 80:
        return "go"
    if total >= 60:
        return "conditional go"
    if total >= 40:
        return "pivot"
    return "no-go"


def load_scores(path: str | None) -> dict[str, Any]:
    raw = sys.stdin.read() if not path or path == "-" else Path(path).read_text(encoding="utf-8")
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"invalid json: {exc}") from exc
    if not isinstance(data, dict):
        raise SystemExit("input json must be an object")
    scores = data.get("scores", data)
    if not isinstance(scores, dict):
        raise SystemExit("scores must be an object")
    return scores


def compute(scores: dict[str, Any]) -> dict[str, Any]:
    normalized_scores: dict[str, float] = {}
    for raw_key, value in scores.items():
        key = normalize_key(str(raw_key))
        if key not in WEIGHTS:
            continue
        try:
            score = float(value)
        except (TypeError, ValueError) as exc:
            raise SystemExit(f"score for {raw_key!r} must be numeric") from exc
        if not 0 <= score <= 10:
            raise SystemExit(f"score for {raw_key!r} must be between 0 and 10")
        normalized_scores[key] = score

    missing = [key for key in WEIGHTS if key not in normalized_scores]
    if missing:
        raise SystemExit("missing scores: " + ", ".join(missing))

    rows = []
    total = 0.0
    for key, weight in WEIGHTS.items():
        score = normalized_scores[key]
        contribution = score * weight / 10
        total += contribution
        rows.append(
            {
                "dimension": key,
                "weight_percent": weight,
                "score": score,
                "weighted_contribution": round(contribution, 2),
            }
        )

    return {
        "weighted_score": round(total, 2),
        "verdict": verdict(total),
        "dimensions": rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Compute weighted validation score.")
    parser.add_argument("path", nargs="?", help="JSON file path, or stdin when omitted")
    args = parser.parse_args()
    result = compute(load_scores(args.path))
    print(json.dumps(result, indent=2, sort_keys=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
