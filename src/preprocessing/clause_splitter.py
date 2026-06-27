import re


def split_into_clauses(text):
    """
    Split contract into clauses using numbered headings.
    """

    # Remove extra spaces
    text = re.sub(r"\r", "", text)
    text = re.sub(r"\n{2,}", "\n", text)

    # Pattern for headings like:
    # 1. Commencement
    # 5. Wage
    # 10. Annual Leave
    pattern = r"(?=^\d+\.\s+[A-Z])"

    clauses = re.split(pattern, text, flags=re.MULTILINE)

    cleaned_clauses = []

    for clause in clauses:

        clause = clause.strip()

        if len(clause) > 30:
            cleaned_clauses.append(clause)

    return cleaned_clauses


if __name__ == "__main__":

    sample = """
1. Commencement
This contract begins today.

2. Payment
Payment shall be made monthly.

3. Termination
Either party may terminate this agreement.
"""

    clauses = split_into_clauses(sample)

    for i, clause in enumerate(clauses):
        print("=" * 60)
        print(f"Clause {i+1}")
        print(clause)