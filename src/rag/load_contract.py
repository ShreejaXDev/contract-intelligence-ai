from src.ingestion.pdf_parser import extract_text_from_pdf
from src.ingestion.text_cleaner import normalize_text

from src.embeddings.embedding_generator import generate_embedding
from src.embeddings.vector_store import add_document

pdf_path = "data/raw/contracts/sample_contract.pdf"

raw_text = extract_text_from_pdf(pdf_path)

clean_text = normalize_text(raw_text)

chunks = clean_text.split(".")


for idx, chunk in enumerate(chunks):

    chunk = chunk.strip()

    if len(chunk) < 20:
        continue

    embedding = generate_embedding(chunk)

    add_document(
        doc_id=f"contract_{idx}",
        text=chunk,
        embedding=embedding
    )

print("Contract loaded into ChromaDB successfully.")