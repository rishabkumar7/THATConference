from langchain_openai import OpenAI
from langchain.agents import (
    load_tools,
    initialize_agent,
    AgentType
)
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI()

tools = load_tools(["llm-math"], llm = llm)

agent = initialize_agent(
        tools,
        llm, 
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
        )

response = agent.run("What is Satya Nadella's age in 2024?")