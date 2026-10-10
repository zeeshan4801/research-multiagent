from crewai import Agent
from config.llm_config import groq_llm



manager_agent=Agent(

    role="Research Manager",

    goal="""
    Manage the complete research process.
    Divide research tasks between agents.
    """,

    backstory="""
    You are a senior research director
    managing an AI research department.
    """,

    llm=groq_llm,

    verbose=True

)
