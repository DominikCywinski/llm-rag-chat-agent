from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


def split_documents(loaded_docs):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(loaded_docs)

    return chunks


def create_vector_store(loaded_docs):
    split_docs = split_documents(loaded_docs)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-mpnet-base-v2"
    )

    vector_db = FAISS.from_documents(split_docs, embeddings)

    return vector_db
