import streamlit as st

from cryptography.fernet import Fernet
from hashlib import pbkdf2_hmac

st.subheader("Insert Data")
st.write("Store your data securely here!")

# # Field for user to type their name
# user : str = st.text_input("User Name:")
# Field for the data (for now, let it be some string)
data : str = st.text_input("Data:")
# Unique passkey for the data
passkey : str = st.text_input("Passkey:")

if st.button("Save"):
    if data and passkey:
        crypt_key = Fernet.generate_key()
        encryptor = Fernet(crypt_key)
        st.session_state["stored_data"] = {
            "data": encryptor.encrypt(bytes(data,"ascii")),
            "key": crypt_key,
            "passkey": pbkdf2_hmac("sha256",bytes(passkey,"ascii"),crypt_key,10000)
        }
        "Data saved!"
        print(st.session_state["stored_data"])
    else:
        "Complete 'Data' and 'Passkey' fields before saving!"