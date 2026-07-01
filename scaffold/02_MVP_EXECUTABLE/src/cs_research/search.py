from pathlib import Path

CORPUS_ROOT = Path(__file__).resolve().parents[2] / "03_CORPUS"

def search_corpus(query: str):
    results = []
    q = query.lower().strip()
    if not q:
        return results
    for file in CORPUS_ROOT.rglob("*.md"):
        text = file.read_text(encoding="utf-8", errors="ignore")
        if q in text.lower() or q in file.name.lower():
            results.append(str(file.relative_to(CORPUS_ROOT)))
    return results
