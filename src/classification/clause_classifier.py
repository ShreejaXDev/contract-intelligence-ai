def classify_clause(text):

    text = text.lower()

    clause_types = {
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
        ]
    }

    detected_clauses = []

    for clause, keywords in clause_types.items():

        for keyword in keywords:

            if keyword in text:

                detected_clauses.append(clause)
                break

    return detected_clauses