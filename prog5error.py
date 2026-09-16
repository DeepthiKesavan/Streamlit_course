import streamlit as st
st.title("Student Result")
name = st.text_input("Enter Name")
marks = st.number_input("Enter Marks", min_value=-1, max_value=100)
if st.button("Check Result"):
    if name == "":
        st.error("Please enter your name.")
    elif marks < 0 or marks > 100:
        st.error("Please enter marks between 0 and 100.")
    elif marks >= 40:
        st.success(name + " - PASS")
    else:
        st.error(name + " - FAIL")