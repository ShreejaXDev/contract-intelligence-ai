from src.ingestion.pdf_parser import extract_text_from_pdf
from src.ingestion.text_cleaner import normalize_text

from src.classification.clause_classifier import classify_clause
from src.classification.risk_scorer import calculate_risk_score

pdf_path = "data/raw/contracts/sample_contract.pdf"

raw_text = extract_text_from_pdf(pdf_path)

clean_text = normalize_text(raw_text)

clauses = classify_clause(clean_text)

risk = calculate_risk_score(clauses)

print("\nDetected Clauses:")
for clause in clauses:
    print("-", clause)

print("\nRisk Analysis:")
print(risk)