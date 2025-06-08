# Method 2 : StructuredTool
# Steps:
# 1. Define a Pydantic model for input validation
# 2. Create a function that performs the desired operation
# 3. Use StructuredTool.from_function to create a tool from the function and model
# 4. Invoke the tool with structured input
# 5. Print the result
# 6. Print the tool's name, description, and args

from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field

class MultiplyInput(BaseModel):
    a: int = Field(required=True, description="First number to multiply")
    b: int = Field(required=True, description="Second number to multiply")
    
    
def multiply_func(a: int, b: int) -> int:
    return a * b

multiply_tool = StructuredTool.from_function(
    func=multiply_func,
    name="multiply",
    description="Multiply two numbers",
    args_schema=MultiplyInput,
)   

result = multiply_tool.invoke({"a": 2, "b": 3})
print(f"Result of multiplication: {result}")    
print(f"Name of the custom tool: {multiply_tool.name}")
print(f"Description of the custom tool: {multiply_tool.description}" )
print(f"Args of the custom tool: {multiply_tool.args} ")



