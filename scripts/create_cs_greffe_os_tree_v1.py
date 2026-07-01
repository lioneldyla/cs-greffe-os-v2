from pathlib import Path
import csv

ROOT = Path.cwd()

DIRS = [
    "cs_greffe_os/data",
    "02_MVP_EXECUTABLE/data",
    "02_MVP_EXECUTABLE/src/cs_learn",
    "02_MVP_EXECUTABLE/src/cs_research",
    "02_MVP_EXECUTABLE/src/strategic_command_center",
    "02_MVP_EXECUTABLE/src/knowledge_builder",
    "02_MVP_EXECUTABLE/tests",
    "02_MVP_EXECUTABLE/feedback",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/COURS",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/PLANS",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/FICHES",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/RESUMES",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/QCM",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/CAS_PRATIQUES",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/REFERENCES",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/SOURCAGE",
    "02_MVP_EXECUTABLE/03_CORPUS/GREFFE_IVOIRIEN",
    "02_MVP_EXECUTABLE/03_CORPUS/SYSTEME_JUDICIAIRE_IVOIRIEN",
    "02_MVP_EXECUTABLE/03_CORPUS/TRANSFORMATION_NUMERIQUE",
    "02_MVP_EXECUTABLE/03_CORPUS/BIBLIOGRAPHIE",
    "02_MVP_EXECUTABLE/03_CORPUS/TEXTES",
    "02_MVP_EXECUTABLE/03_CORPUS/JURISPRUDENCE",
    "02_MVP_EXECUTABLE/03_CORPUS/LIVING_GOVERNANCE_ENGINEERING",
    "docs/extractions",
    "docs/cs_greffe_os/01_PROJECT_MEMORY",
    "docs/cs_greffe_os/20_ROADMAP",
    "docs/cs_greffe_os/22_JDGO",
    "docs/cs_greffe_os/V1_EXECUTION",
    "source_materials",
    "scripts",
    "tests",
]

FILES = [
    "README.md",
    "requirements.txt",
    ".gitignore",
    "cs_greffe_os/app.py",
    "cs_greffe_os/data/modules.csv",
    "02_MVP_EXECUTABLE/app.py",

    "02_MVP_EXECUTABLE/feedback/CS_LEARN_IMPROVEMENTS.md",
    "02_MVP_EXECUTABLE/feedback/CS_LEARN_INFJ_USAGE_2026.md",
    "02_MVP_EXECUTABLE/feedback/CS_LEARN_KNOWLEDGE_GAPS.md",
    "02_MVP_EXECUTABLE/feedback/CS_LEARN_SESSION_HISTORY.md",
    "02_MVP_EXECUTABLE/feedback/IMPROVEMENT_BACKLOG_V1.md",
    "02_MVP_EXECUTABLE/feedback/ISSUES_REGISTER_V1.md",
    "02_MVP_EXECUTABLE/feedback/USAGE_LOG_V1.md",

    "02_MVP_EXECUTABLE/03_CORPUS/CORPUS_MASTER_INDEX_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CORPUS_BUILD_PLAN_2026_2040.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CORPUS_OPERATING_PLAN_2026_2028.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CORPUS_QUALITY_AND_METADATA_STANDARD_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CORPUS_PROGRESS_SCORECARD_V1.md",

    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/CS_LEARN_MASTER_INDEX_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/INDEX_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/USER_USAGE_LOG_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/USER_FEEDBACK_REGISTER_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/LESSONS_LEARNED_V2.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/VALUE_REGISTER_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/IMPROVEMENT_BACKLOG_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/CHANGE_LOG_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/VERSION_HISTORY_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/IMPACT_MEASUREMENT_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/COURS/PLAN_DIRECTEUR_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/COURS/COURS_ENRICHI_V2.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/SOURCAGE/SOURCE_ACCESS_LOG_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/SOURCAGE/TEEO_SOURCE_MASTER_INDEX_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/SOURCAGE/TEEO_SOURCE_MAPPING_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/SOURCAGE/COVERAGE_MATRIX_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/SOURCAGE/ARTIFACT_VALIDATION_MATRIX_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/SOURCAGE/GAP_ANALYSIS_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/SOURCAGE/TEEO_LEVEL_C_READINESS_CHECKLIST.md",

    "02_MVP_EXECUTABLE/03_CORPUS/GREFFE_IVOIRIEN/INDEX_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/SYSTEME_JUDICIAIRE_IVOIRIEN/INDEX_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/TRANSFORMATION_NUMERIQUE/INDEX_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/BIBLIOGRAPHIE/INDEX_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/TEXTES/INDEX_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/JURISPRUDENCE/INDEX_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/LIVING_GOVERNANCE_ENGINEERING/INDEX_V1.md",

    "docs/source_materials_index.md",
    "docs/cs_greffe_os/RESOURCE_INDEX_V1.md",
    "docs/cs_greffe_os/01_PROJECT_MEMORY/PROJECT_MEMORY_V1.md",
    "docs/cs_greffe_os/01_PROJECT_MEMORY/DECISION_LOG_V1.md",
    "docs/cs_greffe_os/01_PROJECT_MEMORY/STRATEGIC_DECISIONS_REGISTER_V1.md",
    "docs/cs_greffe_os/01_PROJECT_MEMORY/CHANGELOG_V1.md",
    "docs/cs_greffe_os/20_ROADMAP/PHASE_DOCUMENTATION_REGISTER_V1.md",
    "docs/cs_greffe_os/20_ROADMAP/CS_GREFFE_OS_COMPLETE_APPROACH_V1.md",

    "docs/cs_greffe_os/V1_EXECUTION/CS_GREFFE_OS_COMPLETE_PROJECT_TREE_V1.md",
    "docs/cs_greffe_os/V1_EXECUTION/CS_GREFFE_OS_V1_OFFICIAL_OPENING_V1.md",
    "docs/cs_greffe_os/V1_EXECUTION/CS_GREFFE_OS_V1_TOME_II_OPERATING_FRAMEWORK_V1.md",
    "docs/cs_greffe_os/V1_EXECUTION/V1_TRAJECTORY_AND_RISK_MONITORING_V1.md",
    "docs/cs_greffe_os/V1_EXECUTION/CRITICAL_IMPROVEMENT_BEFORE_VALIDATION_V1.md",
    "docs/cs_greffe_os/V1_EXECUTION/DIRECTIVE_ARTIFACT_BEFORE_CONVERSATION_CLOSURE_2026.md",
    "docs/cs_greffe_os/V1_EXECUTION/GLOBAL_PROJECT_AUDIT_REPORT_V1.md",
    "docs/cs_greffe_os/V1_EXECUTION/GLOBAL_PROJECT_AUDIT_ACTION_MATRIX_V1.csv",
    "docs/cs_greffe_os/V1_EXECUTION/GLOBAL_PROJECT_AUDIT_TOP_20_PRIORITIES_2026_2028_V1.md",
    "docs/cs_greffe_os/V1_EXECUTION/PROMPT_MERE_CONSOLIDE_TOME_II_V1.md",
    "docs/cs_greffe_os/V1_EXECUTION/PROMPT_MERE_VERIFIE_MVP_RELEASE_0_1.md",
    "docs/cs_greffe_os/V1_EXECUTION/PROMPT_MERE_VERIFIE_BUILD_THE_CORPUS_V1.md",
    "docs/cs_greffe_os/V1_EXECUTION/PROMPT_MERE_VERIFIE_RESEARCH_PROGRAM_2026_2040.md",
    "docs/cs_greffe_os/V1_EXECUTION/IMPLEMENTATION_GAP_MATRIX_V1.md",
    "docs/cs_greffe_os/V1_EXECUTION/SYSTEM_REALITY_AUDIT_V1.md",
    "docs/cs_greffe_os/V1_EXECUTION/DOCUMENTATION_TO_IMPLEMENTATION_MATRIX_V1.md",
    "docs/cs_greffe_os/V1_EXECUTION/PRIORITY_IMPLEMENTATION_REGISTER_V1.md",
    "docs/cs_greffe_os/V1_EXECUTION/V1_REALITY_SCORECARD_V1.md",
    "docs/cs_greffe_os/V1_EXECUTION/MVP_ARCHITECTURE_V2.md",
    "docs/cs_greffe_os/V1_EXECUTION/MVP_FEATURES_REGISTER_V2.md",
    "docs/cs_greffe_os/V1_EXECUTION/MVP_DATA_MODEL_V2.md",
    "docs/cs_greffe_os/V1_EXECUTION/MVP_UI_STRUCTURE_V2.md",
    "docs/cs_greffe_os/V1_EXECUTION/MVP_TRACEABILITY_FRAMEWORK_V2.md",
    "docs/cs_greffe_os/V1_EXECUTION/MVP_SCORECARD_V1.md",
    "docs/cs_greffe_os/V1_EXECUTION/RESEARCH_AGENDA_2026_2040_V2.md",
    "docs/cs_greffe_os/V1_EXECUTION/RESEARCH_DOMAINS_REGISTER_V1.md",
    "docs/cs_greffe_os/V1_EXECUTION/RESEARCH_QUESTIONS_REGISTER_V1.md",
    "docs/cs_greffe_os/V1_EXECUTION/BIBLIOGRAPHY_MASTER_INDEX_V1.md",
    "docs/cs_greffe_os/V1_EXECUTION/CORPUS_REGISTRY_V1.md",
    "docs/cs_greffe_os/V1_EXECUTION/IVORIAN_JUDICIAL_SYSTEM_KNOWLEDGE_MAP_V1.md",
    "docs/cs_greffe_os/V1_EXECUTION/IVORIAN_GREFFE_KNOWLEDGE_MAP_V1.md",
    "docs/cs_greffe_os/V1_EXECUTION/FUTURE_SCENARIOS_2030_2035_2040_V1.md",
]

created_dirs = []
created_files = []
existing_files = []
errors = []

def content_for(path: Path) -> str:
    name = path.name
    stem = path.stem

    if path.suffix == ".md":
        extra = ""
        if "GOVERNANCE" in name.upper() or "DECISION" in name.upper():
            extra = "\n\n> La confiance ne doit jamais progresser plus vite que l’usage.\n"
        return f"# {stem}\n\nDocument initial à compléter.{extra}"

    if path.suffix == ".csv":
        return "id,title,status,created_at\n"

    if path.suffix == ".py":
        return f"# {stem}\n# Script initial CS GREFFE OS V1\n"

    if path.suffix == ".sql":
        return f"-- {stem}\n-- Script SQL initial CS GREFFE OS V1\n"

    if name == ".gitignore":
        return "__pycache__/\n*.pyc\n.env\nvenv/\n.DS_Store\n"

    if name == "requirements.txt":
        return "# Dépendances CS GREFFE OS V1\nstreamlit\npandas\n"

    return ""

for directory in DIRS:
    try:
        path = ROOT / directory
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
            created_dirs.append(str(path.relative_to(ROOT)))
    except Exception as e:
        errors.append(f"{directory}: {e}")

for file in FILES:
    try:
        path = ROOT / file
        path.parent.mkdir(parents=True, exist_ok=True)

        if path.exists():
            existing_files.append(str(path.relative_to(ROOT)))
            continue

        path.write_text(content_for(path), encoding="utf-8")
        created_files.append(str(path.relative_to(ROOT)))
    except Exception as e:
        errors.append(f"{file}: {e}")

missing = []
for directory in DIRS:
    if not (ROOT / directory).exists():
        missing.append(directory)

for file in FILES:
    if not (ROOT / file).exists():
        missing.append(file)

print("\n# Rapport de création CS GREFFE OS V1\n")

print("## Dossier racine")
print(ROOT)

print("\n## Dossiers créés")
for item in created_dirs:
    print(f"- {item}")
if not created_dirs:
    print("- Aucun")

print("\n## Fichiers créés")
for item in created_files:
    print(f"- {item}")
if not created_files:
    print("- Aucun")

print("\n## Fichiers déjà existants")
for item in existing_files:
    print(f"- {item}")
if not existing_files:
    print("- Aucun")

print("\n## Éléments manquants")
for item in missing:
    print(f"- {item}")
if not missing:
    print("- Aucun")

print("\n## Erreurs")
for item in errors:
    print(f"- {item}")
if not errors:
    print("- Aucune")

print("\n## Conformité")
if not missing and not errors:
    print("Conformité : OUI")
else:
    print("Conformité : NON")
from pathlib import Path
import csv

ROOT = Path.cwd()

DIRS = [
    "cs_greffe_os/data",
    "02_MVP_EXECUTABLE/data",
    "02_MVP_EXECUTABLE/src/cs_learn",
    "02_MVP_EXECUTABLE/src/cs_research",
    "02_MVP_EXECUTABLE/src/strategic_command_center",
    "02_MVP_EXECUTABLE/src/knowledge_builder",
    "02_MVP_EXECUTABLE/tests",
    "02_MVP_EXECUTABLE/feedback",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/COURS",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/PLANS",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/FICHES",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/RESUMES",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/QCM",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/CAS_PRATIQUES",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/REFERENCES",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/SOURCAGE",
    "02_MVP_EXECUTABLE/03_CORPUS/GREFFE_IVOIRIEN",
    "02_MVP_EXECUTABLE/03_CORPUS/SYSTEME_JUDICIAIRE_IVOIRIEN",
    "02_MVP_EXECUTABLE/03_CORPUS/TRANSFORMATION_NUMERIQUE",
    "02_MVP_EXECUTABLE/03_CORPUS/BIBLIOGRAPHIE",
    "02_MVP_EXECUTABLE/03_CORPUS/TEXTES",
    "02_MVP_EXECUTABLE/03_CORPUS/JURISPRUDENCE",
    "02_MVP_EXECUTABLE/03_CORPUS/LIVING_GOVERNANCE_ENGINEERING",
    "docs/extractions",
    "docs/cs_greffe_os/01_PROJECT_MEMORY",
    "docs/cs_greffe_os/20_ROADMAP",
    "docs/cs_greffe_os/22_JDGO",
    "docs/cs_greffe_os/V1_EXECUTION",
    "source_materials",
    "scripts",
    "tests",
]

FILES = [
    "README.md",
    "requirements.txt",
    ".gitignore",
    "cs_greffe_os/app.py",
    "cs_greffe_os/data/modules.csv",
    "02_MVP_EXECUTABLE/app.py",

    "02_MVP_EXECUTABLE/feedback/CS_LEARN_IMPROVEMENTS.md",
    "02_MVP_EXECUTABLE/feedback/CS_LEARN_INFJ_USAGE_2026.md",
    "02_MVP_EXECUTABLE/feedback/CS_LEARN_KNOWLEDGE_GAPS.md",
    "02_MVP_EXECUTABLE/feedback/CS_LEARN_SESSION_HISTORY.md",
    "02_MVP_EXECUTABLE/feedback/IMPROVEMENT_BACKLOG_V1.md",
    "02_MVP_EXECUTABLE/feedback/ISSUES_REGISTER_V1.md",
    "02_MVP_EXECUTABLE/feedback/USAGE_LOG_V1.md",

    "02_MVP_EXECUTABLE/03_CORPUS/CORPUS_MASTER_INDEX_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CORPUS_BUILD_PLAN_2026_2040.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CORPUS_OPERATING_PLAN_2026_2028.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CORPUS_QUALITY_AND_METADATA_STANDARD_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CORPUS_PROGRESS_SCORECARD_V1.md",

    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/CS_LEARN_MASTER_INDEX_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/INDEX_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/USER_USAGE_LOG_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/USER_FEEDBACK_REGISTER_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/LESSONS_LEARNED_V2.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/VALUE_REGISTER_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/IMPROVEMENT_BACKLOG_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/CHANGE_LOG_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/VERSION_HISTORY_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/IMPACT_MEASUREMENT_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/COURS/PLAN_DIRECTEUR_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/COURS/COURS_ENRICHI_V2.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/SOURCAGE/SOURCE_ACCESS_LOG_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/SOURCAGE/TEEO_SOURCE_MASTER_INDEX_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/SOURCAGE/TEEO_SOURCE_MAPPING_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/SOURCAGE/COVERAGE_MATRIX_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/SOURCAGE/ARTIFACT_VALIDATION_MATRIX_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/SOURCAGE/GAP_ANALYSIS_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/SOURCAGE/TEEO_LEVEL_C_READINESS_CHECKLIST.md",

    "02_MVP_EXECUTABLE/03_CORPUS/GREFFE_IVOIRIEN/INDEX_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/SYSTEME_JUDICIAIRE_IVOIRIEN/INDEX_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/TRANSFORMATION_NUMERIQUE/INDEX_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/BIBLIOGRAPHIE/INDEX_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/TEXTES/INDEX_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/JURISPRUDENCE/INDEX_V1.md",
    "02_MVP_EXECUTABLE/03_CORPUS/LIVING_GOVERNANCE_ENGINEERING/INDEX_V1.md",

    "docs/source_materials_index.md",
    "docs/cs_greffe_os/RESOURCE_INDEX_V1.md",
    "docs/cs_greffe_os/01_PROJECT_MEMORY/PROJECT_MEMORY_V1.md",
    "docs/cs_greffe_os/01_PROJECT_MEMORY/DECISION_LOG_V1.md",
    "docs/cs_greffe_os/01_PROJECT_MEMORY/STRATEGIC_DECISIONS_REGISTER_V1.md",
    "docs/cs_greffe_os/01_PROJECT_MEMORY/CHANGELOG_V1.md",
    "docs/cs_greffe_os/20_ROADMAP/PHASE_DOCUMENTATION_REGISTER_V1.md",
    "docs/cs_greffe_os/20_ROADMAP/CS_GREFFE_OS_COMPLETE_APPROACH_V1.md",

    "docs/cs_greffe_os/V1_EXECUTION/CS_GREFFE_OS_COMPLETE_PROJECT_TREE_V1.md",
    "docs/cs_greffe_os/V1_EXECUTION/CS_GREFFE_OS_V1_OFFICIAL_OPENING_V1.md",
    "docs/cs_greffe_os/V1_EXECUTION/CS_GREFFE_OS_V1_TOME_II_OPERATING_FRAMEWORK_V1.md",
    "docs/cs_greffe_os/V1_EXECUTION/V1_TRAJECTORY_AND_RISK_MONITORING_V1.md",
    "docs/cs_greffe_os/V1_EXECUTION/CRITICAL_IMPROVEMENT_BEFORE_VALIDATION_V1.md",
    "docs/cs_greffe_os/V1_EXECUTION/DIRECTIVE_ARTIFACT_BEFORE_CONVERSATION_CLOSURE_2026.md",
    "docs/cs_greffe_os/V1_EXECUTION/GLOBAL_PROJECT_AUDIT_REPORT_V1.md",
    "docs/cs_greffe_os/V1_EXECUTION/GLOBAL_PROJECT_AUDIT_ACTION_MATRIX_V1.csv",
    "docs/cs_greffe_os/V1_EXECUTION/GLOBAL_PROJECT_AUDIT_TOP_20_PRIORITIES_2026_2028_V1.md",
    "docs/cs_greffe_os/V1_EXECUTION/PROMPT_MERE_CONSOLIDE_TOME_II_V1.md",
    "docs/cs_greffe_os/V1_EXECUTION/PROMPT_MERE_VERIFIE_MVP_RELEASE_0_1.md",
    "docs/cs_greffe_os/V1_EXECUTION/PROMPT_MERE_VERIFIE_BUILD_THE_CORPUS_V1.md",
    "docs/cs_greffe_os/V1_EXECUTION/PROMPT_MERE_VERIFIE_RESEARCH_PROGRAM_2026_2040.md",
    "docs/cs_greffe_os/V1_EXECUTION/IMPLEMENTATION_GAP_MATRIX_V1.md",
    "docs/cs_greffe_os/V1_EXECUTION/SYSTEM_REALITY_AUDIT_V1.md",
    "docs/cs_greffe_os/V1_EXECUTION/DOCUMENTATION_TO_IMPLEMENTATION_MATRIX_V1.md",
    "docs/cs_greffe_os/V1_EXECUTION/PRIORITY_IMPLEMENTATION_REGISTER_V1.md",
    "docs/cs_greffe_os/V1_EXECUTION/V1_REALITY_SCORECARD_V1.md",
    "docs/cs_greffe_os/V1_EXECUTION/MVP_ARCHITECTURE_V2.md",
    "docs/cs_greffe_os/V1_EXECUTION/MVP_FEATURES_REGISTER_V2.md",
    "docs/cs_greffe_os/V1_EXECUTION/MVP_DATA_MODEL_V2.md",
    "docs/cs_greffe_os/V1_EXECUTION/MVP_UI_STRUCTURE_V2.md",
    "docs/cs_greffe_os/V1_EXECUTION/MVP_TRACEABILITY_FRAMEWORK_V2.md",
    "docs/cs_greffe_os/V1_EXECUTION/MVP_SCORECARD_V1.md",
    "docs/cs_greffe_os/V1_EXECUTION/RESEARCH_AGENDA_2026_2040_V2.md",
    "docs/cs_greffe_os/V1_EXECUTION/RESEARCH_DOMAINS_REGISTER_V1.md",
    "docs/cs_greffe_os/V1_EXECUTION/RESEARCH_QUESTIONS_REGISTER_V1.md",
    "docs/cs_greffe_os/V1_EXECUTION/BIBLIOGRAPHY_MASTER_INDEX_V1.md",
    "docs/cs_greffe_os/V1_EXECUTION/CORPUS_REGISTRY_V1.md",
    "docs/cs_greffe_os/V1_EXECUTION/IVORIAN_JUDICIAL_SYSTEM_KNOWLEDGE_MAP_V1.md",
    "docs/cs_greffe_os/V1_EXECUTION/IVORIAN_GREFFE_KNOWLEDGE_MAP_V1.md",
    "docs/cs_greffe_os/V1_EXECUTION/FUTURE_SCENARIOS_2030_2035_2040_V1.md",
]

created_dirs = []
created_files = []
existing_files = []
errors = []

def content_for(path: Path) -> str:
    name = path.name
    stem = path.stem

    if path.suffix == ".md":
        extra = ""
        if "GOVERNANCE" in name.upper() or "DECISION" in name.upper():
            extra = "\n\n> La confiance ne doit jamais progresser plus vite que l’usage.\n"
        return f"# {stem}\n\nDocument initial à compléter.{extra}"

    if path.suffix == ".csv":
        return "id,title,status,created_at\n"

    if path.suffix == ".py":
        return f"# {stem}\n# Script initial CS GREFFE OS V1\n"

    if path.suffix == ".sql":
        return f"-- {stem}\n-- Script SQL initial CS GREFFE OS V1\n"

    if name == ".gitignore":
        return "__pycache__/\n*.pyc\n.env\nvenv/\n.DS_Store\n"

    if name == "requirements.txt":
        return "# Dépendances CS GREFFE OS V1\nstreamlit\npandas\n"

    return ""

for directory in DIRS:
    try:
        path = ROOT / directory
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
            created_dirs.append(str(path.relative_to(ROOT)))
    except Exception as e:
        errors.append(f"{directory}: {e}")

for file in FILES:
    try:
        path = ROOT / file
        path.parent.mkdir(parents=True, exist_ok=True)

        if path.exists():
            existing_files.append(str(path.relative_to(ROOT)))
            continue

        path.write_text(content_for(path), encoding="utf-8")
        created_files.append(str(path.relative_to(ROOT)))
    except Exception as e:
        errors.append(f"{file}: {e}")

missing = []
for directory in DIRS:
    if not (ROOT / directory).exists():
        missing.append(directory)

for file in FILES:
    if not (ROOT / file).exists():
        missing.append(file)

print("\n# Rapport de création CS GREFFE OS V1\n")

print("## Dossier racine")
print(ROOT)

print("\n## Dossiers créés")
for item in created_dirs:
    print(f"- {item}")
if not created_dirs:
    print("- Aucun")

print("\n## Fichiers créés")
for item in created_files:
    print(f"- {item}")
if not created_files:
    print("- Aucun")

print("\n## Fichiers déjà existants")
for item in existing_files:
    print(f"- {item}")
if not existing_files:
    print("- Aucun")

print("\n## Éléments manquants")
for item in missing:
    print(f"- {item}")
if not missing:
    print("- Aucun")

print("\n## Erreurs")
for item in errors:
    print(f"- {item}")
if not errors:
    print("- Aucune")

print("\n## Conformité")
if not missing and not errors:
    print("Conformité : OUI")
else:
    print("Conformité : NON")

