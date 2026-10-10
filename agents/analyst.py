from crewai import Agent

from config.llm_config import groq_llm



analyst_agent = Agent(

    role="Research Analyst",

    goal="""
    Analyze verified information
    and create useful insights.
    """,

    backstory="""
    You convert research data
    into meaningful conclusions.
    """,

    llm=groq_llm,

    max_iter=2,

    verbose=True
)
