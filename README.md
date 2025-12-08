# ML Exam Generator

This project is a multi-agent system designed to automatically generate exams based on provided educational materials. It utilizes `autogen-agentchat` for agent orchestration and `chonkie` for semantic document processing.

## Overview

The system works by:
1.  **Ingesting Content:** Reading markdown files from the `docs/` directory.
2.  **Indexing:** Chunking the content using semantic analysis and storing it in a ChromaDB vector database for efficient retrieval.
3.  **Generating Exams:** Using a team of AI agents (Planner, Creator, Verifier, Reviewer, Saver) to collaborate on creating, verifying, and saving exam questions.

## Prerequisites

-   **Python 3.12+**
-   **Google Gemini API Keys**

## Installation

### Option 1: Using uv (Recommended)

1.  Clone the repository.
2.  Install the dependencies using `uv`:
    ```bash
    uv sync
    ```

### Option 2: Using pip

If you prefer using standard `pip`:

1.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1.  Create a `.env` file in the root directory.
2.  Add your Gemini API keys. You can rotate between multiple keys if needed:

    ```dotenv
    GEMINI_EXAMK1=your_api_key_here
    GEMINI_EXAMK2=your_second_key_here
    GEMINI_EXAMK3=your_third_key_here
    ```

## Usage

### 1. Indexing Content

Before generating exams, you need to index your source materials. The `src/chunker.py` script reads markdown files from the `docs/` folder, splits them into semantic chunks, and stores them in the local ChromaDB instance.

```bash
# Using uv
uv run src/chunker.py

# Using python directly
python src/chunker.py
```

### 2. Running the Generator

To start the exam generation process, run the main script. This initializes the agent team and starts the workflow. The agents will collaborate to create an exam, which will be saved in the `exams/` directory.

```bash
# Using uv
uv run main.py

# Using python directly
python main.py
```

## Project Structure

-   `docs/`: Source markdown files for the exam content.
-   `exams/`: Generated exam files.
-   `src/`: Source code.
    -   `agents/`: Definitions for the different agents (Planner, Creator, etc.).
    -   `models/`: Configuration for LLM clients (Gemini, Ollama).
    -   `chunker.py`: Script for indexing documents.
    -   `memory.py`: Vector database interface.
-   `chroma_db/`: Local storage for the vector database.
-   `.env`: Environment variables for API keys.
