from crewai import Agent

from config.llm_config import groq_llm



writer_agent = Agent(

    role="Professional Report Writer",

    goal="""
    Create a professional final research report.
    """,

    backstory="""
    You write clear structured reports.
    """,

    llm=groq_llm,

    max_iter=2,

    verbose=True

)
