from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv


load_dotenv()

model = ChatMistralAI(model_name="mistral-large-latest")


# Document
loader = TextLoader("cricket.txt",encoding="utf-8")
docs = loader.load()



# Prompt
poem = docs[0]
prompt = PromptTemplate(
    template='Write a summary in 5 lines for the following poem - \n {poem}',
    input_variables=['poem']
)


# Output parser
parser = StrOutputParser()

chain = prompt | model | parser

print(chain.invoke({'poem':docs[0].page_content}))