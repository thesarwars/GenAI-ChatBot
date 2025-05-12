from main import llm
from langchain.agents import AgentExecutor, create_tool_calling_agent, initialize_agent
from langchain_community.tools import Tool, WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_deepseek import ChatDeepSeek
import os

# print(llm.invoke("hello world"))

wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
tools = [wikipedia]
agent = initialize_agent(llm=llm, tools=tools, agent="zero-shot-react-description", verbose=True)
response = agent.invoke({"input": "What is the age of Donald Trump right now?"})

print(response["output"])