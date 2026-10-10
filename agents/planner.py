from crewai import Agent

from config.llm_config import groq_llm


planner_agent = Agent(

    role="Research Planner",

    goal="""
    Create a simple research strategy.
    Identify important questions and areas.
    """,

    backstory="""
    You are an efficient research planner.
    You create clear research directions.
    """,

    llm=groq_llm,

    max_iter=2,

    verbose=True
)
