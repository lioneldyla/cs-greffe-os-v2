import streamlit as st
from .search import list_subjects, search_files

def render_cs_learn():
    st.title("CS Learn")
    st.caption("Bibliothèque vivante et apprentissage — Release 0.1")

    subjects = list_subjects()
    st.subheader("Matières disponibles")
    st.write(subjects or "Aucune matière disponible.")

    query = st.text_input("Recherche CS Learn")
    if query:
        results = search_files(query)
        st.write(results if results else "Aucun résultat.")
