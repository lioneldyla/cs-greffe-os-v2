from pathlib import Path

def test_mvp_app_exists():
    assert Path("02_MVP_EXECUTABLE/app.py").exists()

def test_teoo_corpus_backbone_exists():
    base = Path("02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO")
    assert (base / "INDEX_V1.md").exists()
    assert (base / "SOURCAGE" / "TEEO_LEVEL_C_READINESS_CHECKLIST.md").exists()

def test_improvement_loop_exists():
    base = Path("02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO")
    required = [
        "IMPROVEMENT_BACKLOG_V1.md",
        "CHANGE_LOG_V1.md",
        "VERSION_HISTORY_V1.md",
        "IMPACT_MEASUREMENT_V1.md",
    ]
    for item in required:
        assert (base / item).exists()

def test_build_the_corpus_orientation():
    text = Path("02_MVP_EXECUTABLE/app.py").read_text(encoding="utf-8")
    assert "BUILD THE CORPUS" in text
