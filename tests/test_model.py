import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from agent import create_agent_executor


def test_model_initialization():
    # Create an instance of the agent
    agent_executor = create_agent_executor()

    # Invoke the agent with a sample input
    response = agent_executor.invoke({"input": "Hi, I'm testing you"})

    # Check if the response is not None
    assert response is not None, "Agent returned a null response."

    # Check if the response contains the key 'output'
    assert (
        "output" in response
    ), "The agent's response does not contain the key 'output'."

    # Check if the 'output' key has a non-empty value
    assert response["output"], "The 'output' key contains an empty value."

    print("Test passed successfully. Agent's response:", response["output"])
