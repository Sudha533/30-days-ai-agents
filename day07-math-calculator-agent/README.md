# 🧮 Day 07 - Math Calculator Agent (LangChain + Python REPL)

This is Day 07 of the 30 Days of AI Agents challenge. In this project, we build a simple Math Calculator Agent using LangChain's `PythonREPL` tool to evaluate math expressions and reasoning-based calculations through code execution.

---

## 🎯 What It Does

- Accepts math and logical questions in natural language
- Uses OpenAI LLM to decide what to do
- Executes Python code through `PythonREPL` to get accurate answers
- Interacts with the user in a continuous loop

---

## 🧰 Tech Stack

- [LangChain](https://github.com/langchain-ai/langchain)
- [OpenAI API](https://platform.openai.com/)
- [Python REPL Tool](https://docs.langchain.com/docs/integrations/tools/python_repl)
- `python-dotenv` for managing environment variables

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/30-days-ai-agents.git
cd 30-days-ai-agents/day07-math-calculator-agent
```

### 2. Create a virtual environment (optional)

```bash
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install langchain langchain-community langchain-experimental openai python-dotenv
```

### 4. Set up your `.env` file

Create a `.env` file in the root of your project with the following line:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 5. Run the agent

```bash
python day07_math_calculator_agent.py
```

---

## 📦 Example Usage

```bash
🤖 Ask a math question! Type 'exit' to quit.
You: What is 15 * (2 + 5)?
🤖 Answer: 105

You: What is the factorial of 5?
🤖 Answer: 120
```

---

## 💡 How It Works

- The LLM receives a natural language query.
- It determines the required computation using LangChain’s **zero-shot-react-description** agent type.
- The PythonREPL tool executes the required Python code.
- The result is returned to the user.

---

## 📁 File Structure

```
📁 day07-math-calculator-agent/
├── day07_math_calculator_agent.py
├── .env
├── README.md
└── requirements.txt
```

---

## 🚀 Future Enhancements

- Add more tools (e.g., Wolfram Alpha, math libraries)
- Introduce memory to recall past questions
- Log history of questions and answers

---

