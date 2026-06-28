import streamlit as st
import requests

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

st.divider()

st.header("📊 Contract Analysis Results")

# -------------------------------
# API URL
# -------------------------------

API_URL = "http://127.0.0.1:8000/upload"

if uploaded_file is None:
    st.warning("Please upload a contract PDF from the sidebar to begin analysis.")

else:

    if st.button("Analyze Contract"):

        with st.spinner("Analyzing Contract..."):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    "application/pdf"
                )
            }

            response = requests.post(API_URL, files=files)

            if response.status_code == 200:

                data = response.json()

                analysis = data["analysis"]

            else:

                st.error("Backend Error")

                st.stop()

        # -----------------------------------
        # Summary
        # -----------------------------------

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("📄 Contract Summary")

            st.success(
                f"Total Clauses : {analysis['total_clauses']}"
            )

        with col2:

            st.subheader("⚠️ Risk Score")

            risk = analysis["risk_summary"]

            st.metric("High Risk", risk["High"])
            st.metric("Medium Risk", risk["Medium"])
            st.metric("Low Risk", risk["Low"])

        st.markdown("---")

        # -----------------------------------
        # Clause Classification
        # -----------------------------------

        st.subheader("📑 Clause Classification")

        for clause in analysis["predictions"]:

            with st.expander(
                f"Clause {clause['clause_number']} : {clause['category']}"
            ):

                st.write("### Category")
                st.write(clause["category"])

                st.write("### Confidence")
                st.progress(clause["confidence"] / 100)
                st.write(f"{clause['confidence']} %")

                st.write("### Risk")

                st.error(
                    f"{clause['risk_level']} Risk"
                )

                st.write("### Reason")

                st.info(
                    clause["reason"]
                )

                st.write("### Clause Text")

                st.write(
                    clause["text"]
                )

        st.markdown("---")

        # -----------------------------------
        # Potential Risks
        # -----------------------------------

        st.subheader("🚨 Potential Risks")

        high_risk = [
            c for c in analysis["predictions"]
            if c["risk_level"] == "High"
        ]

        if len(high_risk) == 0:

            st.success("No High Risk Clauses Found")

        else:

            for clause in high_risk:

                st.error(

                    f"Clause {clause['clause_number']} "

                    f"({clause['category']})"

                )

        st.markdown("---")

        # -----------------------------------
        # AI Recommendations
        # -----------------------------------

        st.subheader("💡 AI Recommendations")

        for clause in analysis["predictions"]:

            st.write(

                f"• Clause {clause['clause_number']} "

                f"({clause['category']}) : "

                f"{clause['reason']}"

            )

        st.markdown("---")

        # -----------------------------------
        # Named Entities
        # -----------------------------------

        st.subheader("📝 Named Entities")

        for clause in analysis["predictions"]:

            with st.expander(

                f"Clause {clause['clause_number']}"

            ):

                entities = clause["entities"]

                for key, value in entities.items():

                    if len(value) > 0:

                        st.write(f"**{key}**")

                        st.write(value)