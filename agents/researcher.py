from crewai import Agent

from config.llm_config import groq_llm



research_agent = Agent(

    role="Research Analyst",

    goal="""

Analyze collected research data
and extract useful information.

""",

    backstory="""

You are a professional research analyst.

""",

    llm=groq_llm,

    max_iter=1,

    verbose=True

)
