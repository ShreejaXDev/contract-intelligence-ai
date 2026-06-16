from src.ingestion.pdf_parser import extract_text_from_pdf
from src.ingestion.text_cleaner import normalize_text

pdf_path = "data/raw/contracts/sample_contract.pdf"

raw_text = extract_text_from_pdf(pdf_path)

clean_text = normalize_text(raw_text)

print("=" * 50)
print("RAW TEXT LENGTH:", len(raw_text))

print("=" * 50)
print("CLEAN TEXT LENGTH:", len(clean_text))

print("=" * 50)
print("FIRST 1000 CHARACTERS")
print(clean_text[:1000])