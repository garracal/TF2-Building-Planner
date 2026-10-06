#!/bin/sh
# Starts the TF2 Building Planner library on this computer.
# Put this file next to index.html (the planner) and the configs folder, then run it.
cd "$(dirname "$0")" || exit 1
PY=python3
command -v python3 >/dev/null 2>&1 || PY=python
if [ -f build_index.py ]; then
  echo "Rebuilding index.json..."
  "$PY" build_index.py
fi
echo
echo "Library running at http://localhost:8000/   (press Ctrl+C to stop it)"
( sleep 1; open "http://localhost:8000/" 2>/dev/null || xdg-open "http://localhost:8000/" 2>/dev/null ) >/dev/null 2>&1 &
"$PY" -m http.server 8000
