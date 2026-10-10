from crewai import Agent

from config.llm_config import groq_llm



analyst_agent = Agent(

    role="Research Analyst",

    goal="""
    Extract insights, trends and conclusions
    from verified information.
    """,

    backstory="""
    You specialize in analyzing research data.
    """,

    llm=groq_llm,

    max_iter=2,

    verbose=True

)
