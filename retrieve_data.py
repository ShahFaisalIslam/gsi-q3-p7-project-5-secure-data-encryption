import streamlit as st
from security import gen_secure_hash,decrypt
st.subheader("Retrieve Data")
st.write("Did you store your data with us? Fetch it by confirming your\
 passkey!")

if "failed_attempts" not in st.session_state:
    st.session_state["failed_attempts"] = 0

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
                if st.session_state["failed_attempts"] > 3:
                    st.session_state["failed_attempts"] = 0
                    st.session_state["logged_in"] = False
                    st.session_state.pop("stored_data")
                    st.rerun()
                else:
                    "Invalid passkey, try again"
                    f"Failed attempts: {st.session_state["failed_attempts"]}"
        else:
            "Please enter passkey before fetching data!"
    # if st.button("Test Login"):
    #     st.switch_page("Login.py")
else:
    "No data stored with us yet!"