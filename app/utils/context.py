def format_docs(docs):
    """
    formats the documents into a single string.
    """
    return "\n\n".join(doc.page_content for doc in docs)
