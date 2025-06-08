
# Goal : WAP using langchaing with StrOutputParser to demonstrate how it helps.
# Take a detailed report of {topic} and summarize it in 5 points

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


# Define the model
model = ChatMistralAI(
    model_name="mistral-large-latest",
    temperature=0.1,)

# Define the prompt template
prompt_template_1 = PromptTemplate(
    template="Take a detailed report of {topic}",
    input_variables=["topic"])


prompt_template_2 = PromptTemplate(
    template="Summarize the folloowing report in 5 points\n {report}",
    input_variables=["report"]
    )

stroutput_parser = StrOutputParser()

chain = prompt_template_1 | model | stroutput_parser | prompt_template_2 | model | stroutput_parser 


result_chain = chain.invoke({"topic": "Langchain"})
print(f'This is the summary of the report using StrOutputParser:\n{result_chain}\n')

