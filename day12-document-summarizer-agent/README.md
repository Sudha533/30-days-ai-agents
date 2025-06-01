
# Document Summarizer Agent

A Python-based AI agent that loads and chunks PDF documents, creates vector embeddings for efficient retrieval, and generates concise summaries using OpenAI’s language models.

---

## Features

- **PDF Loader & Chunking:** Splits PDFs into manageable chunks for effective processing.
- **Vector Store Retrieval:** Uses FAISS and OpenAI embeddings for semantic search.
- **Document Summarization:** Automatically generates a concise summary of the entire document using a map-reduce summarization chain.
- **Batch Processing:** Runs summarization without requiring user interaction during runtime.

---

## Requirements

- Python 3.8+
- OpenAI API Key

### Install dependencies

```bash
pip install langchain langchain-openai langchain-community faiss-cpu python-dotenv
```

---

## Setup

1. Clone or download this repository.
2. Create a `.env` file in the root directory and add your OpenAI API key:

```
OPENAI_API_KEY=your_openai_api_key
```

3. Place your PDF file (e.g., `mastering-ai-agents-galileo.pdf`) in the project directory.

---

## Usage

Run the summarization script:

```bash
python document_summarizer_agent.py
```

The script will process the PDF, split it into chunks, and output a final concise summary without requiring user input.

---

## Code Overview

- **Document Loading:** Uses `PyPDFLoader` to load and chunk PDF pages.
- **Text Splitting:** Uses `RecursiveCharacterTextSplitter` to split documents into chunks.
- **Embedding & Vector Store:** Creates embeddings with OpenAI and stores them in FAISS for efficient retrieval.
- **Summarization Chain:** Uses a map-reduce chain for summarizing document chunks.
- **Output:** Prints the final concise summary to the console.

## Notes

- Adjust chunk size and overlap parameters for better results.
- API usage may incur costs depending on your OpenAI plan.
- Extend functionality by adding retrieval or interactive question answering as needed.



