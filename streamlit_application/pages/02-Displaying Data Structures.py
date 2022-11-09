import streamlit as st

st.title("Displaying Data Structures in Streamlit")

#Displaying Data with st.write()
st.subheader("Displaying Data with st.write()")
names = {"people": ["Tom", "Mary", "Fred", "Stephanie"]}
st.code("""names = {"people": ["Tom", "Mary", "Fred", "Stephanie"]}""", language="python")
st.write(names)
st.code("""st.write(names)""", language="python")



#Displaying Data with st.json()
st.write("---")
st.subheader("Displaying Data with st.json()")
names = {"people": ["Tom", "Mary", "Fred", "Stephanie"]}
st.code("""names = {"people": ["Tom", "Mary", "Fred", "Stephanie"]}""", language="python")
st.json(names)
st.code("""st.json(names)""", language="python")


#Displaying Data with st.json and expanded()
st.write("---")
st.subheader("Displaying Data with st.json() and Expanded")
names = {"people": ["Tom", "Mary", "Fred", "Stephanie"]}
st.code("""names = {"people": ["Tom", "Mary", "Fred", "Stephanie"]}""", language="python")
st.json(names, expanded=False)
st.code("""st.json(names, expanded=False)""", language="python")
