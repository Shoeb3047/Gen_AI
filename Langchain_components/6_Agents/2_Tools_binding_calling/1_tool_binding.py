# Goal : Bind the custom tools to LLM 
from langchain_core.tools import tool
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()
# Customs tool

@tool
def add(a: int, b: int)-> int:
    """Add two numbers."""
    return a + b

@tool
def subtract(a: int, b: int)-> int:
    """Subtract two numbers."""
    return a - b    

@tool
def multiply(a: int, b: int)-> int:
    """Multiply two numbers."""
    return a * b    

@tool
def divide(a: int, b: int)-> float: 
    """Divide two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

# Bind the custom tools to LLM
llm = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0.1,
    # max_tokens=1000,
    # tools=[add, subtract, multiply, divide],
)


llm_with_tools = llm.bind_tools([add, subtract, multiply, divide])  

messages = []
query = HumanMessage("Can we multiply 3 with 1000")
messages.append(query)

# Invoke the LLM with tools
result = llm_with_tools.invoke(messages) 

messages.append(result) 
print(result.tool_calls[0])



tool_result = multiply.invoke(result.tool_calls[0])
messages.append(tool_result)
print(f"Tool Result: {tool_result}")
print(f"Tool Result Type : {type(tool_result)}")
final_result = llm_with_tools.invoke(messages).content
print(f"Final Result: {final_result}")


