import streamlit as st
import datetime
st.title("My First Streamlit Application")
name = st.text_input("Enter your name")
register_number = st.text_input("Enter your register number")
programme = st.selectbox("Select your Programme", ["B.Tech", "M.Tech", "PhD","MCA"])
semester = st.radio("Select your semester", ["1st Sem", "2nd Sem", "3rd Sem", "4th Sem","5th Sem","6th Sem","7th Sem","8th Sem"])
subjects = st.multiselect("Select your subjects", ["Python", "Java", "C++", "JavaScript","Data Structures","DBMS","Operating Systems"])
date_of_birth = st.date_input("Select your date of birth")
if date_of_birth>datetime.date.today():
    st.error("Date of birth cannot be in the future.")
time = st.time_input("Select your preferred meeting time")
age = st.number_input("Enter your age", min_value=0, max_value=100)
profile_picture = st.file_uploader("Upload your profile picture", type=["jpg", "jpeg", "png"])
terms_accepted = st.checkbox("I agree to the terms and conditions")
submit_button = st.button("Submit")
if submit_button and not terms_accepted:
    st.error("You must accept the terms and conditions to submit the form.")
if submit_button and terms_accepted:
    st.success("Form Submitted Successfully!")
    st.write("Name:", name)
    st.write("Register Number:", register_number)
    st.write("Programme:", programme)
    st.write("Semester:", semester) 
    st.write("Subjects:", subjects)
    st.write("Date of Birth:", date_of_birth)
    st.write("Preferred Meeting Time:", time)
    st.write("Age:", age)
    if profile_picture is not None:
        st.image(profile_picture, caption="Profile Picture", use_column_width=True) 
    st.write("Terms Accepted:", terms_accepted)