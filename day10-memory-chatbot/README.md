
# 🧠 Day 10 - Memory Chatbot 

This project builds a chatbot that can remember past parts of a conversation. It uses LangChain's memory capabilities to create a more intelligent and interactive experience.

---

## 🎯 Goal

Create a chatbot that:
- Remembers user input (like names, preferences)
- Responds with context-awareness
- Feels more like a natural conversation

---

## 🛠️ Requirements

Install the necessary packages:

```bash
pip install langchain openai python-dotenv
```

---

## 🔐 Environment Setup

Create a `.env` file in the root directory and add:

```env
OPENAI_API_KEY=your-openai-api-key
```

---

## 🧠 Memory Types Used

This example uses:

- `ConversationBufferMemory` — stores **all** conversation history.

---

## 💡 How It Works

### 1. Load Environment Variables

```python
from dotenv import load_dotenv
load_dotenv()
```

### 2. Load the Chat Model

```python
from langchain.chat_models import ChatOpenAI
llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
```

### 3. Add Memory

```python
from langchain.memory import ConversationBufferMemory
memory = ConversationBufferMemory()
```

### 4. Create a Conversation Chain

```python
from langchain.chains import ConversationChain
conversation = ConversationChain(llm=llm, memory=memory, verbose=True)
```

### 5. Chat Loop

```python
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = conversation.run(user_input)
    print("Bot:", response)
```

---

## 🧪 Example Conversation

```txt
You: My name is John.
Bot: Nice to meet you, John!

You: What’s my name?
Bot: You said your name is John.
```

---

## 📁 Project Structure

| File           | Purpose                             |
|----------------|-------------------------------------|
| `day10_memory_chatbot.py`      | Main chatbot script                 |
| `.env`         | Environment variables for API keys  |
| `README.md`    | This documentation file             |

---

## 📘 Notes

You can explore more memory types:
- `ConversationBufferWindowMemory`
- `ConversationSummaryMemory`

---

## 💡 Ideas to Extend

- Remember user preferences
- Store favorite topics or responses
- Personal assistant-style memory

---


