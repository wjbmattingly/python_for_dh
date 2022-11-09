import streamlit as st
import datetime

st.title("Data Input Widgets")

#Getting user input from st.text_input()
st.subheader("Text Input with st.text_input()")
text_input_code = """
user_text = st.text_input("Input some text here")
st.write(user_text)
"""
st.code(text_input_code, language="python")
user_text = st.text_input("Input some text here")
st.write(user_text)
st.write("---")

#Getting user input from st.text_input() with default value
st.subheader("Text Input with st.text_input() and Default Text")
text_input_code = """
default_text = st.text_input("Input some text here", "default text")
st.write(default_text)
"""
st.code(text_input_code, language="python")
default_text = st.text_input("Input some text here", "default text")
st.write(default_text)
st.write("---")


#Getting user input from st.text_area()
st.subheader("Text Input with st.text_area()")
text_area_code = """
user_text = st.text_area("Input some text here")
st.write(user_text)
"""
st.code(text_area_code, language="python")
user_text = st.text_area("Input some text here")
st.write(user_text)
st.write("---")

#Getting user input from st.text_input() with default value
st.subheader("Text Input with st.text_area() and Default Text")
text_area_code = """
default_text = st.text_area("Input some text here", "default text")
st.write(default_text)
"""
st.code(text_area_code, language="python")
default_text = st.text_area("Input some text here", "default text")
st.write(default_text)
st.write("---")



#Getting user input from st.number_input()
st.subheader("Numerical Input with st.number_input()")
number_input_code = """
user_number = st.number_input("Input Number",
                            min_value=1,
                            max_value=10,
                            value=5,
                            step=1)
st.write(user_number)
"""
st.code(number_input_code, language="python")
user_number = st.number_input("Input Number",
                            min_value=1,
                            max_value=10,
                            value=5,
                            step=1)
st.write(user_number)
st.write("---")



#Getting user input from st.slider()
st.subheader("Numerical Input with st.slider()")
slider_input_code = """
slider_number = st.slider("Select your Number",
                            min_value=1,
                            max_value=10,
                            value=5,
                            step=1)
st.write(slider_number)
"""
st.code(slider_input_code, language="python")
slider_number = st.slider("Select your Number",
                            min_value=1,
                            max_value=10,
                            value=5,
                            step=1)
st.write(slider_number)
st.write("---")


#Getting user input from st.date_input()
st.subheader("Date Input with st.date_input()")
date_input_code = """
import datetime
user_date = st.date_input("Select your Date",
                            value = datetime.date(2000, 6, 12),
                            min_value = datetime.date(2000, 1, 12),
                            max_value = datetime.date(2001, 1, 12)
                            )

st.write(user_date)
"""
st.code(date_input_code, language="python")
user_date = st.date_input("Select your Date",
                            value = datetime.date(2000, 6, 12),
                            min_value = datetime.date(2000, 1, 12),
                            max_value = datetime.date(2001, 1, 12)
                            )

st.write(user_date)
st.write("---")
