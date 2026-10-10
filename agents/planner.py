from crewai import Agent
from config.llm_config import groq_llm



planner_agent=Agent(

role="Research Planner",

goal="""
Create a detailed research plan.
Identify questions that need answers.
""",

backstory="""
Expert academic research planner.
""",

llm=groq_llm,

verbose=True

)
