# Method 3 : BaseTool
# Steps:
# 1. Import BaseTool from langchain_core.tools
# 2. Define a Pydantic model for input validation
# 3. Create a class that inherits from BaseTool
# 4. Implement the _run method to define the tool's functionality
# 5. Define the name, description, and args properties
# 6. Create an instance of the custom tool class
# 7. Invoke the tool with structured input
# 9. Print the result, name, description, and args of the custom tool


from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type

class MultiplyInput(BaseModel):
    a: int = Field(required=True, description="The first number to add")
    b: int = Field(required=True, description="The second number to add")


class MultiplyTool(BaseTool):
    """Custom tool to multiply two numbers."""

    name: str = "multiply"
    description: str = "Multiply two numbers"
    args_schema: Type[BaseModel] = MultiplyInput

    def _run(self, a: int, b: int) -> int:
        """Run the multiplication operation."""
        return a * b
    
# Create an instance of the custom tool
multiply_tool = MultiplyTool()

# Invoke the tool with structured input
result = multiply_tool.invoke({"a": 2, "b": 3})
print(f"Result of multiplication: {result}")    
print(f"Name of the custom tool: {multiply_tool.name}")
print(f"Description of the custom tool: {multiply_tool.description}" )
print(f"Args of the custom tool: {multiply_tool.args_schema} ")



    
    






