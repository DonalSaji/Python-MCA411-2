import streamlit as st
import datetime
st.title("Student Information System")
st.header("Enter Student Details")
st.subheader("Please fill in the following information:")
st.text_input("department of computer science")
st.write("Programmme : MCA")
st.caption("This application is designed to collect student information for the MCA program in the Department of Computer Science.")
st.code("print('Hello, Streamlit!')", language="python")


st.success("Thank you for providing your information!")
st.warning("Please ensure that all fields are filled out correctly.")
st.error("Error: Some fields are missing or incorrect. Please review your input.")
st.info("This application is for demonstration purposes only.")
st.exception("An unexpected error occurred. Please try again later.")


st.markdown("# Python Programming")
st.markdown("## Streamlit Application")
st.markdown("### Student Information System")
st.markdown("#### Please fill in the required details below:")
st.markdown("""
### Topics Covered:
- Streamlit Basics
- User Input Handling
- Displaying Messages and Alerts
- Markdown Formatting

[VISIT STREAMLIT](https://streamlit.io/)
""")

st.help(st.exception)

feedback = st.text_area("Feedback", "Enter your feedback here...")
if feedback:
    st.write("Thank you for your feedback!")

age = st.slider("Select your age", 18, 100, 25)

date_of_birth = st.date_input("Select your date of birth")
if date_of_birth>datetime.date.today():
    st.error("Date of birth cannot be in the future.")

#Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Gold", " \u20b9 85", "5%")
col2.metric("Silver", " \u20b9 90", "10%")
col3.metric("Bronze", " \u20b9 80", "-5%")

import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [20, 22, 21, 23],
    "Department": ["Computer Science", "Mathematics", "Physics", "Chemistry"]
}
df = pd.DataFrame(data)
st.dataframe(df)

st.line_chart(df[["Age"]])
st.bar_chart(df[["Age"]])


st.map({
    "lat": [12.9337, 12.8631, 12.8931, 13.0289],
    "lon": [77.6051, 77.5994, 77.4394, 77.5147]
})

st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

st.text_input("Enter your name")
st.text_area("Enter your address")
st.selectbox("Select your gender", ["Male", "Female", "Other"])
st.multiselect("Select your hobbies", ["Reading", "Traveling", "Sports", "Music"])

