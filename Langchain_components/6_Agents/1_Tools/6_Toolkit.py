# Toolkit : Collection of custom tools that can be used by agents in Langchain.
# Goal : Create a toolkit using Langchain's Toolkit class that includes the custom tool created in the previous step.



from langchain_core.tools import tool

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



class MathToolkit:
    """A toolkit for basic math operations."""


    def get_tools(self):
        """Return the tools in the toolkit."""
        return [add, subtract, multiply, divide]

# class MathToolkit:
#     """A toolkit for basic math operations."""

#     def __init__(self):
#         self.tools = {
#             "add": add,
#             "subtract": subtract,
#             "multiply": multiply,
#             "divide": divide
#         }

#     def get_tools(self):
#         """Return the tools in the toolkit."""
#         return self.tools

toolkit = MathToolkit()

tools = toolkit.get_tools()

print(f"Available tools in the MathToolkit: {tools}")

for tool in tools:
    print(f"{tool.name}: {tool.description}")