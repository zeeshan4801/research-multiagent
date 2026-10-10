from crewai import Agent

from config.llm_config import groq_llm



fact_checker_agent = Agent(

    role="Fact Checker",

    goal="""
    Verify important information
    and remove unreliable claims.
    """,

    backstory="""
    You specialize in checking
    research accuracy.
    """,

    llm=groq_llm,

    max_iter=2,

    verbose=True
)
