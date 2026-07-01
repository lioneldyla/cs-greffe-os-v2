# State Transitions

Generic LDGP lifecycle:

Draft → Registered → Reviewed → Approved → Active → Deprecated → Archived

```mermaid
stateDiagram-v2
    [*] --> Draft
    Draft --> Registered
    Registered --> Reviewed
    Reviewed --> Approved
    Approved --> Active
    Active --> Deprecated
    Deprecated --> Archived
    Archived --> [*]


Puis crée le test :

```bash
cat > tests/docs/test_ldgp_governance_state_model.py <<'EOF'
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE_DIR = ROOT / "living-digital-governance-platform" / "models" / "states"

REQUIRED_FILES = [
    "README.md",
    "STATE_GOVERNANCE_RULES.md",
    "STATE_TRANSITIONS.md",
    "LIFECYCLE_MATRIX.md",
]

REQUIRED_STATES = [
    "Draft",
    "Registered",
    "Reviewed",
    "Approved",
    "Active",
    "Deprecated",
    "Archived",
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


def read_all_state_docs() -> str:
    return "\n".join((STATE_DIR / name).read_text(encoding="utf-8") for name in REQUIRED_FILES)


def test_state_folder_and_files_exist():
    assert STATE_DIR.exists()
    for name in REQUIRED_FILES:
        assert (STATE_DIR / name).exists()


def test_required_states_are_documented():
    content = read_all_state_docs()
    for state in REQUIRED_STATES:
        assert state in content


def test_governance_rules_are_documented():
    content = read_all_state_docs().lower()
    assert "no critical object without owner" in content
    assert "human validation" in content
    assert "archive before deletion" in content


def test_mermaid_diagram_is_present():
    content = (STATE_DIR / "STATE_TRANSITIONS.md").read_text(encoding="utf-8")
    assert "```mermaid" in content
    assert "stateDiagram-v2" in content


def test_lifecycle_matrix_mentions_core_objects():
    content = (STATE_DIR / "LIFECYCLE_MATRIX.md").read_text(encoding="utf-8")
    for obj in REQUIRED_OBJECTS:
        assert obj in content
