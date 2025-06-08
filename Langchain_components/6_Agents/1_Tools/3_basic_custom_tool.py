# Goal : Building a custom tool in Langchain
# Steps:
# 1. Define a custom tool function
# 2. Add hint and description to the function
# 3. Add @tool decorator to the function

# Execution : Use invoke() method to call the tool

from langchain_core.tools import tool

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

result = multiply.invoke({"a": 2, "b": 3})
print(f"Result of multiplication: {result}")    

print(f"Name of the custom tool {multiply.name}")
print(f"Description of the custom tool {multiply.description}" )
print(f"Args of the custom tool {multiply.args} ")