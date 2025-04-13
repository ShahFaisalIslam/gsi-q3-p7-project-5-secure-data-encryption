import streamlit as st

[col1,col2] = st.columns(2)

with col1:
    if st.button(label="Insert Data"):
        st.switch_page("insert_data.py")

with col2:
    if st.button(label="Retrieve Data"):
        st.switch_page("retrieve_data.py")

st.session_state["render_back_to_home"] = False