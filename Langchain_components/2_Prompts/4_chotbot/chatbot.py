from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv

load_dotenv()

model = ChatMistralAI()

chat_history = []

while True:
    user_input = input('You: ')
    chat_history.append(user_input)
    if user_input.lower() == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(result.content)
    print("AI: ", result.content)

print(f"Chat History: {chat_history}")
