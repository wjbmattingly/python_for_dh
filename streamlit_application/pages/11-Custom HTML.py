import streamlit as st

html = """
<a style='background:yellow'>This text has a yellow background</a>
"""
st.header("Without unsafe_allow_html=True")
st.markdown(html)
st.write("---")

st.header("With unsafe_allow_html=True")
st.markdown(html, unsafe_allow_html=True)
