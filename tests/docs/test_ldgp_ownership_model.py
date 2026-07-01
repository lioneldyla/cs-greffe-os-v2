from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OWNERSHIP_DIR = ROOT / "living-digital-governance-platform" / "models" / "ownership"

REQUIRED_FILES = [
    "README.md",
    "OWNERSHIP_ROLES.md",
    "OWNERSHIP_MATRIX.md",
    "RACI_MODEL.md",
]

REQUIRED_ROLES = [
    "Owner",
    "Steward",
    "Reviewer",
    "Approver",
    "Accountable Authority",
    "Human Validator",
]

REQUIRED_OBJECTS = [
    "Dataset",
    "Document",
    "AI Use Case",
    "KPI",
    "Risk",
    "Decision",
    "Action",
]


def read_all_docs() -> str:
    return "\n".join((OWNERSHIP_DIR / name).read_text(encoding="utf-8") for name in REQUIRED_FILES)


def test_ownership_folder_and_files_exist():
    assert OWNERSHIP_DIR.exists()
    for name in REQUIRED_FILES:
        assert (OWNERSHIP_DIR / name).exists()


def test_required_roles_are_documented():
    content = read_all_docs()
    for role in REQUIRED_ROLES:
        assert role in content


def test_required_objects_are_documented():
    content = read_all_docs()
    for obj in REQUIRED_OBJECTS:
        assert obj in content


def test_raci_is_documented():
    content = read_all_docs()
    assert "RACI" in content
    assert "Responsible" in content
    assert "Accountable" in content
    assert "Consulted" in content
    assert "Informed" in content


def test_human_validation_and_traceability_columns_exist():
    content = (OWNERSHIP_DIR / "OWNERSHIP_MATRIX.md").read_text(encoding="utf-8")
    assert "Human Validation Required" in content
    assert "Traceability Required" in content
