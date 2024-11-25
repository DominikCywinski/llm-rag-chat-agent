from dotenv import load_dotenv
from agent_tools import create_agent_tools
from langchain import hub
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory
from langchain.agents import AgentExecutor, create_react_agent


load_dotenv()


def create_agent_executor():
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

    tools = create_agent_tools()

    prompt = hub.pull("hwchase17/react-chat")

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        memory=memory,
        verbose=False,
        handle_parsing_errors=True,
    )

    return agent_executor


def chat(agent_executor):
    while True:
        input_text = input("Search the topic u want:\n")
        response = agent_executor.invoke({"input": input_text})
        print(response["output"])
