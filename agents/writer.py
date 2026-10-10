from crewai import Agent

from config.llm_config import groq_llm



writer_agent = Agent(

    role="Professional Research Report Writer",


    goal="""

Create clear, structured,
citation-aware research reports.

""",


    backstory="""

You are an expert business researcher
who converts research notes into
professional reports.

""",


    llm=groq_llm,


    max_iter=1,


    verbose=True

)
