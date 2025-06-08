# Build in tools are tools that are provided by Langchain.
# They are used to perform common tasks such as searching the web, getting weather information, etc.
# These tools can be used in agents to perform tasks that require external information.

# Demo of build-in tools in Langchain : Shell Commands
from langchain_community.tools import ShellTool


# create a search tool
shell_tool = ShellTool()

# User query
cmd = "whoami"

# Use the search tool to get results
results = shell_tool.run(cmd)    

# Print the results
print(results)


print(shell_tool.name)
print(shell_tool.description)
print(shell_tool.args)