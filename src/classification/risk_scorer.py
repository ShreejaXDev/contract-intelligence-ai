def calculate_risk_score(clauses):

    risk_weights = {
        "Termination": 3,
        "Confidentiality": 1,
        "Payment": 1,
        "Probation": 1,
        "Leave Policy": 1,
        "Liability": 4,
        "Jurisdiction": 2
    }

    score = 0

    for clause in clauses:
        score += risk_weights.get(clause, 0)

    if score <= 3:
        risk_level = "Low"

    elif score <= 7:
        risk_level = "Medium"

    else:
        risk_level = "High"

    return {
        "score": score,
        "risk_level": risk_level
    }