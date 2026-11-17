"""Validate and pretty-print JSON files."""
from __future__ import annotations

import json
from pathlib import Path

VERSION = "0.4.5"


class Plumbgamble8bTool:
    """Check JSON syntax and render a normalized form."""

    def check(self, path):
        target = Path(path)
        if not target.is_file():
            return False, "file not found"
        try:
            data = json.loads(target.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            return False, f"invalid JSON at line {exc.lineno} col {exc.colno}: {exc.msg}"
        return True, json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True)
