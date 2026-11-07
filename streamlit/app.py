import streamlit as st
st.title("My First Streamlit Application")
st.write("Welcome to Streamlit!")
name = st.text_input("Enter your name")
if name:
    st.success(f"Hello, {name}!")