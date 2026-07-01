import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"


def _read_csv(path: Path, required: bool = False) -> pd.DataFrame:
    '''Read a CSV with defensive defaults.

    required=True will raise if the CSV is missing (developer signal).
    '''
    try:
        return pd.read_csv(path)
    except FileNotFoundError:
        if required:
            raise
        st.warning(f"CSV manquant (mode développeur): {path.name}")
        return pd.DataFrame()
    except Exception as e:
        st.warning(f"Erreur de lecture CSV ({path.name}) : {e}")
        return pd.DataFrame()


@st.cache_data
def load_data() -> dict[str, pd.DataFrame]:
    data = {
        "modules": _read_csv(DATA_DIR / "modules.csv"),
        "students": _read_csv(DATA_DIR / "students.csv"),
        "scores": _read_csv(DATA_DIR / "scores.csv"),
        "lessons": _read_csv(DATA_DIR / "lessons.csv"),
        "questions": _read_csv(DATA_DIR / "questions.csv"),
        "attempts": _read_csv(DATA_DIR / "attempts.csv"),
        "corrections": _read_csv(DATA_DIR / "corrections.csv"),
        "sources": _read_csv(DATA_DIR / "sources.csv"),
        "audit_logs": _read_csv(DATA_DIR / "audit_logs.csv"),
    }
    return data


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


def app() -> None:
    st.set_page_config(page_title="CS GREFFE OS Learn", layout="wide")

    st.title("CS GREFFE OS Learn")
    st.subheader("MVP cloud e-learning INFJ")
    st.caption("Données fictives uniquement — aucune donnée judiciaire réelle.")

    datasets = load_data()
    metrics = compute_metrics(datasets)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Nombre de modules", f"{metrics['modules']:.0f}")
    col2.metric("Nombre d'élèves", f"{metrics['students']:.0f}")
    col3.metric("Moyenne générale", f"{metrics['moyenne_generale']:.1f}/20")
    col4.metric("Progression moyenne", f"{metrics['progression_moyenne']:.0f}%")

    tabs = st.tabs(
        [
            "Vue générale",
            "Modules",
            "Élèves",
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
        st.subheader("Vue générale")
        if scores.empty or modules.empty:
            st.info(
                "Chargez les CSV `modules.csv`, `students.csv` et `scores.csv` "
                "pour visualiser les statistiques."
            )
        else:
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
                st.warning("Modules avec une moyenne inférieure à 14/20")
                st.dataframe(low)

    with tab_modules:
        st.subheader("Modules")
        st.dataframe(modules)

    with tab_students:
        st.subheader("Élèves")
        st.dataframe(students)

    with tab_perf:
        st.subheader("Performance")
        if scores.empty:
            st.info("Le fichier `scores.csv` est vide ou absent.")
        else:
            if not modules.empty:
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

            progression = (
                scores.merge(students, on="student_id")
                .groupby(["student_id", "nom"], as_index=False)["progression"]
                .mean()
            )
            st.plotly_chart(
                px.bar(
                    progression,
                    x="nom",
                    y="progression",
                    title="Progression moyenne par élève",
                    labels={"progression": "Progression (%)", "nom": "Élève"},
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
            st.dataframe(df)

    with tab_gov:
        st.subheader("Gouvernance")
        st.markdown(
            '''
- Données fictives uniquement — aucune donnée judiciaire réelle.
- Aucun secret / aucune clé API.
- Aucune connexion Snowflake active.
- Aucune connexion OpenAI active.
- IA future sous validation humaine.
            '''
        )


if __name__ == "__main__":
    app()
