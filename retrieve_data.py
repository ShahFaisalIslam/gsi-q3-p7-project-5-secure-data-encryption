import streamlit as st
from hashlib import pbkdf2_hmac

st.subheader("Retrieve Data")
st.write("Did you store your data with us? Fetch it by confirming your\
 passkey!")

passkey = st.text_input("Passkey:")

if st.button("Fetch Data"):
    if passkey:
        if st.session_state["stored_data"]["passkey"] == pbkdf2_hmac("sha256",bytes(passkey,"ascii"),bytes(st.session_state["stored_data"]["data"],"ascii"),10000):
            st.text_input(label="Data:",disabled=True,
                        value=st.session_state["stored_data"]["data"])
        else:
            "Invalid passkey, try again"
    else:
        "Please enter passkey before fetching data!"
# if st.button("Test Login"):
#     st.switch_page("Login.py")