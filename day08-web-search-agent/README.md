# Web Search Agent with SerpAPI and LangChain

This project demonstrates a simple web search agent using LangChain and SerpAPI. The agent performs real-time web searches to answer user queries by calling the Google Search API through SerpAPI and generates responses using OpenAI.

## Features

- Uses LangChain `initialize_agent` with tools and OpenAI LLM.
- Calls SerpAPI Google Search to fetch live search results.
- Answers user questions with web search data combined with reasoning.
- Simple interactive command-line interface.

## Prerequisites

- Python 3.7+
- An OpenAI API key
- A SerpAPI API key

## Installation

1. Clone the repository or copy the script.

2. Install required packages:

```bash
pip install langchain openai python-dotenv serpapi
```

3. Create a `.env` file in the project directory with your API keys:

```
OPENAI_API_KEY=your_openai_api_key_here
SERPAPI_API_KEY=your_serpapi_api_key_here
```

## Usage

Run the script:

```bash
python day08_web_search_agent.py
```

Type your question, and the agent will search the web and respond.

Type `exit` to quit the program.

## Code Overview

- Loads API keys from environment variables.
- Defines a search function that calls SerpAPI.
- Wraps the search function as a LangChain tool.
- Initializes a LangChain zero-shot agent with the tool.
- Runs an interactive prompt for user queries.

## Notes

- Make sure your API keys are valid.
- SerpAPI may have usage limits on free plans.
- The LangChain agent uses zero-shot reasoning to decide when to call the search tool.

---


