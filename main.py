import streamlit as st

# To avoid navigation bar, we use 'back to home' for guiding users back
# to home page
if "render_back_to_home" not in st.session_state:
    st.session_state["render_back_to_home"] = True

# Authentication Implementation
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

def main():
    st.set_page_config(page_title="Secure Data Encryption",page_icon="🔒",
                       layout="wide")
    st.title("🔒 Secure Data Encryption")
    st.write("Secure your data here!")

    # Required for the pages to be routable
    if st.session_state["logged_in"]:
        pg = st.navigation([st.Page("home.py"),
                        st.Page("insert_data.py"),
                        st.Page("retrieve_data.py"),
                        st.Page("login.py")],position="hidden")
    else:
        pg = st.navigation([st.Page("login.py")],position="hidden")

    pg.run()

    if st.session_state["render_back_to_home"]:
        if st.button("Back to Home"):
            st.switch_page("home.py")
    # So that pages other than the ones that disabled 'back to home' render the
    # button next time
    else:
        st.session_state["render_back_to_home"] = True

if __name__ == "__main__":
    main()
