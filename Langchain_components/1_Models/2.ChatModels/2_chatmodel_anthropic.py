from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv


load_dotenv()

model = ChatAnthropic(model="gpt-4o", temperature=1.5, max_completion_token=10)

result = model.invoke("What is the capital of Delhi?")

print(result.content)