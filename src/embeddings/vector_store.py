import chromadb

client = chromadb.PersistentClient(path="./data/embeddings")

collection = client.get_or_create_collection(
    name="contracts"
)


def add_document(doc_id, text, embedding):

    collection.add(
        ids=[doc_id],
        documents=[text],
        embeddings=[embedding.tolist()]
    )



def search_documents(query_embedding, n_results=1):

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=n_results
    )

    return results