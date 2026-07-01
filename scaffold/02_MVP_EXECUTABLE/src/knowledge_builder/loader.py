from pathlib import Path
import csv

PLAN_PATH = Path(__file__).resolve().parents[2] / "data" / "knowledge_build_plan.csv"

def load_knowledge_build_plan():
    if not PLAN_PATH.exists():
        return []
    with PLAN_PATH.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))
