from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


load_dotenv()

model = ChatOpenAI(model="gpt-4o", temperature=1.5, max_completion_token=10)

result = model.invoke("What is the capital of Delhi?")

print(result.content)