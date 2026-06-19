from src.embeddings.embedding_generator import generate_embedding

sample_text = """
The employee shall undergo a probationary period of six months.
"""

embedding = generate_embedding(sample_text)

print("Embedding Length:", len(embedding))

print("\nFirst 10 Values:")

print(embedding[:10])