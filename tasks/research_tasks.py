from crewai import Task



def create_tasks(
    planner,
    researcher,
    fact_checker,
    analyst,
    writer,
    topic,
    research_data
):


    planning_task = Task(

        description=f"""
Create a short research plan for:

{topic}
""",

        expected_output="""
5 bullet point research plan.
""",

        agent=planner
    )


    research_task = Task(

        description=f"""
Summarize this research data:

{research_data}

Extract only important facts.
""",

        expected_output="""
Short research summary.
""",

        agent=researcher
    )


    fact_task = Task(

        description="""
Check the research summary.
Find possible incorrect claims.
""",

        expected_output="""
Short verification notes.
""",

        agent=fact_checker
    )


    analysis_task = Task(

        description="""
Extract the main insights.
""",

        expected_output="""
5 important insights.
""",

        agent=analyst
    )


    writing_task = Task(

        description="""
Write a concise final report.
""",

        expected_output="""
A short professional report.
""",

        agent=writer
    )


    return [

        planning_task,
        research_task,
        fact_task,
        analysis_task,
        writing_task

    ]
