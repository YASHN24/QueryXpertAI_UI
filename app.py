import os
import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import HuggingFaceHub
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.document_loaders import PyMuPDFLoader


# Function to initialize and load document
def initialize_and_load_doc(api_token, pdf_file_path, repo_id):
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = api_token

    loader = PyMuPDFLoader(pdf_file_path)
    documents = loader.load()
    embedding = HuggingFaceEmbeddings()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    text_chunks = text_splitter.split_documents(documents)

    db = Chroma.from_documents(text_chunks, embedding)

    llm = HuggingFaceHub(repo_id=repo_id, model_kwargs={"temperature": 0.7, "max_length": 256})

    chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=db.as_retriever())
    return chain


# Streamlit application
def run_document_qa_system():
    st.title("QueryXpertAI")

    api_token = st.text_input("Enter your Hugging Face API token:", type="password")
    repo_id = "OpenAssistant/oasst-sft-1-pythia-12b"

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file and api_token and repo_id:
        pdf_file_path = f'/tmp/{uploaded_file.name}'
        with open(pdf_file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        chain = initialize_and_load_doc(api_token, pdf_file_path, repo_id)

        query = st.text_input("Type in your question:")
        if query:
            try:
                answer = chain.run(query)
                st.write("Answer:", answer)
            except Exception as e:
                st.write(f'Error answering query: {str(e)}')


if __name__ == "__main__":
    run_document_qa_system()
