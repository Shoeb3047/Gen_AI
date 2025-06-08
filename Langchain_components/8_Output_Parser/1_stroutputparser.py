
# Goal : WAP using langchaing without output parser to demonstrate what it takes
# Take a detailed report of {topic} and summarize it in 5 points

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv


load_dotenv()


# Define the model
model = ChatMistralAI(
    model_name="mistral-large-latest",
    temperature=0.1,)

# Define the prompt template
prompt_template_1 = PromptTemplate(
    template="Take a detailed report of {topic}",
    input_variables=["topic"])


prompt_tempplate_2 = PromptTemplate(
    template="Summarize the folloowing report in 5 points\n {report}",
    input_variables=["report"]
    )


prompt_1 = prompt_template_1.invoke({"topic": "Langchain"})

result = model.invoke(prompt_1)
report = result.content
# Now we have a report, let's summarize it
print(f'This the report on Langchain:\n{report}\n')
# Now we can use the report to summarize it
prompt_2 = prompt_tempplate_2.invoke({"report":report})
result_2 = model.invoke(prompt_2)
summary = result_2.content
print(f'This is the summary of the report:\n{summary}\n')




