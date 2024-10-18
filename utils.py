import os
from dotenv import load_dotenv
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import Tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.embeddings import HuggingFaceEmbeddings
from wikipedia import summary

chat_initial_message = (
    "You are an AI assistant that can provide helpful answers using you knowledge and available tools.\n"
    "When you know the answer, just answer. If you really are unable to answer, you can use the following "
    "tools: Documents (For context) and Wikipedia(for topic)."
)


def search_wikipedia(query):
    try:
        return summary(query, sentences=2)
    except:
        return "I couldn't find any information. Please, try again..."


def create_agent_executor(memory):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_persist_dir = os.path.join(current_dir, "chroma_db")

    if not os.path.exists(db_persist_dir):
        raise FileNotFoundError("The file doesnt exist")

    load_dotenv()

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-mpnet-base-v2"
    )

    db = Chroma(persist_directory=db_persist_dir, embedding_function=embeddings)

    retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 2})

    model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

    context_q_system_prompt = (
        "Given a chat history and the latest user question "
        "which might reference context in the chat history, "
        "formulate a standalone question which can be understood "
        "without the chat history. Do NOT answer the question, just "
        "reformulate it if needed and otherwise return it as is."
    )

    context_q_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", context_q_system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )

    history_aware_retriever = create_history_aware_retriever(
        model, retriever, context_q_prompt
    )

    qa_system_prompt = (
        "You are an assistant for question-answering tasks. Use "
        "the following pieces of retrieved context to answer the "
        "question. If you don't know the answer, just say that you "
        "don't know. Use three sentences maximum and keep the answer "
        "concise."
        "\n\n"
        "{context}"
    )

    qa_prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", qa_system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )

    qa_chain = create_stuff_documents_chain(model, qa_prompt_template)
    rag_chain = create_retrieval_chain(history_aware_retriever, qa_chain)

    react_chat_prompt = hub.pull("hwchase17/react-chat")

    tools = [
        Tool(
            name="Documents",
            func=lambda input, **kwargs: rag_chain.invoke(
                {"input": input, "chat_history": kwargs.get("chat_history", [])}
            ),
            description="Useful for when you need to answer questions about the context",
        ),
        Tool(
            name="Wikipedia",
            func=search_wikipedia,
            description="Useful for when you dont know information about a topic.",
        ),
    ]

    agent = create_react_agent(llm=model, tools=tools, prompt=react_chat_prompt)
    agent_executor = AgentExecutor.from_agent_and_tools(
        agent=agent,
        tools=tools,
        memory=memory,
        handle_parsing_errors=True,
        verbose=False,
    )

    return agent_executor
