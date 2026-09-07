import streamlit as st
st.title("Student Mark Status")
name = st.text_input("Enter your name")
marks =st.number_input("Enter your marks", min_value=0, max_value=100)
if name:
    st.write(f"Hello {name}, your marks are {marks}.")
    if marks >= 50:
        st.success("Congratulations! You have passed.")
    else:
        st.error("Sorry, you have failed. Better luck next time.")
    
