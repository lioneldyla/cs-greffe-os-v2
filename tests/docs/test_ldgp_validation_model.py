from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VALIDATION_DIR = ROOT / "living-digital-governance-platform" / "models" / "validation"

REQUIRED_FILES = [
    "README.md",
    "VALIDATION_RULES.md",
    "VALIDATION_MATRIX.md",
    "HUMAN_VALIDATION_MODEL.md",
]

REQUIRED_TERMS = [
    "validation",
    "human validation",
    "AI outputs",
    "Accountable Authority",
    "Traceability Required",
    "Dataset",
    "Document",
    "AI Use Case",
    "AI Output",
    "KPI",
    "Risk",
    "Decision",
    "Action",
]


def read_all_docs() -> str:
    return "\n".join((VALIDATION_DIR / name).read_text(encoding="utf-8") for name in REQUIRED_FILES)


def test_validation_folder_and_files_exist():
    assert VALIDATION_DIR.exists()
    for name in REQUIRED_FILES:
        assert (VALIDATION_DIR / name).exists()


def test_required_terms_are_documented():
    content = read_all_docs()
    for term in REQUIRED_TERMS:
        assert term in content


def test_mermaid_human_validation_flow_exists():
    content = (VALIDATION_DIR / "HUMAN_VALIDATION_MODEL.md").read_text(encoding="utf-8")
    assert "```mermaid" in content
    assert "Human Validation Required" in content
    assert "Traceability Log" in content


def test_no_active_without_validation_rule_exists():
    content = (VALIDATION_DIR / "VALIDATION_RULES.md").read_text(encoding="utf-8")
    assert "No critical object can become Active without validation" in content
