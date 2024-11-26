# LLM-RAG-Chat-Agent

This repository combines AI techniques to build an interactive and intelligent chatbot. It integrates a **Large Language Model (LLM)** with **Retrieval-Augmented Generation (RAG)** and an **Agent** framework for enhanced information retrieval, reasoning, and real-time conversation capabilities. The project includes an automated CI/CD pipeline for seamless builds and tests, as well as unit tests to ensure the reliability and accuracy of the model.

## Features

- **LLM-Powered Chatbot:** Provides dynamic responses using a LLM
- **Retrieval-Augmented Generation (RAG):** Incorporates a retrieval mechanism to enhance responses with relevant context from external sources such as Wikipedia or Arxiv.
- **Agent Framework:** Enables the chatbot to make decisions and act autonomously to accomplish tasks, such as answering questions, fetching information, or solving problems.
- **Customizable Pipelines:** Easy integration and adaptation for various use cases, from question-answering systems to specialized knowledge assistants.
- **Automated CI/CD Pipeline:** Automatically builds and tests the application with each push to the repository or pull request.
  
## Use Cases

- Question answering based on external knowledge.
- Conversational AI with dynamic, context-aware responses.
- Enhanced knowledge retrieval using the RAG framework.
  
## Technologies

- **Gemini 1.5 Flash** (GenAI model).
- **FAISS (Facebook AI Similarity Search)**: Used as the core vector database (VectorDB) for storing and retrieving dense vector embeddings, enabling fast and scalable similarity search.
- **LangChain**: Provides tools for chaining large language model (LLM) tasks and integrating with FAISS for efficient retrieval.
- **Streamlit**: Creates an interactive UI for user queries and result visualization.

---

## Setup and Installation

### 1. Clone the repository.

### 2. Create .env file with GOOGLE_API_KEY environment variables.

### 3. If you don’t have conda installed, download and install Miniconda or Anaconda.

### 4. Set Up a Virtual Environment

```bash
conda env create -f environment.yml
```

## Run the Application locally

### 1. Activate conda env:

```bash
conda activate rag-agent
```

### 2. Start a local web server:

```bash
streamlit run app.py
```

### 3. The application will be available at the local address provided by Streamlit (usually http://localhost:8501).

### 4. Ask the question i.e.:

```bash
Give me information about document: 'Video Coding for Machines: Partial transmission of SIFT features'
```

## License

This project is licensed under the MIT License.
