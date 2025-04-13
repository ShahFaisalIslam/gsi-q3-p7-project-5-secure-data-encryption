import streamlit as st
from hashlib import pbkdf2_hmac
from cryptography.fernet import Fernet

st.subheader("Retrieve Data")
st.write("Did you store your data with us? Fetch it by confirming your\
 passkey!")

passkey = st.text_input("Passkey:")

if st.button("Fetch Data"):
    if passkey:
        if st.session_state["stored_data"]["passkey"] == pbkdf2_hmac("sha256",bytes(passkey,"ascii"),st.session_state["stored_data"]["key"],10000):
            decryptor = Fernet(st.session_state["stored_data"]["key"])
            st.text_input(label="Data:",disabled=True,
                        value=str(decryptor.decrypt(st.session_state["stored_data"]["data"]),encoding="ascii"))
        else:
            "Invalid passkey, try again"
    else:
        "Please enter passkey before fetching data!"
# if st.button("Test Login"):
#     st.switch_page("Login.py")