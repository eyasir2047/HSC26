import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

# ----------------------------------------
# PAGE CONFIGURATION & CUSTOM AESTHETICS
# ----------------------------------------
st.set_page_config(page_title="Student Dashboard", page_icon="🎓", layout="centered")

st.markdown("""
<style>
    /* Styling to make it look premium and clean */
    .stApp {
        background-color: #0e1117;
        color: #fafafa;
    }
    .stTextInput > div > div > input {
        border-radius: 8px;
        border: 1px solid #ff4b4b;
    }
    .stButton > button {
        border-radius: 8px;
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
        transition: 0.3s;
        border: none;
        width: 100%;
    }
    .stButton > button:hover {
        background-color: #ff6b6b;
        color: white;
        border-color: #ff6b6b;
    }
    h1 {
        text-align: center;
        background: -webkit-linear-gradient(#fca5a5, #ef4444);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family: 'Inter', sans-serif;
    }
    .auth-container {
        max-width: 400px;
        margin: 0 auto;
        padding-top: 100px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# ----------------------------------------
# AUTHENTICATION LOGIC
# ----------------------------------------
def check_password():
    """Returns `True` if the user had the correct password."""
    def password_entered():
        if st.session_state["password"] == "57":
            st.session_state["password_correct"] = True
            # We keep the password state so we don't accidentally log out,
            # but usually you'd securely hash or token manage this.
            del st.session_state["password"]  
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.markdown("<div class='auth-container'><h1>Welcome to Sirius Academy 🎓</h1><p>Please enter password to proceed.</p></div>", unsafe_allow_html=True)
        st.text_input("Password", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.markdown("<div class='auth-container'><h1>Welcome to  Academy</h1><p>Please enter password to proceed.</p></div>", unsafe_allow_html=True)
        st.text_input("Password", type="password", on_change=password_entered, key="password")
        st.error("😕 Password incorrect. Please try again.")
        return False
    else:
        return True

# ----------------------------------------
# MAIN DASHBOARD LOGIC
# ----------------------------------------
if check_password():
    st.title("Welcome to the Sirius Academy 🎓")
    st.markdown("<p style='text-align: center; color: #a1a1aa;'>Please enter your details below. Your information will be securely stored in our records.</p>", unsafe_allow_html=True)
    
    st.divider()
    
    try:
        # Establish connection to Google Sheets
        conn = st.connection("gsheets", type=GSheetsConnection)
    except Exception as e:
        st.error("⚠️ Connection Error: Could not initialize Google Sheets connection. Have you set up the secrets properly? Check instructions.")
        st.stop()
    
    with st.form(key="student_form"):
        name = st.text_input("Full Name", placeholder="e.g. Raihan Ratul")
        college = st.text_input("College", placeholder="e.g. Govt. Tolaram College")
        phone_number = st.text_input("Phone Number", placeholder="e.g. 01796681477")
        
        st.markdown("<br>", unsafe_allow_html=True)
        submit_button = st.form_submit_button(label="Submit Information ✨")
        
        if submit_button:
            if not name or not college or not phone_number:
                st.warning("⚠️ Please fill out all fields before submitting.")
            else:
                with st.spinner("Saving your information securely..."):
                    try:
                        # Read existing data
                        df = conn.read()
                        
                        # Handle Empty DataFrames if sheet is newly created
                        if df.empty or len(df.columns) == 0:
                            df = pd.DataFrame(columns=["Name", "College", "Phone Number"])
                        
                        # Create new row
                        new_data = pd.DataFrame(
                            [
                                {
                                    "Name": name,
                                    "College": college,
                                    "Phone Number": phone_number
                                }
                            ]
                        )
                        
                        # Append and update the Google Sheet
                        updated_df = pd.concat([df, new_data], ignore_index=True)
                        conn.update(data=updated_df)
                        
                        st.success(f"🎉 Success! Thank you {name}, your information has been recorded.")
                    except Exception as e:
                        st.error("❌ Failed to save information to Google Sheets. Check your Sharing Permissions and API Limits.")
                        st.exception(e)
