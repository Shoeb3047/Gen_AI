from langchain_core.prompts import PromptTemplate
from langchain_mistralai import ChatMistralAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv  


load_dotenv()

prompt1 = PromptTemplate(
    template = "Generate a detailed report of around 500 words for the following topic.\n {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template = "Summarize the following report in 5 points.\n {report}",
    input_variables=["report"]
)

model = ChatMistralAI(
    model_name="mistral-large-latest",
    temperature=0.1,
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({"topic": "Langchain"})

print(result)

chain.get_graph().print_ascii()

