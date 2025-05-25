import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from serpapi import GoogleSearch
import json

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
serpapi_key = os.getenv("SERPAPI_API_KEY")
if not serpapi_key:
    raise ValueError("Please set your SERPAPI_API_KEY in the .env file")
if not api_key:
    raise ValueError("Please set your OPENAI_API_KEY in the .env file")


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


# Prompt for Dynamic Info Extraction
template = """
You are an expert information extractor.

Given the following web search summary about a person, company, or movie, analyze the content and extract relevant information in clean JSON format.

The JSON format should follow these rules:
- If it's a person:
  {{
    "type": "person",
    "full_name": "...",
    "birth": {{
      "year": "...",
      "place": "..."
    }},
    "fields": ["..."],
    "achievements": [
      {{
        "title": "...",
        "year": "..."
      }}
    ]
  }}
- If it's a company:
  {{
    "type": "company",
    "name": "...",
    "founded": {{
      "year": "...",
      "location": "..."
    }},
    "industry": "...",
    "key_people": ["..."],
    "products": ["..."]
  }}
- If it's a movie:
  {{
    "type": "movie",
    "title": "...",
    "release_year": "...",
    "director": "...",
    "genre": ["..."],
    "cast": ["..."],
    "plot": "..."
  }}

Here is the web search summary:
{search_summary}

Now, return the structured JSON only.
"""

# Prompt and chain setup
prompt = PromptTemplate(
    input_variables=["search_summary"],
    template=template
)

chain = LLMChain(llm=llm, prompt=prompt)

#End to End function
def dynamic_info_extractor(query):
    print("🔍 Searching the web...")
    search_summary = serpapi_search(query)
    print("✅ Search Complete. Extracting information...")
    try:
        response = chain.run(search_summary=search_summary)
        data = json.loads(response)
        print("🎯 Extracted Information:")
        print(json.dumps(data, indent=2))
    except Exception as e:
        print("⚠️ Failed to extract structured data. Here’s the raw response:")
        print(response)

# Step 5: CLI Input
print("🧠 Multi-Step Info Extractor (People, Companies, Movies)")
print("Type 'exit' to quit.")
while True:
    user_query = input("\nEnter a name/title/topic: ")
    if user_query.lower() == "exit":
        print("👋 Goodbye!")
        break
    dynamic_info_extractor(user_query)

    