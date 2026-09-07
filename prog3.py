import streamlit as st

st.title("Student Result")

col1, col2 = st.columns(2)

with col1:
    st.header("Input")

    with st.form("student_form"):
        name = st.text_input("Enter Name")
        marks = st.number_input("Enter Marks", 0, 100)
        submit = st.form_submit_button("Submit")

with col2:
    st.header("Output")

    if submit:
        st.write("Name:", name)
        st.write("Marks:", marks)

        if marks >= 50:
            st.success("PASS")
        else:
            st.error("FAIL")