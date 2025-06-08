from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv


load_dotenv()

model = ChatGoogleGenerativeAI(model="claude-3-5-sonnet-20241022", temperature=1.0, max_completion_token=10)

result = model.invoke("What is the capital of Delhi?")

print(result.content)