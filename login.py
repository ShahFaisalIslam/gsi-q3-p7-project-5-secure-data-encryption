import streamlit as st

if st.session_state["logged_in"]:
    st.switch_page("home.py")

st.subheader("Login")
st.write("Please login to continue")

user = st.text_input(label="Username:")

if st.button("Log In"):
    if user:
        st.session_state["logged_in"] = True
        st.session_state["user"] = user
        st.rerun()
    else:
        "Please type username before logging in"

st.session_state["render_back_to_home"] = False