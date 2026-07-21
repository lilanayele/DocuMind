def search_document(database, question):

    results = database.similarity_search(
        question,
        k=3
    )

    return "\n\n".join(
        [doc.page_content for doc in results]
    )
