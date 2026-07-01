import streamlit as st

def render_strategic_command_center():
    st.title("Strategic Command Center")
    st.caption("Pilotage du projet — Release 0.1")

    st.metric("TEEO", "48%", "Niveau D")
    st.metric("Release 0.2", "Gelée")
    st.metric("Nouvelle matière", "Interdite")

    st.subheader("Priorités")
    st.write([
        "TEEO V2.7 — IMPROVE",
        "Sourcer les supports INFJ",
        "Recueillir un feedback utilisateur réel",
        "Mesurer une amélioration effective",
    ])
