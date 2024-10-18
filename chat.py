from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from wikipedia import summary
from langchain.memory import ConversationBufferMemory

from utils import create_agent_executor, chat_initial_message


def search_wikipedia(query):
    try:
        return summary(query, sentences=2)
    except:
        return "I couldn't find any information. Please, try again..."


def chat(initial_message=chat_initial_message):
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    memory.chat_memory.add_message(SystemMessage(content=initial_message))
    agent_executor = create_agent_executor(memory)

    print("\033[33m" + "Start chatting..." + "\033[0m")

    while True:
        query = input("You: ")

        if query.lower() == "exit":
            break

        memory.chat_memory.add_message(HumanMessage(content=query))

        response = agent_executor.invoke({"input": query})
        print("\033[33m" + f"Bot: {response['output']}" + "\033[0m")
        memory.chat_memory.add_message(AIMessage(content=response["output"]))


if __name__ == "__main__":
    chat()
