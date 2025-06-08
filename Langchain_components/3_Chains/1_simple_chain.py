from langchain_core.prompts import PromptTemplate
from langchain_mistralai import ChatMistralAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()



prompt = PromptTemplate(
    template = "Generate 5 interestic facts about {topic}",
    input_variables=["topic"]
)

model = ChatMistralAI(
    model_name="mistral-large-latest",
    temperature=0.1,) 

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic':'Langchain'})

print(result)
chain.get_graph().print_ascii()



























