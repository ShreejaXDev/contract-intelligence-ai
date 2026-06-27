"""
Risk Analyzer

Assigns a risk level based on the predicted clause category.
"""

# -------------------------------------------------------
# Risk Rules
# -------------------------------------------------------

RISK_RULES = {

    "Termination": {
        "risk": "High",
        "reason": "Termination clauses may significantly affect contract continuity and should be reviewed carefully."
    },

    "Liability": {
        "risk": "High",
        "reason": "Liability clauses may expose the organization to legal or financial risks."
    },

    "Confidentiality": {
        "risk": "High",
        "reason": "Confidentiality obligations must be reviewed to protect sensitive information."
    },

    "Intellectual_Property": {
        "risk": "High",
        "reason": "Ownership of intellectual property should always be verified."
    },

    "Payment": {
        "risk": "Medium",
        "reason": "Payment schedules, penalties, and obligations should be reviewed."
    },

    "Property": {
        "risk": "Medium",
        "reason": "Property-related clauses should be checked for ownership and responsibilities."
    },

    "Performance": {
        "risk": "Medium",
        "reason": "Performance obligations should be verified for compliance."
    },

    "Employment": {
        "risk": "Medium",
        "reason": "Employment terms should comply with applicable labor regulations."
    },

    "Legal": {
        "risk": "Low",
        "reason": "General legal provisions usually require standard legal review."
    },

    "General": {
        "risk": "Low",
        "reason": "General administrative clauses usually present lower legal risk."
    }

}


# -------------------------------------------------------
# Risk Prediction Function
# -------------------------------------------------------

def analyze_risk(category):

    if category in RISK_RULES:
        return RISK_RULES[category]

    return {
        "risk": "Unknown",
        "reason": "No predefined risk rule available."
    }


# -------------------------------------------------------
# Test
# -------------------------------------------------------

if __name__ == "__main__":

    categories = [
        "Termination",
        "Payment",
        "Confidentiality",
        "General"
    ]

    for category in categories:

        result = analyze_risk(category)

        print("=" * 60)
        print("Category :", category)
        print("Risk     :", result["risk"])
        print("Reason   :", result["reason"])