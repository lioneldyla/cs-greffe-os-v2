from pathlib import Path

CORPUS_ROOT = Path(__file__).resolve().parents[2] / "03_CORPUS" / "CS_LEARN"

def list_subjects():
    if not CORPUS_ROOT.exists():
        return []
    return sorted([p.name for p in CORPUS_ROOT.iterdir() if p.is_dir()])

def search_files(query: str):
    results = []
    q = query.lower().strip()
    if not q:
        return results
    for file in CORPUS_ROOT.rglob("*.md"):
        text = file.read_text(encoding="utf-8", errors="ignore")
        if q in text.lower() or q in file.name.lower():
            results.append(str(file.relative_to(CORPUS_ROOT)))
    return results
