import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

load_dotenv()

llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

# Memory object stores past conversation
memory = ConversationBufferMemory()

# ConversationChain ties LLM and memory together
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

print("🧠 Memory Chatbot is ready! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("👋 Bye!")
        break

    response = conversation.run(user_input)
    print(f"Bot: {response}")
