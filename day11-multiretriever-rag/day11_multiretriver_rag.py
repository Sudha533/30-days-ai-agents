import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.chains.router import MultiRetrievalQAChain
from langchain.schema import BaseRetriever, Document
from serpapi import GoogleSearch

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

llm = ChatOpenAI(temperature=0)

# Load and embed PDF
pdf_path = "./mastering-ai-agents-galileo.pdf"
loader = PyPDFLoader(pdf_path)
pages = loader.load_and_split()

embedding = OpenAIEmbeddings()
db = FAISS.from_documents(pages, embedding)
pdf_retriever = db.as_retriever()

# Define SerpAPI retriever
class SerpAPIRetriever(BaseRetriever):
    def _get_relevant_documents(self, query: str) -> list[Document]:
        params = {
            "engine": "google",
            "q": query,
            "api_key": SERPAPI_API_KEY,
            "num": "3"
        }
        search = GoogleSearch(params)
        results = search.get_dict()
        snippets = [res.get("snippet", "") for res in results.get("organic_results", [])[:3]]
        text = "\n".join(snippets) if snippets else "No results found."
        return [Document(page_content=text)]

web_search_retriever = SerpAPIRetriever()

# Define a default QA chain (for fallback)
default_qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=pdf_retriever,
    verbose=True,
)

# Create MultiRetrievalQAChain
qa_chain = MultiRetrievalQAChain.from_retrievers(
    llm=llm,
    retriever_infos=[
        {
            "name": "pdf",
            "description": "Information from the PDF document",
            "retriever": pdf_retriever,
        },
        {
            "name": "web",
            "description": "Real-time web search using SerpAPI",
            "retriever": web_search_retriever,
        },
    ],
    
    default_chain=default_qa_chain,
    verbose=True,
)

# Chat loop
while True:
    question = input("Ask a question (or type 'exit'): ")
    if question.lower() == "exit":
        break
    answer = qa_chain.run(question)
    print(f"\nAnswer: {answer}\n")
