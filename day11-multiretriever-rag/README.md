# 📚 Multi-Retriever RAG with LangChain, PDF, and Web Search

This project demonstrates a **Retrieval-Augmented Generation (RAG)** application using **multiple retrievers**: one that extracts information from a PDF and another that fetches real-time data using **SerpAPI web search**. Built with LangChain and OpenAI, this app routes user questions to the most relevant information source.

---

## ✨ Features

- 🧠 Uses **LangChain's `MultiRetrievalQAChain`** to handle multiple sources of information
- 📄 Retrieves answers from a local **PDF document** using FAISS vector store
- 🌐 Fetches real-time answers from the **web using SerpAPI**
- 💬 Powered by **OpenAI's Chat Model** (`ChatOpenAI`)
- 🔁 Dynamically routes queries to the most relevant retriever

---

## 🛠️ Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

Make sure the following libraries are installed:

- `langchain`
- `langchain_openai`
- `serpapi`
- `python-dotenv`
- `faiss-cpu` or `faiss`

### 2. Set Up Environment Variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your-openai-api-key
SERPAPI_API_KEY=your-serpapi-api-key
```

---

## 🚀 Run the App

```bash
python day11_multiretriver_rag.py
```

Then enter questions like:

- "What is covered in the AI Agents PDF?"
- "Who is the CEO of Google?"
- "Give me insights on LangChain from the PDF."

Type `exit` to quit.

---

## 📌 Project Structure

```
.
├── mastering-ai-agents-galileo.pdf     # PDF used for local document retrieval
├── day11_multiretriver_rag.py          # Main application script
├── .env                                # API keys (not committed to version control)
├── README.md
└── requirements.txt
```

---

## 🧩 How It Works

1. **PDF Retriever**  
   - Loads PDF
   - Splits it into pages
   - Embeds using `OpenAIEmbeddings`
   - Stores in FAISS vector DB

2. **Web Retriever**  
   - Custom retriever using `serpapi` for Google Search
   - Returns search snippets as documents

3. **MultiRetrievalQAChain**  
   - Combines both retrievers
   - Routes user question based on descriptions and returns the best-matched answer

---

## 🧪 Tested With

- Python 3.10+
- LangChain `v0.3.25`
- OpenAI API
- SerpAPI

---

## ✅ Recent Fix

### ❗ Issue: `conversation_llm must be provided`
With LangChain v0.3+, `MultiRetrievalQAChain` requires both `llm` and `conversation_llm` to be explicitly passed.

✅ **Fix:**

```python
llm = ChatOpenAI(temperature=0)
qa_chain = MultiRetrievalQAChain.from_retrievers(
    llm=llm,
    conversation_llm=llm,
    ...
)
```

---


