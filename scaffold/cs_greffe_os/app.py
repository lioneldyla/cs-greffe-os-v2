from pathlib import Path
import pandas as pd
import streamlit as st

DATA_PATH = Path(__file__).parent / "data" / "modules.csv"

st.set_page_config(page_title="CS GREFFE OS Learn", layout="wide")
st.title("CS GREFFE OS — Learn")

if DATA_PATH.exists():
    df = pd.read_csv(DATA_PATH)
    st.dataframe(df)
else:
    st.warning("Aucune donnée de module trouvée.")
