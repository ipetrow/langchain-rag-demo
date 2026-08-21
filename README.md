# Project Overview
The project presents a *2-Step, Retrieval-Augmented Generation (RAG)* question and answers application built around *LangChain*, an *LLM API*, an *in-memory vector store* and *Python*. Furthermore, it explores several types of *Evaluation Testing* techniques for ensuring the correctness and the relevance of the RAG implementation.

# Use Case
The application helps users to retrieve relevant information from their book journal entries filled during their reading activities. This helps readers to understand better their reading habits, preferences and emotional connection to stories.

# Implementation Scope
The goals of the implementation were to explore the following concepts:
- Exploring the *LangChain* framework and the provided models and prompts interfaces.
- Understanding the *Retrieval-Augmented Generation* (RAG) architectural pattern.
- Exploring the *RAG* techniques for *Evaluation testing*.

## Out of Scope
- An exhaustive implementation of the multiple RAG evaluation test types.

# Project Structure
Application structure:
- The application codebase is situated in the `src/app/` Python module.
- `__main__.py`: The entry point of the application responsible for the initial configuration steps and the initialization of the interactive user interface.
- `services/`: Contains external model integrations that require API keys and endpoints.
- `chat_session.py`: Contains the interactive user interface.
- `document_loader.py`: Converts the csv data into *LangChain* `Document` objects.
- `vectorstore.py`: Contains the vector store related logic.
- `rag.py`: Contains the Retrieval-Augmented Generation flow logic.

Tests structure:
- The tests are separated from the application codebase and are situated in `tests/`.
- `tests/evals/`: Contains all evaluation tests.
- `tests/unit`: Contains all unit tests.

# Prerequisites 
- Installed Python version 3.14.2 or higher.
- Installed Python `uv` package and project management tool. A basic understanding of how the tool works would be helpful for a better insight of how the project is set up and executed.
- Deployed in *Azure* embedding and large language models.
- The embedding and large language model names, API keys, endpoints included in the environment variables.

# Implementation Details

## Application Configuration
On application start the vector store is being filled with predefined book journal entries. The process includes the transformation of text csv data into *LangChain* `Document` objects (`src/app/document_loaded.py`) which are subsequently embedded by an embedding model and added in the vector store.

## RAG
The application presents a *2-Step, Semantic search* RAG implementation. This RAG type characterizes with the retrieval steps always happening before the generation.

Once the configuration completes, each user's question is handled in `src/app/rag.py` where the semanticly related documents are retrieved (*Retrieval* step), concatenated together as context using the `stuff` approach (*Augmentation* step) and together with the question send to the LLM for generating the answer (*Generation* step).

## Models
The application relies on an embedding model used for preparing the embeddings for the vector store and an LLM used for the user interaction layer for handling the questions and answers functionality. 

Both processes are independent from each other which allows the use of different providers. The implementation utilizes this option by using the OpenAI embedding model `text-embedding-3-small` and the Anthropic LLM `claude-sonnet-4-6`.

## Vector Store
The vector store used is the in-memory implementation `InMemoryVectorStore` provided by *LangChain*. Its usage simplicity makes it a good candidate for a demo application.

The embedding model, used for the transformation of the text book journal entries into a vector of numbers, is the standard *LangChain* interface `OpenAIEmbeddings`.

After its configuration, the vector store is being filled with the embeddings of multiple predefined book journal entries situated in `data/book_journal_entries.csv`. The dataset path for the production application is set in the `.env` file and read in `src/app/services/config.py`.

# Running the Project
## Setup
1. Clone the repository: `git@github.com:ipetrow/langchain-rag-demo.git`.
2. Sync the project in order to download and install all the required project dependencies and they are up to date: `uv sync`. This will create the project virtual environment (`.venv`) as well.
3. Ensure the embedding model name (`AZURE_EMBEDDING_MODEL`), API key (`AZURE_EMBEDDING_MODEL_API_KEY`) and endpoint (`AZURE_EMBEDDING_MODEL_ENDPOINT`) environment variables are correctly set. They are read in `src/app/services/config.py`.
4. Ensure the LLM model name (`AZURE_LLM_MODEL`), API key (`AZURE_LLM_API_KEY`) and endpoint (`AZURE_LLM_ENDPOINT`) environment variables are correctly set. They are read in `src/app/services/config.py`.

## Execution
The application can be started with the command `uv run python -m src.app`.

# Evaluation Tests
There are 3 types of evaluation tests implemented.

## Type 1: Correctness
This test evaluates that a generated LLM answer is similar to a ground-truth answer. The comparison process is using an LLM-as-a-judge approach in which an independent LLM, provided also with the original question, compares both answers for similarity.

The essence of this type of test requires to prepare in advance a test dataset that contains a list of question and ground-truth answer items.

The answers' correctness evaluation is implemented in `tests/evals/test_answers_correctness.py`.

## Type 2: Relevance
This test evaluates that a generated by an LLM answer properly addresses the question. Similarly to *Type 1*, the evaluation is being made using an LLM-as-a-judge approach. However, a major difference is that preparing a ground-truth answer is not needed. This simplifies the implementation.

The answers' relevance evaluation can be found in `tests/evals/test_answers_relevance.py`.

## Type 3: Retrieval Correctness
This test asserts the retriever, based on the provided question, returns the expected book jounrnal entries' ids. In relation to the other two types, here the LLM-as-a-judge approach is not used. The comparison is deterministic, using Python. 

The implementation is in `tests/evals/test_documents_retrieval.py`.

## Implementation Details
During the tests setup phase, the vector store is being filled with the embeddings of multiple predefined book journal entries situated in `tests/data/test_book_journal_entries.csv`. The dataset path, used for the tests only, is set in the `.env.test` file and read in `src/app/services/config.py`.

## Execution
- For executing one of the tests: `uv run python -m pytest tests/evals/test_answers_correctness.py`.
- For executing all tests: `uv run python -m pytest`.

**Note**: To see the execution log messages, use `pytest` with `-s`.  
