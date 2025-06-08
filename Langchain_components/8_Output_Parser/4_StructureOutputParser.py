from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3', description='Fact 3 about the topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Give 3 fact about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

# Manual approach alternative
# prompt = template.invoke({'topic': 'black hole'})
# result = model.invoke(prompt)
# # Extract the content from AIMessage
# content = result.content
# # Remove the json code block markers if present
# if content.startswith('```json') and content.endswith('```'):
#     content = content[7:-3].strip()

# # Parse the result
# parsed_result = parser.parse(content)    
# print(parsed_result)

chain = template | model | parser
result = chain.invoke({'topic':'black hole'})
print(result)