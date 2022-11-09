import streamlit as st

st.title("Data Selection Widgets")

#Getting user input from st.checkbox()
st.subheader("Boolean Input with st.checkbox()")
checkbox_code = """
checked = st.checkbox("Select this checkbox")
st.write(f"Current state of checkbox: {checked}")
"""
st.code(checkbox_code, language="python")
checked = st.checkbox("Select this checkbox")
st.write(f"Current state of checkbox: {checked}")
st.write("---")


#Getting user input from st.button()
st.subheader("Boolean Input with st.button()")
button_code = """
state = st.button("Click to Change current state")
st.write(f"Button has been pressed: {state}")
"""
st.code(button_code, language="python")
state = st.button("Press Button")
st.write(f"Button has been pressed: {state}")
st.write("---")

#Getting user input from st.checkbox()
st.subheader("Selection with st.radio()")
radio_code = """
options = ["Red", "Blue", "Yellow"]
radio_selection = st.radio("Select Color", options)
st.write(f"Color selected is {radio_selection}")
"""
st.code(radio_code, language="python")
options = ["Red", "Blue", "Yellow"]
radio_selection = st.radio("Select Color", options)
st.write(f"Color selected is {radio_selection}")
st.write("---")


#Getting user input from st.checkbox()
st.subheader("Selection with st.selectbox()")
selectbox_code = """
options = ["Red", "Blue", "Yellow"]
selectbox_selection = st.selectbox("Select Color", options)
st.write(f"Color selected is {selectbox_selection}")
"""
st.code(selectbox_code, language="python")
options = ["Red", "Blue", "Yellow"]
selectbox_selection = st.selectbox("Select Color", options)
st.write(f"Color selected is {selectbox_selection}")
st.write("---")


#Getting user input from st.multiselect()
st.subheader("Selection with st.multiselect()")
multiselect_code = """
options = ["Red", "Blue", "Yellow"]
multiselect_selection = st.multiselect("Select Color", options)
st.write(f"Color selected is {multiselect_selection}")
"""
st.code(multiselect_code, language="python")
options = ["Red", "Blue", "Yellow"]
multiselect_selection = st.multiselect("Select Color", options)
st.write(f"Color selected is {multiselect_selection}")
st.write("---")
