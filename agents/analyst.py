from crewai import Agent

from config.llm_config import groq_llm


analyst_agent = Agent(

    role="Research Data Analyst",

    goal="""
    Analyze collected research data.
    Find important patterns,
    trends and insights.
    """,

    backstory="""
    You are a professional research analyst
    who converts raw information into insights.
    """,

    llm=groq_llm,

    verbose=True
)
