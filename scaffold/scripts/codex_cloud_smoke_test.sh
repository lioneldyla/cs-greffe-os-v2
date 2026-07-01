#!/usr/bin/env bash
set -euo pipefail
python -m py_compile 02_MVP_EXECUTABLE/app.py
echo "Smoke test OK"
