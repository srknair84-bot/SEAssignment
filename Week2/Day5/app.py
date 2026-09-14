import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings

st.title("PDF RAG Assistant")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"]) 

if uploaded_file is not None:
    st.success(f"Uploaded: {uploaded_file.name}")

    file_path = "uploaded.pdf"

    with open(file_path, "wb") as file:
        file.write(uploaded_file.getbuffer())

    loader = PyPDFLoader(file_path)

    documents = loader.load()

    st.success(f"PDF loaded successfully! Pages: {len(documents)}")

    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = text_splitter.split_documents(documents)

    st.success(f"PDF split successfully! Chunks: {len(chunks)}")

    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

    st.success("Embedding model created successfully!")