from src.classification.clause_classifier import classify_clause

sample_text = """
The employee shall receive salary every month.
Either party may terminate this agreement with 30 days written notice.
The employee shall undergo a probationary period of six months.
"""

clauses = classify_clause(sample_text)

print("Detected Clauses:")

for clause in clauses:
    print("-", clause)