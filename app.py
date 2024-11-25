import streamlit as st
import sys
from pathlib import Path

src_path = Path(__file__).parent / "src"
sys.path.append(str(src_path))
from agent import create_agent_executor, chat
from web_layout import create_layout, show_results


@st.cache_resource
def load_agent_executor():
    agent_executor = create_agent_executor()
    print("Agent Loaded")

    return agent_executor


user_input, submit_clicked = create_layout()

agent_executor = load_agent_executor()

if submit_clicked:
    if user_input != "":
        try:
            response = agent_executor.invoke({"input": user_input})
            show_results(user_input, response["output"])

        except Exception as e:
            st.header("Sorry, something went wrong :(. Please try again.")
            print(e)
    else:
        st.header("Please enter a question.")
