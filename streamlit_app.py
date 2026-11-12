import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Streamlit Hello", page_icon="📊")
st.title("📊 Streamlit Hello")
st.write("A small demo app: pick a number of points and see a random walk.")

n = st.slider("Number of points", 10, 500, 100)
seed = st.number_input("Random seed", value=42, step=1)
rng = np.random.default_rng(int(seed))
df = pd.DataFrame({"value": rng.standard_normal(n).cumsum()})
st.line_chart(df)
st.dataframe(df.describe().T)
