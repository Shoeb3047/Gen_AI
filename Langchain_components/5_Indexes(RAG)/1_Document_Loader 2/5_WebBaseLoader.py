from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
load_dotenv()

url = "https://www.flipkart.com/apple-macbook-air-m2-16-gb-256-gb-ssd-macos-sequoia-mc7x4hn-a/p/itmdc5308fa78421"
loader = WebBaseLoader(url)   # url or list of url can also be provided


#Case 1
docs = loader.load()
# print(type(docs), len(docs))  # List : Every loader return a python list of documents objects
# print(docs[0].page_content)                       # 1. page_content 2. metadata




model = ChatMistralAI(model_name="mistral-large-latest")

# Prompt

prompt = PromptTemplate(
    template='What are the three best feature of this product - \n {webcontent}',
    input_variables=['webcontent']
)


# Output parser
parser = StrOutputParser()

chain = prompt | model | parser

print(chain.invoke({'webcontent': docs[0].page_content}))