"""Script de scaffolding idempotent pour CS GREFFE OS V1.

Usage : python scripts/create_cs_greffe_os_tree_v1.py
La racine du projet est automatiquement detectee a partir du fichier lui-meme.
"""
from pathlib import Path

# Racine du depot = parent du dossier scripts/
ROOT = Path(__file__).resolve().parent.parent

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
        "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/COURS/PLAN_DIRECTEUR_V1.md",
        "02_MVP_EXECUTABLE/03_CORPUS/CS_LEARN/TEEO/COURS/COURS_ENRICHI_V2.md",
        "02_MVP_EXECUTABLE/03_CORPUS/GREFFE_IVOIRIEN/INDEX_V1.md",
        "02_MVP_EXECUTABLE/03_CORPUS/SYSTEME_JUDICIAIRE_IVOIRIEN/INDEX_V1.md",
        "02_MVP_EXECUTABLE/03_CORPUS/TRANSFORMATION_NUMERIQUE/INDEX_V1.md",
        "02_MVP_EXECUTABLE/03_CORPUS/BIBLIOGRAPHIE/INDEX_V1.md",
        "02_MVP_EXECUTABLE/03_CORPUS/TEXTES/INDEX_V1.md",
        "02_MVP_EXECUTABLE/03_CORPUS/JURISPRUDENCE/INDEX_V1.md",
        "02_MVP_EXECUTABLE/03_CORPUS/LIVING_GOVERNANCE_ENGINEERING/INDEX_V1.md",
        "docs/source_materials_index.md",
        "docs/cs_greffe_os/RESOURCE_INDEX_V1.md",
]


def content_for(path: Path) -> str:
        name = path.name
        stem = path.stem

    if path.suffix == ".md":
                extra = ""
                if "GOVERNANCE" in name.upper() or "DECISION" in name.upper():
                                extra = "\n\n> La confiance ne doit jamais progresser plus vite que l'usage.\n"
                            return f"# {stem}\n\nDocument initial a completer.{extra}"

    if path.suffix == ".csv":
                return "id,title,status,created_at\n"

    if path.suffix == ".py":
                return f"# {stem}\n# Script initial CS GREFFE OS V1\n"

    if name == ".gitignore":
                return "__pycache__/\n*.pyc\n.env\nvenv/\n.DS_Store\n"

    if name == "requirements.txt":
                return "streamlit>=1.35,<2\npandas>=2.0,<3\nplotly>=5.18,<6\n"

    return ""


def main() -> None:
        created_dirs: list[str] = []
    created_files: list[str] = []
    existing_files: list[str] = []
    errors: list[str] = []

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

    missing = [
                item
                for item in DIRS + FILES
                if not (ROOT / item).exists()
    ]

    print("\n# Rapport de creation CS GREFFE OS V1\n")
    print(f"## Dossier racine\n{ROOT}\n")

    print("## Dossiers crees")
    for item in created_dirs or ["- Aucun"]:
                print(f"- {item}")

    print("\n## Fichiers crees")
    for item in created_files or ["- Aucun"]:
                print(f"- {item}")

    print("\n## Fichiers deja existants")
    for item in existing_files or ["- Aucun"]:
                print(f"- {item}")

    print("\n## Elements manquants")
    for item in missing or ["- Aucun"]:
                print(f"- {item}")

    print("\n## Erreurs")
    for item in errors or ["- Aucune"]:
                print(f"- {item}")

    print("\n## Conformite")
    print("Conformite : OUI" if not missing and not errors else "Conformite : NON")


if __name__ == "__main__":
        main()
