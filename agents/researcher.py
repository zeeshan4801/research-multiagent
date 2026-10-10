from crewai import Agent

from config.llm_config import groq_llm



research_agent = Agent(

    role="Research Analyst",

    goal="""
    Analyze collected research information.
    Create structured research notes.
    """,

    backstory="""
    You are a professional research analyst.
    You convert information into useful findings.
    """,

    llm=groq_llm,

    max_iter=2,

    verbose=True

)
