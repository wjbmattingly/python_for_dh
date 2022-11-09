import streamlit as st

st.title("Streamlit Demo Application")

with open("./markdown/about.md", "r") as f:
    about_text = f.read()

st.markdown(about_text, unsafe_allow_html=True)
