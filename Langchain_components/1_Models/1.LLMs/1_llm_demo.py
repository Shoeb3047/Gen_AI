from langchain_openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo-instruct")

result = llm.invoke("What is the captial of India")

print(result)


# LLM takes input as string and give output as string
# Use of LLM is getting outdated , industry has moved to chat models specialzed for conversation tasks.