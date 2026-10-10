from crewai import Agent

from config.llm_config import groq_llm



planner_agent = Agent(

    role="Research Planner",

    goal="""
    Create a clear research strategy.
    Identify important questions and areas.
    """,

    backstory="""
    You are an expert research planner
    who organizes complex research.
    """,

    llm=groq_llm,

    max_iter=2,

    verbose=True

)
