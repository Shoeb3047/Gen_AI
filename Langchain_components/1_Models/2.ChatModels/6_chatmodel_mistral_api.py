from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv

load_dotenv()


model = ChatMistralAI(model_name='mistral-large-latest')

result = model.invoke("What is the capital of India")

print(result.content)

