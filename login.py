import streamlit as st

if st.session_state["logged_in"]:
    st.switch_page("home.py")

st.subheader("Login")
st.write("Please login to continue")

if st.button("Log In"):
    st.session_state["logged_in"] = True
    st.rerun()
    print(f"Button logged in: {st.session_state["logged_in"]}")

st.session_state["render_back_to_home"] = False