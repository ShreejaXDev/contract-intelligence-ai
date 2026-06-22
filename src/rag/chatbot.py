from src.rag.retriever import retrieve_relevant_context


def ask_contract(query):

    context = retrieve_relevant_context(query)

    response = f"""
Relevant Contract Information:

{context}
"""

    return response


if __name__ == "__main__":

    while True:

        query = input("\nAsk a question about the contract: ")

        if query.lower() == "exit":
            break

        answer = ask_contract(query)

        print(answer)