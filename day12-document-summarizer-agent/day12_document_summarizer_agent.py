import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document

load_dotenv()

# Initialize LLM
llm = ChatOpenAI(temperature=0, model="gpt-4")  # or "gpt-3.5-turbo"

# Load PDF
pdf_path = "./mastering-ai-agents-galileo.pdf"
loader = PyPDFLoader(pdf_path)
pages = loader.load()

# Step 1: Chunking the document
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separators=["\n\n", "\n", " ", ""]
)
docs = text_splitter.split_documents(pages)

# Step 2: Summarize in chunks (map-reduce)
summarize_chain = load_summarize_chain(
    llm=llm,
    chain_type="map_reduce",  # or try "refine"
    verbose=True
)

summary = summarize_chain.run(docs)

# Output
print("\n==== FINAL SUMMARY ====\n")
print(summary)
