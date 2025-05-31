import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import MultiRetrievalQAChain
from langchain.schema import BaseRetriever  # base class for retrievers

from serpapi import GoogleSearch

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("Please set your OPENAI_API_KEY in the .env file")
if not SERPAPI_API_KEY:
    raise ValueError("Please set your SERPAPI_API_KEY in the .env file")

# Initialize conversational LLM
llm = ChatOpenAI(temperature=0)

# Step 1: Load PDF and split into pages
pdf_path = "./mastering-ai-agents-galileo.pdf"
loader = PyPDFLoader(pdf_path)
pages = loader.load_and_split()

# Step 2: Create embeddings and vectorstore retriever for PDF
embedding = OpenAIEmbeddings()
db = FAISS.from_documents(pages, embedding)
pdf_retriever = db.as_retriever()

# Step 3: Define SerpAPI search function
def serpapi_search(query: str) -> str:
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_API_KEY,
        "num": "3"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    if "organic_results" in results:
        snippets = [res.get("snippet", "") for res in results["organic_results"][:3]]
        return "\n".join(snippets)
    return "No results found."

# Step 4: Implement SerpAPIRetriever as a subclass of BaseRetriever
class SerpAPIRetriever(BaseRetriever):
    def get_relevant_documents(self, query: str):
        result = serpapi_search(query)
        # Return as list of documents with "page_content" key
        return [{"page_content": result}]

web_search_retriever = SerpAPIRetriever()

# Step 5: Create MultiRetrievalQAChain with retriever_infos
qa_chain = MultiRetrievalQAChain.from_retrievers(
    llm=llm,
    conversation_llm=llm,
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
    verbose=True,
)

# Step 6: Interactive Q&A loop
print("Ask questions about the PDF or the web. Type 'exit' to quit.")
while True:
    question = input("\nYour question: ")
    if question.lower() == "exit":
        print("Goodbye!")
        break
    answer = qa_chain.run(question)
    print(f"\nAnswer:\n{answer}")
