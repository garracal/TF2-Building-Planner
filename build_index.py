#!/usr/bin/env python3
"""Builds index.json for the TF2 Building Planner config library.

Run from the repo root:   python3 build_index.py
Reads every .json file under configs/ and writes a small index.json listing
each config's map, author, description and size. The planner's library page
loads only this index, then fetches a single config when someone clicks it.
"""
import json, pathlib, subprocess, sys
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parent
CONFIGS = ROOT / "configs"
entries, skipped = [], []


def added(f):
    """Date the file was first committed (needs full git history), else its modified time."""
    try:
        out = subprocess.run(
            ["git", "log", "--diff-filter=A", "--follow", "--format=%cI", "--", str(f)],
            cwd=ROOT, capture_output=True, text=True, timeout=20).stdout.split()
        if out:
            return out[-1][:10]
    except Exception:
        pass
    return datetime.fromtimestamp(f.stat().st_mtime, tz=timezone.utc).date().isoformat()


for f in sorted(CONFIGS.rglob("*.json")):
    try:
        data = json.loads(f.read_text(encoding="utf-8"))
        m = data.get("map") or data          # wrapper format, or a bare map
        meta = data.get("meta") or m.get("meta") or {}
        stages = m.get("stages") or [m]      # older exports have a single stage
        if not isinstance(m, dict) or not (m.get("stages") or m.get("img")):
            raise ValueError("not a TF2 Building Planner config")
        entries.append({
            "file": f.relative_to(ROOT).as_posix(),
            "map": meta.get("name") or m.get("name") or f.stem,
            "author": meta.get("author", ""),
            "description": meta.get("description", "")[:250],
            "cover": meta.get("cover", ""),
            "stages": len(stages),
            "added": added(f),
            "sizeMB": round(f.stat().st_size / 1_000_000, 2),
        })
    except Exception as e:
        skipped.append((f.name, str(e)))

entries.sort(key=lambda e: (e["map"].lower(), e["author"].lower(), e["file"]))
(ROOT / "index.json").write_text(json.dumps(entries, indent=2), encoding="utf-8")

print(f"Indexed {len(entries)} config(s) -> index.json")
for name, err in skipped:
    print(f"  skipped {name}: {err}", file=sys.stderr)
sys.exit(1 if skipped else 0)
