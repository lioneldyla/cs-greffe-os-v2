import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

# SCHEMA : colonnes minimales requises par table (alignees sur les CSV reels).
# Les colonnes supplementaires presentes dans les CSV sont preservees et affichees.
SCHEMA: dict[str, list[str]] = {
    "modules": ["module_id", "title"],
    "students": ["student_id", "nom", "prenom", "email", "promotion", "statut"],
    "scores": ["score_id", "student_id", "module_id", "score", "progression", "date_eval"],
    "lessons": ["lesson_id", "module_id", "titre"],
    "questions": ["question_id", "lesson_id", "enonce"],
    "attempts": ["attempt_id", "student_id", "question_id", "correcte", "score_obtenu", "date_tentative"],
    "corrections": ["correction_id", "attempt_id"],
    "sources": ["source_id", "module_id", "titre"],
    "audit_logs": ["log_id", "user_id", "action"],
}


def _read_csv(path: Path, required: bool = False) -> pd.DataFrame:
    """Read a CSV with defensive defaults."""
    try:
        return pd.read_csv(path)
    except FileNotFoundError:
        if required:
            raise
        st.warning(f"CSV manquant : {path.name}")
        return pd.DataFrame()
    except Exception as e:
        st.warning(f"Erreur de lecture CSV ({path.name}) : {e}")
        return pd.DataFrame()


def _validate_schema(df: pd.DataFrame, name: str) -> pd.DataFrame:
    """Validate that required columns are present; warn and return empty df if not."""
    required = SCHEMA.get(name, [])
    missing = [col for col in required if col not in df.columns]
    if missing:
        st.warning(
            f"Colonnes manquantes dans {name}.csv : {missing}. "
            "Verifiez le fichier CSV."
        )
        return pd.DataFrame()
    return df


@st.cache_data
def load_data() -> dict[str, pd.DataFrame]:
    raw = {
        name: _read_csv(DATA_DIR / f"{name}.csv")
        for name in SCHEMA
    }
    return {name: _validate_schema(df, name) for name, df in raw.items()}


def compute_metrics(datasets: dict[str, pd.DataFrame]) -> dict[str, float]:
    modules = datasets["modules"]
    students = datasets["students"]
    scores = datasets["scores"]

    metrics: dict[str, float] = {
        "modules": float(len(modules)),
        "students": float(len(students)),
        "moyenne_generale": 0.0,
        "progression_moyenne": 0.0,
    }
    if not scores.empty:
        metrics["moyenne_generale"] = float(scores["score"].mean())
        metrics["progression_moyenne"] = float(scores["progression"].mean())
    return metrics


def _chart_moyenne_module(
    scores: pd.DataFrame, modules: pd.DataFrame
) -> None:
    """Affiche le graphique Moyenne par module (factorise)."""
    if scores.empty or modules.empty:
        st.info(
            "Chargez les CSV `modules.csv` et `scores.csv` "
            "pour visualiser les statistiques."
        )
        return
    module_avg = (
        scores.merge(modules, on="module_id")
        .groupby(["module_id", "title"], as_index=False)["score"]
        .mean()
    )
    st.plotly_chart(
        px.bar(
            module_avg,
            x="title",
            y="score",
            title="Moyenne par module",
            labels={"score": "Moyenne /20", "title": "Module"},
        ),
        use_container_width=True,
    )
    low = module_avg[module_avg["score"] < 14]
    if not low.empty:
        st.warning("Modules avec une moyenne inferieure a 14/20")
        st.dataframe(low)


def app() -> None:
    st.set_page_config(page_title="CS GREFFE OS Learn", layout="wide")

    st.title("CS GREFFE OS Learn")
    st.subheader("MVP cloud e-learning INFJ")
    st.caption("Donnees fictives uniquement - aucune donnee judiciaire reelle.")

    datasets = load_data()
    metrics = compute_metrics(datasets)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Nombre de modules", f"{metrics['modules']:.0f}")
    col2.metric("Nombre d'eleves", f"{metrics['students']:.0f}")
    col3.metric("Moyenne generale", f"{metrics['moyenne_generale']:.1f}/20")
    col4.metric("Progression moyenne", f"{metrics['progression_moyenne']:.0f}%")

    tabs = st.tabs(
        [
            "Vue generale",
            "Modules",
            "Eleves",
            "Performance",
            "Data Model",
            "Gouvernance",
        ]
    )
    tab_overview, tab_modules, tab_students, tab_perf, tab_model, tab_gov = tabs

    modules = datasets["modules"]
    students = datasets["students"]
    scores = datasets["scores"]

    with tab_overview:
        st.subheader("Vue generale")
        _chart_moyenne_module(scores, modules)
        if not modules.empty:
            st.markdown("**Catalogue des modules**")
            st.dataframe(modules, use_container_width=True)

    with tab_modules:
        st.subheader("Modules")
        st.dataframe(modules, use_container_width=True)

    with tab_students:
        st.subheader("Eleves")
        if not students.empty:
            promotions = sorted(students["promotion"].dropna().unique().tolist())
            selected = st.multiselect(
                "Filtrer par promotion", promotions, default=promotions
            )
            filtered = students[students["promotion"].isin(selected)] if selected else students
            st.dataframe(filtered, use_container_width=True)
        else:
            st.info("Le fichier `students.csv` est vide ou absent.")

    with tab_perf:
        st.subheader("Performance")
        if scores.empty:
            st.info("Le fichier `scores.csv` est vide ou absent.")
        else:
            if "date_eval" in scores.columns:
                dates = sorted(scores["date_eval"].dropna().unique().tolist())
                selected_dates = st.multiselect(
                    "Filtrer par date d'evaluation", dates, default=dates
                )
                scores_filtered = (
                    scores[scores["date_eval"].isin(selected_dates)]
                    if selected_dates
                    else scores
                )
            else:
                scores_filtered = scores

            _chart_moyenne_module(scores_filtered, modules)

            if not students.empty:
                progression = (
                    scores_filtered.merge(students, on="student_id")
                    .groupby(["student_id", "nom"], as_index=False)["progression"]
                    .mean()
                )
                st.plotly_chart(
                    px.bar(
                        progression,
                        x="nom",
                        y="progression",
                        title="Progression moyenne par eleve",
                        labels={"progression": "Progression (%)", "nom": "Eleve"},
                    ),
                    use_container_width=True,
                )

    with tab_model:
        st.subheader("Tables Data Model (fictives)")
        for name in [
            "lessons",
            "questions",
            "attempts",
            "corrections",
            "sources",
            "audit_logs",
        ]:
            df = datasets.get(name, pd.DataFrame())
            st.markdown(f"**{name}**")
            st.dataframe(df, use_container_width=True)

    with tab_gov:
        st.subheader("Gouvernance")
        st.markdown(
            """
            - Donnees fictives uniquement - aucune donnee judiciaire reelle.
            - Aucun secret / aucune cle API.
            - Aucune connexion Snowflake active.
            - Aucune connexion OpenAI active.
            - IA future sous validation humaine.
            """
        )


if __name__ == "__main__":
    app()
