import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import streamlit as st

df = pd.read_csv('diffavg_5.csv', header=None)

st.write("CSVdata:")
st.dataframe(df)

st.line_chart(df)
