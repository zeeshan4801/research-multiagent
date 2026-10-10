from crewai import Agent

from config.llm_config import groq_llm



fact_checker_agent = Agent(

    role="Fact Checker",

    goal="""
    Verify research information and identify
    unreliable statements.
    """,

    backstory="""
    You are a professional fact verification expert.
    """,

    llm=groq_llm,

    max_iter=2,

    verbose=True

)
