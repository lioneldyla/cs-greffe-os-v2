import streamlit as st
from .search import search_corpus

def render_cs_research():
    st.title("CS Research")
    st.caption("Recherche documentaire et analytique — Release 0.1")

    query = st.text_input("Recherche corpus")
    if query:
        results = search_corpus(query)
        st.write(results if results else "Aucun résultat.")
