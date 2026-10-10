from crewai import Agent

from config.llm_config import groq_llm

from tools.search_tool import web_search
from tools.webpage_tool import read_webpage



research_agent = Agent(

    role="Research Collector",

    goal="""
    Collect reliable information from the internet.
    Use search tools when needed.
    """,

    backstory="""
    You are an expert online researcher.
    You gather facts, statistics and sources.
    """,

    tools=[
        web_search,
        read_webpage
    ],

    llm=groq_llm,

    max_iter=2,

    verbose=True,

    allow_delegation=False
)
