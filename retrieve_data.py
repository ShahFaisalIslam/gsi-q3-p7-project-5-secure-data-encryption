import streamlit as st
from security import gen_secure_hash,decrypt
from time import time
LOCKOUT_TIME = 60
st.subheader("Retrieve Data")
st.write("Did you store your data with us? Fetch it by confirming your\
 passkey!")

if "failed_attempts" not in st.session_state:
    st.session_state["failed_attempts"] = 0

if "lockout_time" in st.session_state:
    if time() - st.session_state["lockout_time"] >= LOCKOUT_TIME:
        st.session_state.pop("lockout_time")
if "lockout_time" in st.session_state:        
    f"You are locked out. Come back after {round(LOCKOUT_TIME - (time() - st.session_state["lockout_time"]))} seconds!"
else:
    if "key" in st.session_state["stored_data"]:

        passkey = st.text_input("Passkey:")

        if st.button("Fetch Data"):
            if passkey:
                if st.session_state["stored_data"]["passkey"] == gen_secure_hash(passkey,st.session_state["stored_data"]["key"]):
                    if st.session_state["failed_attempts"]:
                        st.session_state["failed_attempts"] = 0
                    st.text_input(label="Data:",disabled=True,
                                value=decrypt(st.session_state["stored_data"]["data"],
                                            st.session_state["stored_data"]["key"]))
                else:
                    st.session_state["failed_attempts"] += 1
                    if st.session_state["failed_attempts"] >= 3:
                        st.session_state["failed_attempts"] = 0
                        st.session_state["lockout_time"] = time()
                    else:
                        "Invalid passkey, try again"
                        f"Failed attempts: {st.session_state["failed_attempts"]}"
            else:
                "Please enter passkey before fetching data!"
        # if st.button("Test Login"):
        #     st.switch_page("Login.py")
    else:
        "No data stored with us yet!"