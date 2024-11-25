from langchain_community.document_loaders import WebBaseLoader


def load_web_data(url="https://docs.smith.langchain.com/"):
    loader = WebBaseLoader(url)
    loaded_docs = loader.load()

    return loaded_docs
