import streamlit as st

from security import gen_secure_hash,encrypt
from data import store_data

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
        key,encrypted_data = encrypt(data)
        st.session_state["stored_data"] = {
            "data": encrypted_data,
            "key": key,
            "passkey": gen_secure_hash(passkey,key)
        }
        store_data(st.session_state["user"],st.session_state["stored_data"])
        "Data saved!"
    else:
        "Complete 'Data' and 'Passkey' fields before saving!"