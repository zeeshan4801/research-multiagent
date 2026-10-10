from crewai import Agent

from config.llm_config import groq_llm

from tools.search_tool import web_search
from tools.webpage_tool import read_webpage



research_agent=Agent(

role="Internet Research Specialist",

goal="""
Find reliable information using research tools.
Collect important facts and sources.
""",

backstory="""
Professional online researcher skilled in
finding trustworthy information.
""",

tools=[
    web_search,
    read_webpage
],

llm=groq_llm,

verbose=True

)
