from src.embeddings.embedding_generator import generate_embedding

from src.embeddings.vector_store import (
    add_document,
    search_documents
)

documents = [
    "The employee shall undergo a probationary period of six months.",

    "Either party may terminate this agreement by giving 30 days notice.",

    "Salary shall be paid on the last day of every month."
]

for i, doc in enumerate(documents):

    embedding = generate_embedding(doc)

    add_document(
        doc_id=str(i),
        text=doc,
        embedding=embedding
    )

query = "What is the notice period?"

query_embedding = generate_embedding(query)

results = search_documents(query_embedding)

print(results["documents"])