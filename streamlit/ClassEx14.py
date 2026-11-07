import streamlit as st


st.title("My First Streamlit Application")
st.text_input("Enter your name")
st.text_area("Enter your address")
st.selectbox("Select your gender", ["Male", "Female", "Other"])
st.multiselect("Select your hobbies", ["Reading", "Traveling", "Sports", "Music"])


import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [20, 22, 21, 23],
    "Department": ["Computer Science", "Mathematics", "Physics", "Chemistry"]
}
df = pd.DataFrame(data)

tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
with tab1:
    st.text_area("This is Tab 1")
with tab2:
    st.selectbox("This is Tab 2", ["Option 1", "Option 2", "Option 3"])
with tab3:
    st.dataframe(df)
    st.line_chart(df[["Age"]])

st.sidebar.title("Filter Options")
course= st.sidebar.selectbox("Select your course", ["Python", "Java", "C++", "JavaScript"])
year = st.sidebar.selectbox("Select your year", ["1st Year", "2nd Year", "3rd Year", "4th Year"])