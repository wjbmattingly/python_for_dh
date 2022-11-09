import streamlit as st
import pandas as pd

df = pd.read_csv("data/titanic.csv")
df = df[:20]

# Displaying data with st.write()
st.header("Displaying a Table with st.write()")
st.write(df)
st.write("---")

# Displaying data with st.dataframe()
st.header("Displaying a Table with st.dataframe()")
st.dataframe(df, height=750)
st.write("---")

# Displaying data with st.table()
st.header("Displaying a Table with st.table()")
st.table(df)
st.write("---")

# Displaying data with st.markdown()
st.header("Displaying a Table with st.markdown()")
st.markdown(df.to_markdown())
