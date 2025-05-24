import os
from langchain.agents import initialize_agent,AgentType
from langchain.llms import OpenAI
from dotenv import load_dotenv
from serpapi import GoogleSearch
from langchain.agents import Tool

load_dotenv()

# Ensure OpenAI API Key is set in environment
api_key = os.getenv("OPENAI_API_KEY")
serpapi_key= os.getenv("SERPAPI_API_KEY")
if not serpapi_key:
    raise ValueError("Please set your SERPAPI_API_KEY in the .env file")
if not api_key:
    raise ValueError("Please set your OPENAI_API_KEY in the .env file")

# Load LLM
llm = OpenAI(temperature=0)

def serpapi_search(query: str) -> str:
    params = {
        "engine": "google",
        "q": query,
        "api_key": serpapi_key,
        "num": "3"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    if "organic_results" in results:
        snippets = [res.get("snippet", "") for res in results["organic_results"][:3]]
        return "\n".join(snippets)
    return "No results found."

# Create a LangChain Tool using the above function
search_tool = Tool(
    name="SerpAPI Search",
    func=serpapi_search,
    description="Useful for answering questions by searching the web."
)

# Initialize the agent with tools
agent = initialize_agent(
    tools=[search_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

print("🌐 Web Search Agent - Ask real-time questions. Type 'exit' to quit.")
while True:
    query = input("You: ")
    if query.lower() == "exit":
        print("👋 Goodbye!")
        break

    try:
        response = agent.run(query)
        print(f"🤖 Answer: {response}")
    except Exception as e:
        print(f"⚠️ Error: {e}")

