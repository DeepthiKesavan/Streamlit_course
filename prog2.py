import streamlit as st
st.title("Student Results")
name = st.text_input("Enter your name")
marks = st.number_input("Enter your marks", 0, 100)
choice=st.selectbox("Select your choice", ["Pass/Fail", "Grade"])
if st.button("Check Result"):
    if choice == "Pass/Fail":
        if marks >= 50:
            st.success(f"Hello {name}, you have passed with marks: {marks}.")
        else:
            st.error(f"Hello {name}, you have failed with marks: {marks}.")
    elif choice == "Grade":
        if marks >= 90:
            st.success(f"Hello {name}, you have an A grade with marks: {marks}.")
        elif marks >= 80:
            st.success(f"Hello {name}, you have a B grade with marks: {marks}.")
        elif marks >= 70:
            st.success(f"Hello {name}, you have a C grade with marks: {marks}.")
        elif marks >= 50:
            st.success(f"Hello {name}, you have a D grade with marks: {marks}.")
        else:
            st.error(f"Hello {name}, you have failed with marks: {marks}.")