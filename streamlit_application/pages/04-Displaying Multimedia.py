import streamlit as st

st.title("Displaying Multimedia")


st.header("Displaying an Image")
st.image("data/si_logo.jpg")
st.code("""st.image("data/si_logo.jpg")""", language="python")


st.header("Play Audio")
st.write("Hit play to listen to this whale sound from PMEL Acoustics Program.")
st.audio("https://www.pmel.noaa.gov/acoustics/whales/sounds/whalewav/ak52_10x.wav")
st.code("""st.audio("https://www.pmel.noaa.gov/acoustics/whales/sounds/whalewav/ak52_10x.wav")""", language="python")
