 import streamlit as st

from src.document_loader import load_document
from src.embeddings import get_embeddings
from src.vector_store import split_documents, create_database
from src.qa import search_document


st.title("📄 DocuMind")

file = st.file_uploader(
    "Upload PDF",
    type="pdf"
)

if file:

    with open("temp.pdf", "wb") as f:
        f.write(file.read())

    st.success("PDF uploaded successfully!")

    documents = load_document("temp.pdf")

    chunks = split_documents(documents)

    embeddings = get_embeddings()

    database = create_database(
        chunks,
        embeddings
    )

    st.success("Document processed!")

    question = st.text_input(
        "Ask a question about the document"
    )

    if question:
        answer = search_document(
            database,
            question
        )

        st.write(answer)
