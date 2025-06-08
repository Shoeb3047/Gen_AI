from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

# model = ChatMistralAI(
#     model_name="mistral-large-latest",
#     temperature=0.1,)
parser = JsonOutputParser()

# template = PromptTemplate(
#     template='Give me 5 facts about {topic} \n {format_instruction}',
#     input_variables=['topic'],
#     partial_variables={'format_instruction': parser.get_format_instructions()}
# )


template = PromptTemplate(
    template=(
        'Give me 5 facts about {topic} in the following JSON format:\n'
        '{format_instruction}\n'
        'Ensure all strings are valid JSON (e.g., escape inner double quotes with a backslash).'
    ),
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)


# # Non chain approach
# # Manual approach alternative
# prompt = template.invoke({'topic': 'black hole'}) 
# result = model.invoke(prompt)
# # print(result)
# # Extract the content from AIMessage
# content = result.content
# # Remove the json code block markers if present
# if content.startswith('```json') and content.endswith('```'):
#     content = content[7:-3].strip()

# Parse the result
# parsed_result = parser.parse(content)    
# print(parsed_result)



# Create chain
chain = template | model | parser

# Invoke the chain
result = chain.invoke({'topic': 'black hole'})
print(result)

