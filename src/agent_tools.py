from langchain_core.tools import create_retriever_tool
from langchain_community.tools import WikipediaQueryRun, ArxivQueryRun
from langchain_community.utilities import WikipediaAPIWrapper, ArxivAPIWrapper
from load_data import load_web_data
from vector_store import create_vector_store


def create_web_retriever_tool(
    url: str = "https://docs.smith.langchain.com/", name: str = "LangSmith"
):
    loaded_data = load_web_data(url)
    vector_store = create_vector_store(loaded_data)
    retriever = vector_store.as_retriever()

    web_tool = create_retriever_tool(
        retriever,
        name=name + "_search",
        description=f"Search for information about {name}. For any questions about {name}, you must use this tool!",
    )

    return web_tool


def create_arxiv_retriever_tool(k_results: int = 3):
    arxiv_wrapper = ArxivAPIWrapper(top_k_results=k_results, doc_content_chars_max=200)
    arxiv_tool = ArxivQueryRun(api_wrapper=arxiv_wrapper)

    return arxiv_tool


def create_wikipedia_retriever_tool(k_results: int = 3):
    wiki_wrapper = WikipediaAPIWrapper(
        top_k_results=k_results, doc_content_chars_max=200
    )
    wiki_tool = WikipediaQueryRun(api_wrapper=wiki_wrapper)

    return wiki_tool


def create_agent_tools():
    arxiv_tool = create_arxiv_retriever_tool()
    wiki_tool = create_wikipedia_retriever_tool()
    web_tool = create_web_retriever_tool()

    return [arxiv_tool, wiki_tool, web_tool]
