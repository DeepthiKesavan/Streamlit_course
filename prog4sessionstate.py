import streamlit as st
st.title("session state")
if 'name' not in st.session_state:
    st.session_state.name = ""
name = st.text_input("Enter Name")
if st.button("Submit"):
    st.session_state.name = name
if st.session_state.name:
    st.success(f"Hello, {st.session_state.name}!")
    st.write("Nice to see you")
    