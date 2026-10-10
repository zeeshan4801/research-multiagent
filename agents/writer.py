from crewai import Agent

from config.llm_config import groq_llm



writer_agent = Agent(

    role="Report Writer",

    goal="""

Create a clear professional report.

""",

    backstory="""

You write concise business reports.

""",

    llm=groq_llm,

    max_iter=1,

    verbose=True

)
