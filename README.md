# LLM-RAG-Chat-Agent

This repository combines powerful AI techniques to build an interactive and intelligent chatbot. It integrates a **Large Language Model (LLM)** with **Retrieval-Augmented Generation (RAG)** and an **Agent** framework for enhanced information retrieval, reasoning, and real-time conversation capabilities.

## Features

- **LLM-Powered Chatbot:** Provides dynamic responses using a LLM
- **Retrieval-Augmented Generation (RAG):** Incorporates a retrieval mechanism to enhance responses with relevant context from external sources.
- **Agent Framework:** Enables the chatbot to make decisions and act autonomously to accomplish tasks, such as answering questions, fetching information, or solving problems.
- **Customizable Pipelines:** Easy integration and adaptation for various use cases, from question-answering systems to specialized knowledge assistants.

## Use Cases

- Question answering based on external knowledge.
- Conversational AI with dynamic, context-aware responses.
- Enhanced knowledge retrieval using the RAG framework.

## Getting Started

### Prerequisites

- Python 3.10 or 3.11.
- Poetry (https://python-poetry.org/docs/#installation).

### Installation

1. Clone the repository.

2. Install dependencies using Poetry:
   ```bash
   poetry install --no-root
   ```
   
3. Set up your environment variables (.env file).

4. Activate the Poetry shell:
   ```bash
   poetry shell
   ```

## Usage

1. Place your .txt data in the ./input_docs directory (optional)

2. Create vector store:
   ```bash
   python vector_store.py
   ```

3. Start chatting:
   ```bash
   python chat.py
   ```
   
## Contributing

Feel free to contribute by submitting issues or pull requests.
