import streamlit as st

#Displaying text with st.title()
st.title("This a Title.")
st.code("""st.title("This a Title.")""", language="python")
st.write("---")

#Displaying text with st.header()
st.header("This a Header.")
st.code("""st.header("This a Header.")""", language="python")
st.write("---")

#Displaying text with st.subheader()
st.header("This a Subheader.")
st.code("""st.header("This a Subheader.")""", language="python")
st.write("---")

#Displaying text with st.write()
st.write("This is text.")
st.code("""st.write("This is text.")""", language="python")
st.write("---")

#Displaying text with st.caption()
st.caption("This a Caption.")
st.code("""st.caption("This a Caption.")""", language="python")
st.write("---")

#Displaying text with st.markdown()
with open("./markdown/sample.md", "r") as f:
    markdown_text = f.read()
st.markdown(markdown_text)
markdown_code = """
with open("./markdown/sample.md", "r") as f:
    markdown_text = f.read()
st.markdown(markdown_text)
"""
st.code(markdown_code, language="python")
