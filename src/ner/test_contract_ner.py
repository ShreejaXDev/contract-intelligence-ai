from src.ingestion.pdf_parser import extract_text_from_pdf
from src.ingestion.text_cleaner import normalize_text
from src.ner.entity_extractor import extract_entities

pdf_path = "data/raw/contracts/sample_contract.pdf"

raw_text = extract_text_from_pdf(pdf_path)

clean_text = normalize_text(raw_text)

entities = extract_entities(clean_text)

print("=" * 50)
print("TOTAL ENTITIES FOUND:", len(entities))

print("=" * 50)
print("FIRST 20 ENTITIES")

for entity in entities[:20]:
    print(entity)