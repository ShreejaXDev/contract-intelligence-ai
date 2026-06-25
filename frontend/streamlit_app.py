import streamlit as st

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="AI Contract Intelligence",
    layout="wide"
)

# ----------------------------
# Main Title
# ----------------------------
st.title("📄 AI-Powered Contract Intelligence & Risk Scoring")

# ----------------------------
# Sidebar
# ----------------------------
st.sidebar.title("Navigation")
st.sidebar.info("Upload a contract PDF to begin analysis.")

# PDF Upload Button
uploaded_file = st.sidebar.file_uploader(
    "Choose a Contract PDF",
    type=["pdf"]
)