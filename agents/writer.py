from crewai import Agent

from config.llm_config import groq_llm


writer_agent = Agent(

    role="Professional Research Writer",

    goal="""
    Create a clear professional final report
    from research findings.
    """,

    backstory="""
    You are an expert technical writer.
    You create structured reports
    understandable by everyone.
    """,

    llm=groq_llm,

    verbose=True
)
