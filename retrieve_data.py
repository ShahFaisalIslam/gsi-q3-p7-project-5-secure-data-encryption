import streamlit as st
from security import gen_secure_hash,decrypt
st.subheader("Retrieve Data")
st.write("Did you store your data with us? Fetch it by confirming your\
 passkey!")

if "key" in st.session_state["stored_data"]:

    passkey = st.text_input("Passkey:")

    if st.button("Fetch Data"):
        if passkey:
            if st.session_state["stored_data"]["passkey"] == gen_secure_hash(passkey,st.session_state["stored_data"]["key"]):
                st.text_input(label="Data:",disabled=True,
                            value=decrypt(st.session_state["stored_data"]["data"],
                                        st.session_state["stored_data"]["key"]))
            else:
                "Invalid passkey, try again"
        else:
            "Please enter passkey before fetching data!"
    # if st.button("Test Login"):
    #     st.switch_page("Login.py")
else:
    "No data stored with us yet!"