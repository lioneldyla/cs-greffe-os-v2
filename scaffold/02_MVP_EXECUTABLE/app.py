import streamlit as st

from src.cs_learn.page import render_cs_learn
from src.cs_research.page import render_cs_research
from src.strategic_command_center.page import render_strategic_command_center

st.set_page_config(page_title="CS GREFFE OS V1", layout="wide")

PAGES = {
    "Accueil": "home",
    "CS Learn": "learn",
    "CS Research": "research",
    "Strategic Command Center": "command",
    "About": "about",
}

choice = st.sidebar.radio("Navigation", list(PAGES.keys()))

if choice == "Accueil":
    st.title("CS GREFFE OS V1 — MVP Release 0.1")
    st.markdown("""
    **Principe : Small, Simple and Governed**

    Modules autorisés :
    - CS Learn
    - CS Research
    - Strategic Command Center

    Orientation actuelle : **BUILD THE CORPUS** avant toute Release 0.2.
    """)
elif choice == "CS Learn":
    render_cs_learn()
elif choice == "CS Research":
    render_cs_research()
elif choice == "Strategic Command Center":
    render_strategic_command_center()
else:
    st.title("About / Boundaries")
    st.markdown("""
    Ce MVP est un démonstrateur pédagogique non sensible.

    Exclusions :
    - pas de production ;
    - pas de données judiciaires sensibles ;
    - pas d'agents autonomes ;
    - pas de décision automatisée.
    """)
