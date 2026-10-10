from crewai import Agent

from config.llm_config import groq_llm


fact_checker_agent = Agent(

    role="Fact Checking Specialist",

    goal="""
    Verify research information.
    Identify incorrect claims.
    Check reliability of sources.
    """,

    backstory="""
    You are an expert fact checker.
    Your job is to make sure research
    reports contain accurate information.
    """,

    llm=groq_llm,

    verbose=True
)
