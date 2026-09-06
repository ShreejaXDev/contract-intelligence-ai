import streamlit as st
import time
import re
import pdfplumber

st.set_page_config(
    page_title="AI Contract Intelligence",
    page_icon="📄",
    layout="wide"
)

st.markdown("""
<style>
.block-container{
    padding-top:1.5rem;
}

.card{
    background:#1f2937;
    padding:18px;
    border-radius:12px;
    border:1px solid #374151;
    margin-bottom:15px;
}

.small{
    color:#9ca3af;
    font-size:14px;
    white-space: pre-wrap;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# Clause classification logic (kept identical to src/classification/clause_classifier.py)
# -------------------------

CLAUSE_TYPES = {
    "Termination": [
        "terminate",
        "termination",
        "end this agreement",
        "written notice"
    ],
    "Confidentiality": [
        "confidential",
        "non-disclosure",
        "proprietary information"
    ],
    "Payment": [
        "salary",
        "payment",
        "compensation",
        "wages"
    ],
    "Probation": [
        "probation",
        "probationary period"
    ],
    "Leave Policy": [
        "leave",
        "vacation",
        "sick leave"
    ],
    "Intellectual Property": [
        "intellectual property",
        "copyright",
        "invention"
    ],
    "Non-Compete": [
        "non-compete",
        "noncompete",
        "compete with"
    ]
}

RISK_RULES = [
    ("governing law", "Missing governing law clause"),
    ("arbitration", "No arbitration clause"),
    ("notice period", "Notice period may need clarification"),
    ("indemnif", "No indemnification clause found"),
    ("dispute resolution", "No dispute resolution clause found"),
]


def extract_text_from_pdf(uploaded_file) -> str:
    text_parts = []
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text() or ""
            text_parts.append(page_text)
    return "\n".join(text_parts)


def classify_clauses(text: str):
    lower_text = text.lower()
    detected = []
    for clause, keywords in CLAUSE_TYPES.items():
        for keyword in keywords:
            if keyword in lower_text:
                detected.append(clause)
                break
    return detected


def find_risks(text: str):
    lower_text = text.lower()
    risks = []
    for keyword, message in RISK_RULES:
        if keyword not in lower_text:
            risks.append(message)
    return risks


def compute_risk_score(num_clauses: int, num_risks: int) -> int:
    # Simple heuristic: more missing-clause risks -> higher score, capped 0-100
    base = num_risks * 15
    score = min(100, base)
    return score


def extract_simple_entities(text: str):
    dates = re.findall(
        r"\b\d{1,2}(?:st|nd|rd|th)?\s+\w+\s+\d{4}\b|\b\d{2}/\d{2}/\d{4}\b",
        text
    )
    orgs = re.findall(
        r"\b([A-Z][a-zA-Z]+(?:\s[A-Z][a-zA-Z]+)*\s(?:Ltd|LLC|Inc|Technologies|Corporation|Company|Pvt))\b",
        text
    )
    return {
        "dates": list(dict.fromkeys(dates))[:5],
        "organizations": list(dict.fromkeys(orgs))[:5],
    }


# -------------------------
# Sidebar
# -------------------------

st.title("📄 AI-Powered Contract Intelligence & Risk Scoring")

with st.sidebar:

    st.header("⚙ Navigation")

    st.write("Upload a PDF contract to begin.")

    uploaded_file = st.file_uploader(
        "📂 Upload Contract PDF",
        type=["pdf"]
    )

    analyze = False

    st.divider()

    if uploaded_file:

        st.success("File uploaded successfully")

        st.write(f"**Name:** {uploaded_file.name}")
        st.write(f"**Size:** {uploaded_file.size/(1024*1024):.2f} MB")

        analyze = st.button(
            "🚀 Analyze Contract",
            use_container_width=True
        )

# -------------------------
# Default Values
# -------------------------

documents = 0
risk = "--"
clauses = "--"
status = "Waiting"

summary = "Summary will appear here after analysis."
risk_text = "Risk score will appear here after analysis."
key_clause_text = "Detected clauses will appear here."
risk_details = "Potential risks identified in the contract will appear here."
recommendation = "Recommendations will appear here."
entities = "Organizations, people, dates and locations extracted from the contract will appear here."

# -------------------------
# Real Analysis (no backend, runs in-process)
# -------------------------

if analyze and uploaded_file is not None:

    with st.spinner("Analyzing Contract..."):

        try:
            contract_text = extract_text_from_pdf(uploaded_file)

            if not contract_text.strip():
                st.error("Couldn't extract any text from this PDF. It may be a scanned/image PDF.")
            else:
                detected_clauses = classify_clauses(contract_text)
                risks_found = find_risks(contract_text)
                score = compute_risk_score(len(detected_clauses), len(risks_found))
                ents = extract_simple_entities(contract_text)

                documents = 1
                risk = f"{score}%"
                clauses = len(detected_clauses)
                status = "Completed"

                summary = contract_text[:600] + ("..." if len(contract_text) > 600 else "")

                risk_level = "Low Risk" if score < 34 else ("Medium Risk" if score < 67 else "High Risk")
                risk_text = f"{risk_level}\n\nOverall contract risk score: {score}%"

                key_clause_text = "\n".join(f"• {c}" for c in detected_clauses) or "No known clause types detected."

                risk_details = "\n".join(f"• {r}" for r in risks_found) or "No obvious missing clauses detected."

                recommendation = "\n".join(f"✔ Consider adding: {r.replace('No ', '').replace('Missing ', '')}" for r in risks_found) or "No specific recommendations — contract covers standard bases."

                entities = (
                    "Dates:\n" + ("\n".join(ents["dates"]) or "None found") +
                    "\n\nOrganizations:\n" + ("\n".join(ents["organizations"]) or "None found")
                )

                st.success("✅ Analysis Completed Successfully!")

        except Exception as e:
            st.error(f"Something went wrong while analyzing the PDF: {e}")

elif analyze and uploaded_file is None:
    st.warning("Please upload a PDF first.")

# -------------------------
# Dashboard
# -------------------------

st.header("📊 AI Contract Analysis Dashboard")

a, b, c, d = st.columns(4)

a.metric("Documents", documents)
b.metric("Risk Score", risk)
c.metric("Clauses", clauses)
d.metric("Status", status)

# -------------------------
# Results
# -------------------------

left, right = st.columns(2)

with left:
    st.markdown(f"""
<div class="card">
<h3>📄 Contract Summary</h3>
<p class="small">{summary}</p>
</div>
""", unsafe_allow_html=True)

with right:
    st.markdown(f"""
<div class="card">
<h3>⚠️ Risk Score</h3>
<p class="small">{risk_text}</p>
</div>
""", unsafe_allow_html=True)

sections = [
    ("📋 Key Clauses", key_clause_text),
    ("🚨 Potential Risks", risk_details),
    ("💡 AI Recommendations", recommendation),
    ("📝 Named Entities", entities)
]

for title, text in sections:
    st.markdown(f"""
<div class="card">
<h3>{title}</h3>
<p class="small">{text}</p>
</div>
""", unsafe_allow_html=True)

st.caption("🚀 Running fully self-contained — no separate backend required.")
