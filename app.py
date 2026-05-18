import streamlit as st
from document_loader import DocumentLoader
from text_splitter import TextSplitter
from vector_store import VectorStore
from retriever import Retriever
from rag_pipeline import RAGPipeline

st.title("PDF RAG Assistant")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file is not None:

    # Save uploaded file
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    # Load document
    loader = DocumentLoader()
    documents = loader.load_pdf("temp.pdf")

    # Split document
    splitter = TextSplitter()
    chunks = splitter.split_documents(documents)

    # Create vector store
    vector_store = VectorStore()
    vector_store.add_documents(chunks)

    # Create retriever
    retriever = Retriever(vector_store.collection)

    # Create rag pipeline
    rag_pipeline = RAGPipeline(retriever)

    st.success("PDF processed successfully!")

    question = st.text_input("Ask a question about the document")

    if st.button("Ask"):
        answer = rag_pipeline.ask(question)
        st.write(answer)