import streamlit as st

# -----------------------------------
# Page Configuration
# -----------------------------------
st.set_page_config(
    page_title="AI Contract Intelligence",
    layout="wide"
)

# -----------------------------------
# Main Title
# -----------------------------------
st.title("📄 AI-Powered Contract Intelligence & Risk Scoring")

# -----------------------------------
# Sidebar
# -----------------------------------
st.sidebar.title("Navigation")
st.sidebar.info("Upload a contract PDF to begin analysis.")

uploaded_file = st.sidebar.file_uploader(
    "Choose a Contract PDF",
    type=["pdf"]
)

# -----------------------------------
# Main Content
# -----------------------------------
st.divider()

st.header("📊 Contract Analysis Results")

if uploaded_file is None:
    st.warning("Please upload a contract PDF from the sidebar to begin analysis.")

# -----------------------------------
# Empty Result Sections
# -----------------------------------

col1, col2 = st.columns(2)

with col1:
    st.subheader("📄 Contract Summary")
    st.info("Summary will appear here after analysis.")

with col2:
    st.subheader("⚠️ Risk Score")
    st.info("Risk score will appear here after analysis.")

st.markdown("---")

st.subheader("📋 Key Clauses")
st.info("Detected clauses will appear here.")

st.markdown("---")

st.subheader("🚨 Potential Risks")
st.info("Potential risks identified in the contract will appear here.")

st.markdown("---")

st.subheader("💡 AI Recommendations")
st.info("Suggestions and recommendations will appear here.")

st.markdown("---")

st.subheader("📑 Clause Classification")
st.info("Clause categories will appear here.")

st.markdown("---")

st.subheader("📝 Named Entities")
st.info("Important entities (People, Organizations, Dates, etc.) will appear here.")