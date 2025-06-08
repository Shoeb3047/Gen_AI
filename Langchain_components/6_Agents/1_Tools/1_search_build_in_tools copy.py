# Build in tools are tools that are provided by Langchain.
# They are used to perform common tasks such as searching the web, getting weather information, etc.
# These tools can be used in agents to perform tasks that require external information.

# Demo of build-in tools in Langchain : DuckDuckGoSearchResults
from langchain_community.tools import DuckDuckGoSearchResults
import json

# create a search tool
search_tool = DuckDuckGoSearchResults()

# User query
query = "What is current news about India?"

# Use the search tool to get results
results = search_tool.run(query)    

# Print the results
print(results)




print(search_tool.name)
print(search_tool.description)
print(search_tool.args)