# Goal : Create an AI agent that can convert currencies using a custom tool in real time


# I need to extract the current conversion rate between two currenies 
# 
from langchain_core.tools import InjectedToolArg
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from typing import Annotated
from langchain_mistralai import ChatMistralAI
import requests
import json
from dotenv import load_dotenv

load_dotenv()


@tool
def get_conversion_factor(base_currency: str, target_currency: str) -> float:
    """Fetch the conversion rate from an API between base_currency and target_currency
    """
    # Fetch the conversion rate from an API between base_currency and target_currency
    
    api_key = '864ef1b44f60e7015db450a7'  # Replace with your actual API key
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/{base_currency}/{target_currency}'

    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Error fetching conversion rate: {response.status_code}") 
    
    response.json()
    
    
@tool
def convert(base_currency_value: int, conversion_rate: Annotated[float,InjectedToolArg]) -> float:
    """
    given a currency conversion rate this function calculates the target currency value from a given base currency value
    """
    return base_currency_value * conversion_rate


# tool binding
llm = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0.1,
)

llm_with_tools = llm.bind_tools([get_conversion_factor, convert])   
messages = [HumanMessage('Only use availaible tool to answer this. What is the conversion factor between INR and USD, and based on that can you convert 10 inr to usd')]

ai_message = llm_with_tools.invoke(messages)
messages.append(ai_message)
print(ai_message.tool_calls)

# for tool_call in ai_message.tool_calls:
#   # execute the 1st tool and get the value of conversion rate
#   if tool_call['name'] == 'get_conversion_factor':
#     tool_message1 = get_conversion_factor.invoke(tool_call)
#     # fetch this conversion rate
#     conversion_rate = json.loads(tool_message1.content)['conversion_rate']
#     # append this tool message to messages list
#     messages.append(tool_message1)
#   # execute the 2nd tool using the conversion rate from tool 1
#   if tool_call['name'] == 'convert':
#     # fetch the current arg
#     tool_call['args']['conversion_rate'] = conversion_rate
#     tool_message2 = convert.invoke(tool_call)
#     messages.append(tool_message2)
    

# final_answer = llm_with_tools.invoke(messages).content
# print(f"Final Answer: {final_answer}")


# Using AI agent for the same task
from langchain.agents import initialize_agent, AgentType


# Step 5: Initialize the Agent ---
agent_executor = initialize_agent(
    tools=[get_conversion_factor, convert],
    llm=llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,  # using ReAct pattern
    verbose=True  # shows internal thinking
)


# --- Step 6: Run the Agent ---
user_query = "Only use availaible tool to answer this. What is the conversion factor between INR and USD, and based on that can you convert 10 inr to usd"


response = agent_executor.invoke({"input": user_query})