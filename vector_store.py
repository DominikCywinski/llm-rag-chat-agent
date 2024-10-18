import os
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

current_dir = os.path.dirname(os.path.abspath(__file__))
input_docs_dir = os.path.join(current_dir, "input_docs")

if not os.path.exists(input_docs_dir):
    raise FileNotFoundError(f"The directory {input_docs_dir} does not exist.")

doc_files = [doc for doc in os.listdir(input_docs_dir) if doc.endswith(".txt")]

docs_with_meta = []

for doc_file in doc_files:
    doc_path = os.path.join(input_docs_dir, doc_file)
    loader = TextLoader(doc_path)
    loaded_doc = loader.load()

    for doc in loaded_doc:
        doc.metadata = {"source": doc_file}
        docs_with_meta.append(doc)

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
split_docs = text_splitter.split_documents(docs_with_meta)

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

persist_directory = os.path.join(current_dir, "chroma_db")

Chroma.from_documents(split_docs, embeddings, persist_directory=persist_directory)
