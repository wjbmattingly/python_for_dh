import streamlit as st

st.title("Metrics")
text = st.text_area("Paste text here to get word count.", "This is some default text.")

st.header("Without Change")
no_change_code = """
text = st.text_area("Paste text here to get word count.", "This is some default text.")
word_count = len(text.split())
st.metric("Word Count", word_count)
"""
st.code(no_change_code, language="python")
word_count = len(text.split())
st.metric("Word Count", word_count)

st.header("With Change")
with_change_code = """
if "prev_word_count" not in st.session_state:
    st.session_state["prev_word_count"] = 5
text = st.text_area("Paste text here to get word count.", "This is some default text.")
word_count = len(text.split())
change = word_count-st.session_state.prev_word_count
st.metric("Word Count", word_count, change)
st.session_state.prev_word_count = word_count
"""
st.code(with_change_code, language="python")
if "prev_word_count" not in st.session_state:
    st.session_state["prev_word_count"] = 5
change = word_count-st.session_state.prev_word_count
st.metric("Word Count", word_count, change)
st.session_state.prev_word_count = word_count
