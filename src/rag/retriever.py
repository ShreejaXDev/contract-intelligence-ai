from src.embeddings.embedding_generator import generate_embedding
from src.embeddings.vector_store import search_documents


def retrieve_relevant_context(query):

    query_embedding = generate_embedding(query)

    results = search_documents(
        query_embedding=query_embedding,
        n_results=1
    )

    return results["documents"][0][0]