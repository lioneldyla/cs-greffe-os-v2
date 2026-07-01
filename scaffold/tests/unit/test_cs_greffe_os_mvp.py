from pathlib import Path
import pandas as pd

def test_modules_csv_exists():
    path = Path("cs_greffe_os/data/modules.csv")
    assert path.exists()
    df = pd.read_csv(path)
    assert {"module", "description", "objectif"}.issubset(df.columns)

def test_no_phase_23_artifact():
    assert not list(Path("docs/cs_greffe_os").rglob("*PHASE_23*"))

def test_teeo_v27_files_exist():
    base = Path("02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO")
    for name in [
        "IMPROVEMENT_BACKLOG_V1.md",
        "CHANGE_LOG_V1.md",
        "VERSION_HISTORY_V1.md",
        "IMPACT_MEASUREMENT_V1.md",
    ]:
        assert (base / name).exists()

def test_teeo_scorecard_locked_at_48():
    text = Path("02_MVP_EXECUTABLE/03_CORPUS/CORPUS_PROGRESS_SCORECARD_V1.md").read_text(encoding="utf-8")
    assert "48%" in text
    assert "Aucune nouvelle matière" in text
