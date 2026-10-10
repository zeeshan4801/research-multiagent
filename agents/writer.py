from crewai import Agent

from config.llm_config import groq_llm



writer_agent = Agent(

    role="Report Writer",

    goal="""
    Write a concise professional
    research report.
    """,

    backstory="""
    You create clear structured
    business-quality reports.
    """,

    llm=groq_llm,

    max_iter=2,

    verbose=True
)
