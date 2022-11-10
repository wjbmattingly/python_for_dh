import streamlit as st
import pandas as pd

st.header("Preparing the Data")
df = pd.read_csv("data/titanic.csv")
df = df[["Age", "Survived"]]
chart_df = df.groupby(["Age"]).sum()
chart_df["Age"] = chart_df.index
st.write("Code for cleaning the DataFrame")
df_code = """
df = pd.read_csv("data/titanic.csv")
df = df[["Age", "Survived"]]
chart_df = df.groupby(["Age"]).sum()
chart_df["Age"] = chart_df.index
"""

st.code(df_code, language="python")
st.write(chart_df)


st.header("Line Chart")
line_chart_code = """
st.line_chart(chart_df, x="Age", y=["Survived"])
"""
st.code(line_chart_code, language="python")
st.line_chart(chart_df, x="Age", y=["Survived"])

st.header("Bar Chart")
bar_chart_code = """
st.line_chart(chart_df, x="Age", y=["Survived"])
"""
st.code(bar_chart_code, language="python")
st.bar_chart(chart_df, x="Age", y=["Survived"])

st.header("Area Chart")
area_chart_code = """
st.line_chart(chart_df, x="Age", y=["Survived"])
"""
st.code(area_chart_code, language="python")
st.area_chart(chart_df, x="Age", y=["Survived"])
