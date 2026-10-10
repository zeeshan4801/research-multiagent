from crewai import Agent

from config.llm_config import groq_llm

from tools.search_tool import web_search
from tools.webpage_tool import read_webpage



research_agent = Agent(

    role="Research Collector",

    goal="""
    Collect reliable information
    using available research tools.
    """,

    backstory="""
    You are an online research specialist.
    Find useful facts and sources.
    """,

    tools=[

        web_search,
        read_webpage

    ],

    llm=groq_llm,

    max_iter=3,

    verbose=True
)
