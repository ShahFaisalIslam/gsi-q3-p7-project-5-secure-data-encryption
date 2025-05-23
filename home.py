import streamlit as st
from data import retrieve_data

st.subheader(f"Welcome Back, {st.session_state["user"]}")

if 'stored_data' not in st.session_state:
    st.session_state["stored_data"] = retrieve_data(st.session_state["user"])

[col1,col2] = st.columns(2)

with col1:
    if st.button(label="Insert Data"):
        st.switch_page("insert_data.py")

with col2:
    if st.button(label="Retrieve Data"):
        st.switch_page("retrieve_data.py")

if st.button("Log Out"):
    st.session_state["user"] = None
    st.session_state["logged_in"] = False
    st.rerun()

st.session_state["render_back_to_home"] = False